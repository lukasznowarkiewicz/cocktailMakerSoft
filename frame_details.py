import customtkinter
import os
import json
from PIL import Image
import functions
import tkinter
from functools import partial
from main import drinks

class Details(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        # top frame with description and photo
        topFrame = customtkinter.CTkFrame(master=self, width=1024, height=600, fg_color="transparent", border_color="white")
        topFrame.pack(pady=50,padx=50, side="top")
        self.label = customtkinter.CTkLabel(topFrame, text="This is page Details. It should be updated while choosing drink. If you are seeing this text, something malfunction.", compound="top", wraplength=400)
        self.label.pack(side="left", fill="x", pady=50,padx=50)


        self.my_image = customtkinter.CTkImage(light_image=Image.open("cocktail.png"),
                                  dark_image=Image.open("cocktail.png"),
                                  size=(300, 300))

        self.image_label = customtkinter.CTkLabel(topFrame, image=self.my_image, text="")  # display image with a CTkLabel
        self.image_label.pack(side="right", fill="x", pady=10)
    

        # bottom frame with buttons
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
        
        self.labelSpacer = customtkinter.CTkLabel(bottomFrame, text="            ")
        self.labelSpacer.pack(side="bottom", fill="x", pady=10)


    def updateValues(self, drinkName):
        updated_text = (drinks.get_cocktail_by_name(drinkName))['description']
        self.label.configure(text=updated_text)
        print(f"Label description updated to: {updated_text}")
    
