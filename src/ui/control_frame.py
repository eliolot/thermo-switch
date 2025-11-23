import customtkinter as ctk
from .converter_frame import ConverterFrame
from logic.converter import TemperatureConverter


class ControlFrame(ctk.CTkFrame):
    def __init__(self, container):
        super().__init__(container, corner_radius=12, fg_color="transparent")

        self.selected_mode = ctk.IntVar(value=0)

        self.radio_f2c = ctk.CTkRadioButton(
            self, text="°F -> °C", variable=self.selected_mode, value = 0, command=self.change_frame
        )
        self.radio_f2c.grid(row=0, column =0, padx=10, pady=10)

        self.radio_c2f = ctk.CTkRadioButton(
            self, text="°C -> °F", variable=self.selected_mode, value = 1, command=self.change_frame
        )
        self.radio_c2f.grid(row=0, column=1, padx=10, pady=10)


        #create subframes
        self.frames = {
            0: ConverterFrame(container, "Fahrenheit", TemperatureConverter.fahrenheit_to_celsius),
            1: ConverterFrame(container, "Celsius", TemperatureConverter.celsius_to_fahrenheit)
        }
        self.change_frame()


    def change_frame(self):
        frame = self.frames[self.selected_mode.get()]
        frame.reset()
        frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        frame.tkraise()

