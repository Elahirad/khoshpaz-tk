from customtkinter import (
    CTk,
    CTkFrame,
    CTkImage,
    CTkLabel,
    CTkButton,
    StringVar,
    CTkSwitch,
)
from customtkinter import (
    set_appearance_mode,
    set_default_color_theme,
    get_appearance_mode,
    ThemeManager,
)

from PIL import Image

MODE1, MODE2, MODE3 = range(3)


class App(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Geometry
        self.geometry("750x550")
        self.resizable(False, False)

        # Appearance
        set_appearance_mode("system")
        set_default_color_theme("green")
        self.after(200, lambda: self.iconbitmap("./app/logo.ico"))
        self.title("کترینگ خوش‌پز")

        # Side menu
        self.build_side_menu()
        self.switch_mode(MODE1)

    def build_side_menu(self):
        frame = CTkFrame(self, width=170, height=550)

        frame.pack_propagate(0)
        frame.pack(fill="y", anchor="e", side="right")

        logo_image_data = Image.open("./app/logo.png")
        logo_image = CTkImage(
            dark_image=logo_image_data, light_image=logo_image_data, size=(120, 120)
        )

        CTkLabel(master=frame, text="", image=logo_image).pack(
            pady=(15, 0), anchor="center"
        )
        CTkLabel(master=frame, text="کترینگ خوش‌پز", font=("B Koodak Bold", 20)).pack(
            anchor="center", pady=(10, 0)
        )

        def switch_event():
            if switch_var.get() == "on":
                set_appearance_mode("dark")
            else:
                set_appearance_mode("light")

        switch_var = StringVar(value="on" if get_appearance_mode() == "Dark" else "off")
        switch = CTkSwitch(
            frame,
            text="حالت تاریک",
            font=("B Nazanin Bold", 14),
            command=switch_event,
            variable=switch_var,
            onvalue="on",
            offvalue="off",
        )

        switch.pack(pady=(15, 0))

        self.btn1 = CTkButton(
            master=frame,
            text="Button 1",
            anchor="center",
            command=lambda: self.switch_mode(MODE1),
        )
        self.btn2 = CTkButton(
            master=frame,
            text="Button 2",
            anchor="center",
            command=lambda: self.switch_mode(MODE2),
        )
        self.btn3 = CTkButton(
            master=frame,
            text="Button 3",
            anchor="center",
            command=lambda: self.switch_mode(MODE3),
        )

        self.btn1.pack(anchor="center", ipady=5, pady=(30, 0))
        self.btn2.pack(anchor="center", ipady=5, pady=(30, 0))
        self.btn3.pack(anchor="center", ipady=5, pady=(30, 0))

    def switch_mode(self, mode):
        self.mode = mode
        for btn in [self.btn1, self.btn2, self.btn3]:
            btn.configure(fg_color=ThemeManager.theme["CTkButton"]["fg_color"])
        if self.mode == MODE1:
            self.btn1.configure(fg_color=ThemeManager.theme["CTkButton"]["hover_color"])
        if self.mode == MODE2:
            self.btn2.configure(fg_color=ThemeManager.theme["CTkButton"]["hover_color"])
        if self.mode == MODE3:
            self.btn3.configure(fg_color=ThemeManager.theme["CTkButton"]["hover_color"])
