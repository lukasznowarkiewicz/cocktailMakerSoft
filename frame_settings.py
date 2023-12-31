import customtkinter
import os
import json
from PIL import Image
import functions
import tkinter
from functools import partial

class Settings(customtkinter.CTkFrame):

    def create_pump_buttons(self, pump_id):
        self.bottomFrame = customtkinter.CTkFrame(master=self, width=1200, height=100, fg_color="transparent", border_color="white")
        self.bottomFrame.pack(pady=2,padx=2, side="top")
        on_button = customtkinter.CTkButton(self.bottomFrame, text=f"{pump_id} - ON", compound="top", font=("arial", 18), border_spacing=10, command=lambda: functions.controlPump(self, pump_id, "ON"))
        on_button.pack(side="left", pady=5, padx=5)
        off_button = customtkinter.CTkButton(self.bottomFrame, text=f"{pump_id} - OFF", compound="top", font=("arial", 18), border_spacing=10, command=lambda: functions.controlPump(self, pump_id, "OFF"))
        off_button.pack(side="right", pady=5, padx=5)

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



    