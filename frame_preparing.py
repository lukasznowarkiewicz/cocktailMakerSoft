import customtkinter
import os
import json
from PIL import Image
import functions
import tkinter
from functools import partial
import time

class Preparing(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = customtkinter.CTkLabel(self, text="Starting preparation of your drink")
        label.pack(side="top", fill="x", pady=10)
        button = customtkinter.CTkButton(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(side="top", fill="x", pady=20)

        
        button2 = customtkinter.CTkButton(self, text="Prepare",
                           command=lambda: functions.prepare_drink(self))
        button2.pack(side="top", fill="x", pady=20)

        
