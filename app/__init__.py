from customtkinter import CTk, set_appearance_mode, set_default_color_theme


class App(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Geometry
        self.geometry("750x550")
        self.resizable(False, False)

        # Appearance
        set_appearance_mode("dark")
        set_default_color_theme("green")
