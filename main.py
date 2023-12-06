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

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        # self.num_of_frames = 0
        self.title(f"cocktailMakerDashboard.py commit-hash: {functions.get_commit_hash(self)}")
        self.geometry("1024x600")
        self.bind("<Escape>", self.toggle_fullscreen)
        customtkinter.set_appearance_mode("Dark")
        print(functions.print_debug_info(self))
        
        # json data import of the recipes
        with open('recipes.json', 'r') as recipes_json:
            recipes_data = json.load(recipes_json)

        container = customtkinter.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (frame_start.StartPage, frame_details.Details, frame_preparing.Preparing):
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
    
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        

        


if __name__ == "__main__":
    app = App()
    app.mainloop()


    