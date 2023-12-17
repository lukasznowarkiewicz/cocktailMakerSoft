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
    