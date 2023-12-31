import customtkinter
import os
import json
from PIL import Image
import functions
import tkinter
from functools import partial

class Settings(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = customtkinter.CTkLabel(self, text="Device settings")
        label.pack(side="top", fill="x", pady=10)
        button = customtkinter.CTkButton(self, text="Return to start screen",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        onButton = customtkinter.CTkButton(self, fg_color="blue", text="P1 - ON", compound="top", font=("arial", 18), border_spacing=10, command=lambda: functions.controlPump(self, "P1", "ON") )
        offButton = customtkinter.CTkButton(self, fg_color="blue", text="P1 - OFF", compound="top", font=("arial", 18), border_spacing=10, command=lambda: functions.controlPump(self, "P1", "OFF") )
        onButton.pack()
        offButton.pack()
    