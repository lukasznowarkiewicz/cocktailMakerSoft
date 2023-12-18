import customtkinter
import os
import json
from PIL import Image
import functions
import tkinter
from functools import partial

class Details(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.label = customtkinter.CTkLabel(self, text="This is page Details")
        self.label.pack(side="top", fill="x", pady=10)
        # self.label.con
        self.button = customtkinter.CTkButton(self, text="Return to drink choice",
                           command=lambda: controller.show_frame("StartPage"))
        self.button.pack()
        button2 = customtkinter.CTkButton(self, text="Make it!",
                           command=lambda: controller.show_frame("Preparing"))
        button2.pack()
        # self.updateValues(self, "cokolwiek")
    def updateValues(self, drinkName):
        updated_text = f"This is page Details for {drinkName}"
        self.label.configure(text=updated_text)
        print(f"Label updated to: {updated_text}")
    
