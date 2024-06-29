from customtkinter import (
    set_appearance_mode,
    set_default_color_theme,
    ThemeManager, CTk,
)

from app.view.constants import *
from app.view.main_view import MainView
from app.view.sidebar import SideBar
from .context import Context


class AppView(CTk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__main_view = None
        self.__sidebar = None
        self.__context = Context()
        self.__context['mode'] = MANAGE_ORDERS
        fake_gredients = [
            {"id": 1, "نام": "شکر", "واحد": "کیلو"},
            {"id": 2, "نام": "روغن", "واحد": "کیلو"},
            {"id": 3, "نام": "آرد", "واحد": "کیلو"},
        ]
        self.__context['ingredients'] = fake_gredients
        # Geometry
        self.geometry("850x650")
        self.resizable(False, False)

        # Appearance
        set_appearance_mode("system")
        set_default_color_theme("green")
        self.after(200, lambda: self.iconbitmap("./app/view/assets/logo.ico"))
        self.title("کترینگ خوش‌پز")

        self.__build_view()

    def __build_view(self):
        for child in self.winfo_children():
            child.destroy()

        # Sidebar view
        self.__sidebar = SideBar(self, width=170, height=650)
        self.__sidebar.pack_propagate(False)
        self.__sidebar.pack(fill="y", anchor="e", side="right")

        # Main view
        self.__main_view = MainView(
            self,
            width=680,
            height=650,
            fg_color=ThemeManager.theme["CTk"]["fg_color"],
        )
        self.__main_view.pack_propagate(False)
        self.__main_view.pack(fill="both", anchor="e", side="right")
