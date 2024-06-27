from customtkinter import (
    set_appearance_mode,
    set_default_color_theme,
    ThemeManager,
)

from app.constants import *
from app.main_view import MainView
from app.sidebar import SideBar
from app.types import Observer, IApp


class App(IApp):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__observers: list[Observer] = []

        # Geometry
        self.geometry("850x650")
        self.resizable(False, False)

        # Appearance
        set_appearance_mode("system")
        set_default_color_theme("green")
        self.after(200, lambda: self.iconbitmap("./app/assets/logo.ico"))
        self.title("کترینگ خوش‌پز")

        self.mode = MANAGE_ORDERS

        # Sidebar view
        self.__sidebar = SideBar(self, self, width=170, height=650)
        self.__sidebar.pack_propagate(False)
        self.__sidebar.pack(fill="y", anchor="e", side="right")
        self.__add_observer(self.__sidebar)

        # Main view
        self.__main_view = MainView(
            self,
            self,
            width=680,
            height=650,
            fg_color=ThemeManager.theme["CTk"]["fg_color"],
        )
        self.__main_view.pack_propagate(False)
        self.__main_view.pack(fill="both", anchor="e", side="right")
        self.__add_observer(self.__main_view)

    def switch_mode(self, new_mode: int) -> None:
        self.mode = new_mode
        self.__notify()

    def __add_observer(self, observer: Observer) -> None:
        self.__observers.append(observer)

    def __remove_observer(self, observer: Observer) -> None:
        self.__observers.remove(observer)

    def __notify(self) -> None:
        for observer in self.__observers:
            observer.update()
