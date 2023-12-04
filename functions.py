import subprocess
import platform
import sys

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
