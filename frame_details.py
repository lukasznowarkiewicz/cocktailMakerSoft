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
        self.grid_rowconfigure(2, weight=1)  # configure grid system
        self.grid_columnconfigure(2, weight=1)
        self.controller = controller
        self.label = customtkinter.CTkLabel(self, text="This is page Details")
        self.label.pack(side="top", fill="x", pady=10)


        bottomFrame = customtkinter.CTkFrame(master=self, width=1200, height=200, fg_color="transparent", border_color="white")
        bottomFrame.pack(pady=50,padx=50, side="bottom")
        # self.label.con
        self.button = customtkinter.CTkButton(bottomFrame, text="Return to drink choice", width=400, height=60, 
                           command=lambda: controller.show_frame("StartPage"))
        # self.button.grid(sticky="nsew", row=1, column=4)
        self.button.pack(side="left", pady=10)
        self.button2 = customtkinter.CTkButton(bottomFrame, text="Make it!",  width=400, height=60, 
                           command=lambda: controller.show_frame("Preparing"))
        self.button2.pack(side="right", pady=10)
        # self.updateValues(self, "cokolwiek")
    def updateValues(self, drinkName):
        updated_text = f"This is page Details for {drinkName}"
        self.label.configure(text=updated_text)
        print(f"Label updated to: {updated_text}")
    
