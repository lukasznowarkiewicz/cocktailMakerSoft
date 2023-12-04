import customtkinter
import os
import json
from PIL import Image
import functions



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title(f"cocktailMakerDashboard.py commit-hash: {functions.get_commit_hash(self)}")
        self.geometry("1024x600")
        self.bind("<Escape>", self.toggle_fullscreen)
        customtkinter.set_appearance_mode("Dark")
        print(functions.print_debug_info(self))
        

    def toggle_fullscreen(self, event=None):
        is_fullscreen = self.attributes('-fullscreen')
        self.attributes('-fullscreen', not is_fullscreen)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()


    