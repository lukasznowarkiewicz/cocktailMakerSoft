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
        
        # Wczytaj dane z pliku JSON
        with open('recipes.json', 'r') as recipes_json:
            recipes_data = json.load(recipes_json)

        # main window - menu, steps during preparation, etc
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid(row=0, column=0, sticky="nesw")

        # Configure rows and columns for equal distribution
        for col in range(6): # 5 columns
            self.home_frame.columnconfigure(col, weight=1)

        for row in range(2): # 2 rows
            self.home_frame.rowconfigure(row, weight=1)

        # Button creation and placement with added padding
        padding_x = 5
        padding_y = 5
        for idx, button_data in enumerate(recipes_data):
            # self.image = customtkinter.CTkImage(Image.open(os.path.join(image_path, button_data["image"])), size=(120, 120))
            label = button_data["label"]
            #image = button_data["image"]
            btn = customtkinter.CTkButton(self.home_frame, text=label, compound="top", font=("arial", 18), border_spacing=10)
            btn.grid(row=idx // 5, column=idx % 5, padx=padding_x, pady=padding_y)


    def toggle_fullscreen(self, event=None):
        is_fullscreen = self.attributes('-fullscreen')
        self.attributes('-fullscreen', not is_fullscreen)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()


    