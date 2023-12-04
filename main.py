import customtkinter
import os
import json
from PIL import Image
import functions
import tkinter
from functools import partial


class App(customtkinter.CTk):

    frames = {}
    current = None

    def __init__(self):
        super().__init__()
        self.num_of_frames = 0
        self.title(f"cocktailMakerDashboard.py commit-hash: {functions.get_commit_hash(self)}")
        self.geometry("1024x600")
        self.bind("<Escape>", self.toggle_fullscreen)
        customtkinter.set_appearance_mode("Dark")
        print(functions.print_debug_info(self))
        
        # json data import of the recipes
        with open('recipes.json', 'r') as recipes_json:
            recipes_data = json.load(recipes_json)

        # root!
        self.main_container = customtkinter.CTkFrame(self, corner_radius=8, fg_color="transparent")
        self.main_container.pack(fill=tkinter.BOTH, expand=True, padx=8, pady=8)

        # home frame - showing options
        self.home_frame = customtkinter.CTkFrame(self.main_container, width=1020, height=580, corner_radius=0, fg_color="transparent")
        self.home_frame.grid(row=0, column=0, sticky="nesw")

        self.preparing_frame = customtkinter.CTkFrame(self.main_container, corner_radius=0, fg_color="transparent")

        # Button creation and placement with added padding
        for idx, button_data in enumerate(recipes_data):
            # self.image = customtkinter.CTkImage(Image.open(os.path.join(image_path, button_data["image"])), size=(120, 120))
            label = button_data["label"]
            #image = button_data["image"]
            btn = customtkinter.CTkButton(self.home_frame, text=label, compound="top", font=("arial", 18), border_spacing=10)
            btn.grid(row=idx // 5, column=idx % 5, padx=5, pady=5)
            btn.configure(height = 120, width = 192)
            btn.configure(command =  partial( self.toggle_frame_by_id,  "frame_" + str(self.num_of_frames + 1) ) )
            self.num_of_frames = self.num_of_frames + 1
            self.create_frame(f"frame_{self.num_of_frames}", 'blue')
            # self.create_nav(main_container, "label","blue")


        
        # button to select the correct frame
    def frame_selector_bt(self, parent, frame_id):
        
        # create frame 
        bt_frame = customtkinter.CTkButton(parent)
        # style frame
        bt_frame.configure(height = 40)
        # creates a text label
        bt_frame.configure(text = "cos" )
        bt_frame.configure(command =  partial( self.toggle_frame_by_id,  "frame" + str(self.num_of_frames + 1) ) )
        # set layout
        bt_frame.grid(pady = 3, row=self.num_of_frames, column=0)
        # update state
        self.num_of_frames = self.num_of_frames + 1

    # create the frame
    def create_frame(self, frame_id, color):
        App.frames[frame_id] = customtkinter.CTkFrame(self)
        App.frames[frame_id].configure(corner_radius = 8)
        App.frames[frame_id].configure(fg_color = color)
        App.frames[frame_id].configure(border_width = 2)
        App.frames[frame_id].configure(border_color = "#323232")
        App.frames[frame_id].padx = 8

        bt_from_frame1 = customtkinter.CTkButton(App.frames[frame_id], text="Test "+ "blue" , command=lambda:print("test " + color) )
        bt_from_frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    # method to change frames
    def toggle_frame_by_id(self, frame_id):
        
        if App.frames[frame_id] is not None:
            if App.current is App.frames[frame_id]:
                App.current.pack_forget()
                App.current = None
            elif App.current is not None:
                App.current.pack_forget()
                App.current = App.frames[frame_id]
                App.current.pack(in_=self.preparing_frame, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
            else:
                App.current = App.frames[frame_id]
                App.current.pack(in_=self.preparing_frame, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    # method to create a pair button selector and its related frame
    def create_nav(self, parent, frame_id, frame_color):
        self.frame_selector_bt(parent, frame_id)
        self.create_frame(frame_id, frame_color)

    def toggle_fullscreen(self, event=None):
        is_fullscreen = self.attributes('-fullscreen')
        self.attributes('-fullscreen', not is_fullscreen)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()


    