import customtkinter
import os
import json
from PIL import Image
import functions
import tkinter
from functools import partial
import time
import main


class Preparing(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.currentDrink = "None"

        topFrame = customtkinter.CTkFrame(master=self, width=1024, height=600, fg_color="transparent", border_color="white")
        topFrame.pack(pady=50,padx=50, side="top")
        self.my_image = customtkinter.CTkImage(light_image=Image.open("drinks/alafrench.PNG"),
                                  dark_image=Image.open("drinks/alafrench.PNG"),
                                  size=(300, 300))

        self.image_label = customtkinter.CTkLabel(topFrame, image=self.my_image, text="")  # display image with a CTkLabel
        self.image_label.pack(side="right", fill="x", pady=10)

        # bottom frame with buttons
        bottomFrame = customtkinter.CTkFrame(master=self, width=1200, height=200, fg_color="transparent", border_color="white")
        bottomFrame.pack(pady=50,padx=50, side="bottom")
        self.button = customtkinter.CTkButton(bottomFrame, font=("lato", 22), text="Return to start screen", width=400, height=60, 
                           command=lambda: controller.show_frame("StartPage"))
        
        self.button.pack(side="left", pady=10)
        self.button2 = customtkinter.CTkButton(bottomFrame, font=("lato", 22), text="Start",  width=400, height=60, 
                           command=lambda: functions.prepare_drink(self, self.currentDrink))
        self.button2.pack(side="right", pady=10)
        
        self.labelSpacer = customtkinter.CTkLabel(bottomFrame, text="            ")
        self.labelSpacer.pack(side="bottom", fill="x", pady=10)

    def updateValues(self, drinkName):
        imagePath=(main.drinks.get_cocktail_by_name(drinkName))['image']
        self.my_image.configure(light_image=Image.open("drinks/"+imagePath))
        self.my_image.configure(dark_image=Image.open("drinks/"+imagePath))

        
