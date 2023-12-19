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
        self.grid_rowconfigure(9, weight=10)
        self.grid_columnconfigure(5, weight=1)



        # json data import of the recipes
        with open('recipes.json', 'r') as recipes_json:
            recipes_data = json.load(recipes_json)

        button_array = []
        label = []
        # Button creation and placement with added padding
        for idx, button_data in enumerate(recipes_data):
            # self.image = customtkinter.CTkImage(Image.open(os.path.join(image_path, button_data["image"])), size=(120, 120))
            label.append(button_data["label"])
            print(f"Label {label[idx]}")
            #image = button_data["image"]
            # btn = customtkinter.CTkButton(self, text=label, compound="top", font=("arial", 18), border_spacing=10, command=lambda: controller.show_frame("Details", btn._text))
            button_array.append(customtkinter.CTkButton(self, text=label[idx], compound="top", font=("arial", 18), border_spacing=10, command=lambda l=label[idx]:  controller.show_frame("Details", l)))
            button_array[idx].grid(row=idx // 5, column=idx % 5, padx=5, pady=5)
            button_array[idx].configure(height = 260, width = 192)
            

        button3 = customtkinter.CTkButton(self, text="Settings",
                            command=lambda: controller.show_frame("Settings"))
        button3.grid(sticky="nsew", row=3, column=4)
        # button3.configure(height=50, width=50)