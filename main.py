import customtkinter
import os
import json
from PIL import Image
import functions
import tkinter
from functools import partial
import frame_start
import frame_details
import frame_preparing
import frame_settings
import json

class Drinks:
    def __init__(self, config_file):
        self.config_file = config_file
        self.cocktails = self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, 'r') as file:
                config_data = json.load(file)
                return config_data
        except FileNotFoundError:
            print(f"Error: Config file '{self.config_file}' not found.")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in config file: {e}")
            return None

    def get_cocktail_names(self):
        return [cocktail['label'] for cocktail in self.cocktails] if self.cocktails else []

    def get_cocktail_by_name(self, cocktail_name):
        for cocktail in self.cocktails:
            if cocktail['label'] == cocktail_name:
                return cocktail
        return None


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        # self.num_of_frames = 0
        self.title(f"cocktailMakerDashboard.py commit-hash: {functions.get_commit_hash(self)}")
        self.geometry("1024x600")
        self.bind("<Escape>", self.toggle_fullscreen)
        customtkinter.set_appearance_mode("Dark")
        print(functions.print_debug_info(self))
        
        # Importing drinks and recipes
        drinks = Drinks('recipes.json')

        # Get the names of available cocktails
        cocktail_names = drinks.get_cocktail_names()
        print("Available cocktails:", cocktail_names)

        # Get details for a specific cocktail (e.g., Cosmopolitan)
        cosmo_details = drinks.get_cocktail_by_name('Cosmopolitan')
        if cosmo_details:
            print("\nDetails for Cosmopolitan:")
            print("Description:", cosmo_details['description'])
            print("Steps:", cosmo_details['steps'])
        else:
            print("\nCosmopolitan not found in the configuration.")

        

        container = customtkinter.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (frame_start.StartPage, frame_details.Details, frame_preparing.Preparing, frame_settings.Settings):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")


    def toggle_fullscreen(self, event=None):
        is_fullscreen = self.attributes('-fullscreen')
        self.attributes('-fullscreen', not is_fullscreen)
    
    def show_frame(self, page_name, argument='none'):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        if (page_name=="Details"):
            self.frames[page_name].updateValues(argument)
        frame.tkraise()
        
        

        


if __name__ == "__main__":
    app = App()
    app.mainloop()


    