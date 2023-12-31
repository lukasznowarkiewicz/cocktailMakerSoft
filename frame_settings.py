import customtkinter
import os
import json
from PIL import Image
import functions
import tkinter
from functools import partial

class Settings(customtkinter.CTkFrame):

    def create_pump_buttons(self, pump_id):
        on_button = customtkinter.CTkButton(self, text=f"{pump_id} - ON", compound="top", font=("arial", 18), border_spacing=10, command=lambda: functions.controlPump(self, pump_id, "ON"))
        on_button.pack(side="top", pady=10)
        off_button = customtkinter.CTkButton(self, text=f"{pump_id} - OFF", compound="top", font=("arial", 18), border_spacing=10, command=lambda: functions.controlPump(self, pump_id, "OFF"))
        off_button.pack(side="bottom", pady=10)

    def create_all_pump_buttons(self):
        pump_ids = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]

        for pump_id in pump_ids:
            self.create_pump_buttons(pump_id)

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = customtkinter.CTkLabel(self, text="Device settings")
        label.pack(side="top", fill="x", pady=10)
        button = customtkinter.CTkButton(self, text="Return to start screen",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        self.create_all_pump_buttons()
        # onButton = customtkinter.CTkButton(self, text="P1 - ON", compound="top", font=("arial", 18), border_spacing=10, command=lambda: functions.controlPump(self, "P1", "ON") )
        # onButton.pack(side="left", pady=10)
        # offButton = customtkinter.CTkButton(self, text="P1 - OFF", compound="top", font=("arial", 18), border_spacing=10, command=lambda: functions.controlPump(self, "P1", "OFF") )
        # offButton.pack(side="left", pady=10)




    