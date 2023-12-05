import customtkinter
import os
import json
from PIL import Image
import functions
import tkinter
from functools import partial



class StartPage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.configure(self, width=1020, height=580, corner_radius=0, fg_color="transparent")
        label = customtkinter.CTkLabel(self, text="This is the start page")
        # label.pack(side="top", fill="x", pady=10)
        self.grid(row=0, column=0, sticky="nesw")

        button1 = customtkinter.CTkButton(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = customtkinter.CTkButton(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        
        button1.grid(row=0, column=0)
        button2.grid(row=0, column=0)
        # button1.pack()
        # button2.pack()

        # json data import of the recipes
        with open('recipes.json', 'r') as recipes_json:
            recipes_data = json.load(recipes_json)

        # Button creation and placement with added padding
        for idx, button_data in enumerate(recipes_data):
            # self.image = customtkinter.CTkImage(Image.open(os.path.join(image_path, button_data["image"])), size=(120, 120))
            label = button_data["label"]
            #image = button_data["image"]
            btn = customtkinter.CTkButton(self, text=label, compound="top", font=("arial", 18), border_spacing=10, command=lambda: controller.show_frame("Details"))
            btn.grid(row=idx // 5, column=idx % 5, padx=5, pady=5)
            btn.configure(height = 120, width = 192)