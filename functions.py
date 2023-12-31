import subprocess
import platform
import sys
import time
import serial.tools.list_ports
import serial
import os
import shutil
# from main import drinks

class SerialPort:
    def __init__(self, port, baudrate=115200, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial = None

    def open(self):
        self.serial = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
        time.sleep(2)  # Wait for the connection to stabilize

    def close(self):
        if self.serial and self.serial.is_open:
            self.serial.close()

    def read_data(self):
        if self.serial and self.serial.is_open:
            return self.serial.readline().decode("utf-8").strip()
        return None

    def send_data(self, data):
        if self.serial and self.serial.is_open:
            self.serial.write(data.encode())
            self.serial.flush()

def find_pico_port():
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if 'Pico' in port.description:
            return port.device
    return None


def get_commit_hash(self):
        try:
            # Run 'git rev-parse HEAD' command to get the commit hash
            result = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Error retrieving commit hash: {e}")
            return "Unknown"
        
def print_debug_info(self):
        # Print Python version
        python_version = sys.version
        print(f"Python Version: {python_version}")

        # Print OS information
        os_info = platform.platform()
        print(f"OS: {os_info}")

        # Print installed package versions
        print("Installed Packages:")
        try:
            result = subprocess.run([sys.executable, '-m', 'pip', 'freeze'], capture_output=True, text=True, check=True)
            installed_packages = result.stdout.split('\n')
            
            for package in installed_packages:
                print(package)
                
        except subprocess.CalledProcessError as e:
            print(f"Error retrieving installed package versions: {e}")     

def prepare_drink(self, drinkName):
    from main import drinks
     # Find the port of the Raspberry Pi Pico
    pico_port = find_pico_port()

    if pico_port is None:
        print("Raspberry Pi Pico not found. Make sure it is connected.")
        return

    print(f"Raspberry Pi Pico found on port: {pico_port}")

    # Open the serial connection
    with serial.Serial(pico_port, 115200, timeout=1) as ser:
        # Wait for the connection to stabilize
        # time.sleep(1)

        # Send 'hello world' over the serial port
        print("Preparing your drink!")
        # ser.write(b'P1-ON\n')
        # print("P1-ON\n")
        # ser.flush()
        # # time.sleep(3)
        # ser.write(b'P1-OFF\n')
        # print("P1-OFF\n")
        # cosmo_details = self.get_cocktail_by_name(drinkName)
        cosmo_details = drinks.get_cocktail_by_name(drinkName)
        # frame_details.drinks.get_cocktail_by_name(drinkName)
        # print({currentDrink['steps']})
        if cosmo_details:
            print("\nDetails for Cosmopolitan:")
            print("Description:", cosmo_details['description'])
            print("Steps:", cosmo_details['steps'])
        else:
            print("\nCosmopolitan not found in the configuration. ", drinkName)
        for step in cosmo_details['steps']:
            # ser.write(bytes(step[0] + '\n'))
            command = step[0] + '\n'
            ser.write(command.encode('utf-8'))
            print(command)
            time.sleep(step[1])
            command = step[2] + '\n'
            ser.write(command.encode('utf-8'))
            print(command)

def controlPump(self, pumpNumber, ONorOFF):
    from main import drinks
    pico_port = find_pico_port()
    if pico_port is None:
        print("Raspberry Pi Pico not found. Make sure it is connected.")
        return
    print(f"Raspberry Pi Pico found on port: {pico_port}")
    # Open the serial connection
    with serial.Serial(pico_port, 115200, timeout=1) as ser:
        print("Controlling manually pump!")
        msg = pumpNumber+"-"+ONorOFF
        if (ONorOFF == 'ON'):
            # ser.write(b'P1-ON\n')
            # msg = pumpNumber+"-"+ONorOFF
            # ser.write(b'')
            ser.write(msg.encode('utf-8'))
            print(msg)
            ser.flush()
        elif (ONorOFF == 'OFF'):
            # ser.write(b'P1-OFF\n')
            # print("P1-OFF\n")
            # ser.flush()
            ser.write(msg.encode('utf-8'))
            print(msg)
            ser.flush()
        else:
            return
        
        # cosmo_details = drinks.get_cocktail_by_name(drinkName)
        # for step in cosmo_details['steps']:
        #     # ser.write(bytes(step[0] + '\n'))
        #     command = step[0] + '\n'
        #     ser.write(command.encode('utf-8'))
        #     print(command)
        #     time.sleep(step[1])
        #     command = step[2] + '\n'
        #     ser.write(command.encode('utf-8'))
        #     print(command)

            
def clean_cache():  
    # Remove the contents of the __pycache__ directories
    for root, dirs, files in os.walk(os.path.abspath(".")):
        for dir_name in dirs:
            if dir_name == "__pycache__":
                cache_path = os.path.join(root, dir_name)
                print(f"Cleaning cache folder: {cache_path}")
                try:
                    # Remove the contents of the __pycache__ folder
                    shutil.rmtree(cache_path)
                except OSError as e:
                    print(f"Error cleaning cache folder: {e}")