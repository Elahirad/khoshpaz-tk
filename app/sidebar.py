from app.constants import *


from PIL import Image
from customtkinter import (
    CTkButton,
    CTkFrame,
    CTkImage,
    CTkLabel,
    CTkSwitch,
    StringVar,
    ThemeManager,
    get_appearance_mode,
    set_appearance_mode,
)

from app.types import Observer


class SideBar(CTkFrame, Observer):

    def __init__(self, master: CTkFrame, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master = master
        logo_image_data = Image.open("./app/assets/logo.png")
        logo_image = CTkImage(
            dark_image=logo_image_data, light_image=logo_image_data, size=(120, 120)
        )

        CTkLabel(master=self, text="", image=logo_image).pack(
            pady=(15, 0), anchor="center"
        )
        CTkLabel(master=self, text="کترینگ خوش‌پز", font=("B Koodak Bold", 20)).pack(
            anchor="center", pady=(10, 0)
        )

        def switch_event():
            if switch_var.get() == "on":
                set_appearance_mode("dark")
            else:
                set_appearance_mode("light")

        switch_var = StringVar(value="on" if get_appearance_mode() == "Dark" else "off")
        switch = CTkSwitch(
            self,
            text="حالت تاریک",
            font=normal_text_font,
            command=switch_event,
            variable=switch_var,
            onvalue="on",
            offvalue="off",
        )

        switch.pack(pady=(15, 0))

        self.btn1 = CTkButton(
            master=self,
            text="مدیریت سفارش‌ها",
            font=normal_text_font,
            anchor="center",
            command=lambda: self.master.switch_mode(MANAGE_ORDERS),
        )
        self.btn2 = CTkButton(
            master=self,
            text="مدیریت بسته‌های اقتصادی",
            font=normal_text_font,
            anchor="center",
            command=lambda: self.master.switch_mode(MANAGE_ECO_PACKS),
        )
        self.btn3 = CTkButton(
            master=self,
            text="مدیریت غذاها",
            font=normal_text_font,
            anchor="center",
            command=lambda: self.master.switch_mode(MANAGE_FOODS),
        )
        self.btn4 = CTkButton(
            master=self,
            text="مدیریت مواد اولیه",
            font=normal_text_font,
            anchor="center",
            command=lambda: self.master.switch_mode(MANAGE_INGREDIENTS),
        )
        self.btn5 = CTkButton(
            master=self,
            text="مدیریت اجزای غذا",
            font=normal_text_font,
            anchor="center",
            command=lambda: self.master.switch_mode(MANAGE_PARTS),
        )

        self.btn1.pack(anchor="center", ipady=5, pady=(30, 0))
        self.btn2.pack(anchor="center", ipady=5, pady=(30, 0))
        self.btn3.pack(anchor="center", ipady=5, pady=(30, 0))
        self.btn4.pack(anchor="center", ipady=5, pady=(30, 0))
        self.btn5.pack(anchor="center", ipady=5, pady=(30, 0))
        self.switch_mode()

    def switch_mode(self):
        for btn in [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5]:
            btn.configure(fg_color=ThemeManager.theme["CTkButton"]["fg_color"])
        if self.master.mode == MANAGE_ORDERS:
            self.btn1.configure(fg_color=ThemeManager.theme["CTkButton"]["hover_color"])
        if self.master.mode == MANAGE_ECO_PACKS:
            self.btn2.configure(fg_color=ThemeManager.theme["CTkButton"]["hover_color"])
        if self.master.mode == MANAGE_FOODS:
            self.btn3.configure(fg_color=ThemeManager.theme["CTkButton"]["hover_color"])
        if self.master.mode == MANAGE_INGREDIENTS:
            self.btn4.configure(fg_color=ThemeManager.theme["CTkButton"]["hover_color"])
        if self.master.mode == MANAGE_PARTS:
            self.btn5.configure(fg_color=ThemeManager.theme["CTkButton"]["hover_color"])

    def update(self):
        self.switch_mode()
