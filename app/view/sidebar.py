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
        self._context = Context()
        self._context.add_callback(self._switch_ui_mode, 'mode')

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

        self._btn1 = CTkButton(
            master=self,
            text="مدیریت سفارش‌ها",
            font=normal_text_font,
            anchor="center",
            command=lambda: self.switch_mode(MANAGE_ORDERS),
        )
        self._btn2 = CTkButton(
            master=self,
            text="مدیریت غذاها",
            font=normal_text_font,
            anchor="center",
            command=lambda: self.switch_mode(MANAGE_FOODS),
        )
        self._btn3 = CTkButton(
            master=self,
            text="مدیریت مواد اولیه",
            font=normal_text_font,
            anchor="center",
            command=lambda: self.switch_mode(MANAGE_INGREDIENTS),
        )
        self._btn4 = CTkButton(
            master=self,
            text="مدیریت انبار",
            font=normal_text_font,
            anchor="center",
            command=lambda: self.switch_mode(MANAGE_INVENTORY),
        )
        self._btn5 = CTkButton(
            master=self,
            text="مدیریت اجزای غذا",
            font=normal_text_font,
            anchor="center",
            command=lambda: self.switch_mode(MANAGE_PARTS),
        )
        self._btn7 = CTkButton(
            master=self,
            text="مدیریت مشتریان",
            font=normal_text_font,
            anchor="center",
            command=lambda: self.switch_mode(MANAGE_CUSTOMERS),
        )

        self._btn1.pack(anchor="center", ipady=5, pady=(30, 0))
        self._btn2.pack(anchor="center", ipady=5, pady=(30, 0))
        self._btn3.pack(anchor="center", ipady=5, pady=(30, 0))
        self._btn4.pack(anchor="center", ipady=5, pady=(30, 0))
        self._btn5.pack(anchor="center", ipady=5, pady=(30, 0))
        self._btn7.pack(anchor="center", ipady=5, pady=(30, 0))
        self._switch_ui_mode()

    def switch_mode(self, mode: int) -> None:
        self._context['mode'] = mode

    def _switch_ui_mode(self) -> None:
        buttons: list[CTkButton] = [self._btn1, self._btn2, self._btn3, self._btn4, self._btn5,
                                    self._btn7]
        for btn in buttons:
            btn.configure(fg_color=ThemeManager.theme["CTkButton"]["fg_color"])
        mode = self._context['mode']
        if mode == MANAGE_ORDERS:
            self._btn1.configure(fg_color=ThemeManager.theme["CTkButton"]["hover_color"])
        if mode == MANAGE_FOODS:
            self._btn2.configure(fg_color=ThemeManager.theme["CTkButton"]["hover_color"])
        if mode == MANAGE_INGREDIENTS:
            self._btn3.configure(fg_color=ThemeManager.theme["CTkButton"]["hover_color"])
        if mode == MANAGE_INVENTORY:
            self._btn4.configure(fg_color=ThemeManager.theme["CTkButton"]["hover_color"])
        if mode == MANAGE_PARTS:
            self._btn5.configure(fg_color=ThemeManager.theme["CTkButton"]["hover_color"])
        if mode == MANAGE_CUSTOMERS:
            self._btn7.configure(fg_color=ThemeManager.theme["CTkButton"]["hover_color"])
