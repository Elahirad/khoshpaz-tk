from app.view.constants import *

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

from app.view.context import Context


class SideBar(CTkFrame):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__context = Context()
        self.__context.add_callback(self.__switch_ui_mode)

        logo_image_data = Image.open("./app/view/assets/logo.png")
        logo_image = CTkImage(
            dark_image=logo_image_data, light_image=logo_image_data, size=(120, 120)
        )

        CTkLabel(master=self, text="", image=logo_image).pack(
            pady=(15, 0), anchor="center"
        )
        CTkLabel(master=self, text="کترینگ خوش‌پز", font=("B Koodak Bold", 20)).pack(
            anchor="center", pady=(10, 0)
        )

        def switch_event() -> None:
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

        self.__btn1 = CTkButton(
            master=self,
            text="مدیریت سفارش‌ها",
            font=normal_text_font,
            anchor="center",
            command=lambda: self.switch_mode(MANAGE_ORDERS),
        )
        self.__btn2 = CTkButton(
            master=self,
            text="مدیریت بسته‌های اقتصادی",
            font=normal_text_font,
            anchor="center",
            command=lambda: self.switch_mode(MANAGE_ECO_PACKS),
        )
        self.__btn3 = CTkButton(
            master=self,
            text="مدیریت غذاها",
            font=normal_text_font,
            anchor="center",
            command=lambda: self.switch_mode(MANAGE_FOODS),
        )
        self.__btn4 = CTkButton(
            master=self,
            text="مدیریت مواد اولیه",
            font=normal_text_font,
            anchor="center",
            command=lambda: self.switch_mode(MANAGE_INGREDIENTS),
        )
        self.__btn5 = CTkButton(
            master=self,
            text="مدیریت اجزای غذا",
            font=normal_text_font,
            anchor="center",
            command=lambda: self.switch_mode(MANAGE_PARTS),
        )

        self.__btn1.pack(anchor="center", ipady=5, pady=(30, 0))
        self.__btn2.pack(anchor="center", ipady=5, pady=(30, 0))
        self.__btn3.pack(anchor="center", ipady=5, pady=(30, 0))
        self.__btn4.pack(anchor="center", ipady=5, pady=(30, 0))
        self.__btn5.pack(anchor="center", ipady=5, pady=(30, 0))
        self.__switch_ui_mode()

    def switch_mode(self, mode: int) -> None:
        self.__context['mode'] = mode

    def __switch_ui_mode(self) -> None:
        buttons: list[CTkButton] = [self.__btn1, self.__btn2, self.__btn3, self.__btn4, self.__btn5]
        for btn in buttons:
            btn.configure(fg_color=ThemeManager.theme["CTkButton"]["fg_color"])
        mode = self.__context['mode']
        if mode == MANAGE_ORDERS:
            self.__btn1.configure(fg_color=ThemeManager.theme["CTkButton"]["hover_color"])
        if mode == MANAGE_ECO_PACKS:
            self.__btn2.configure(fg_color=ThemeManager.theme["CTkButton"]["hover_color"])
        if mode == MANAGE_FOODS:
            self.__btn3.configure(fg_color=ThemeManager.theme["CTkButton"]["hover_color"])
        if mode == MANAGE_INGREDIENTS:
            self.__btn4.configure(fg_color=ThemeManager.theme["CTkButton"]["hover_color"])
        if mode == MANAGE_PARTS:
            self.__btn5.configure(fg_color=ThemeManager.theme["CTkButton"]["hover_color"])
