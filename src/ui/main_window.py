import customtkinter as ctk
from .control_frame import ControlFrame



class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Thermo-Converter")
        self.geometry("430x200")
        self.resizable(False, False)

        #global theme
        ctk.set_appearance_mode("dark") # light / dark / system
        ctk.set_default_color_theme("blue") # blue, green, dark-blue

        self.columnconfigure(0, weight=1)

        ControlFrame(self).grid(row=0, column=0, pady=10)

        
