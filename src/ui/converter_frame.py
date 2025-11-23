import customtkinter as ctk


class ConverterFrame(ctk.CTkFrame):
    def __init__(self, container, unit_label, converter_func):
        super().__init__(container, corner_radius=12)


        self.unit_label = unit_label
        self.converter_func = converter_func

        #widgets
        self.label = ctk.CTkLabel(self, text=self.unit_label, font=("Segoe UI", 14))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.input_value = ctk.StringVar()
        self.entry = ctk.CTkEntry(self, textvariable=self.input_value, width=140)
        self.entry.grid(row=0, column=1, padx=10, pady=10)
        self.entry.focus()

        self.btn = ctk.CTkButton(self, text = "Convert", command=self.convert)
        self.btn.grid(row=0, column=2, padx=10, pady=10)

        self.result_label = ctk.CTkLabel(self, text="", font=("Segoe UI Semibold", 15))
        self.result_label.grid(row=1, column=0, columnspan=3, pady=15)

    def convert(self):
        try:
            value = float(self.input_value.get())
            result = self.converter_func(value)
            self.result_label.configure(text=result)
        except ValueError:
            self.result_label.configure(text="Error: insert a numeric value")

    def reset(self):
        self.entry.delete(0, "end")
        self.result_label.configure(text="")
    
