from customtkinter import (
    CTk,
)
from customtkinter import (
    set_appearance_mode,
    set_default_color_theme,
    ThemeManager,
)

from app.constants import *
from app.main_view import MainView
from app.sidebar import SideBar
from app.types import Observer


class App(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.observers: Observer = []

        # Geometry
        self.geometry("850x650")
        self.resizable(False, False)

        # Appearance
        set_appearance_mode("system")
        set_default_color_theme("green")
        self.after(200, lambda: self.iconbitmap("./app/assets/logo.ico"))
        self.title("کترینگ خوش‌پز")

        self.mode = MANAGE_ORDERS

        # Side bar view
        self.sidebar = SideBar(self, self, width=170, height=650)
        self.sidebar.pack_propagate(0)
        self.sidebar.pack(fill="y", anchor="e", side="right")
        self.add_observer(self.sidebar)

        # Main view
        self.main_view = MainView(
            self,
            self,
            width=680,
            height=650,
            fg_color=ThemeManager.theme["CTk"]["fg_color"],
        )
        self.main_view.pack_propagate(0)
        self.main_view.pack(fill="both", anchor="e", side="right")

        self.add_observer(self.main_view)

    def switch_mode(self, new_mode):
        self.mode = new_mode
        self._notify()

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def _notify(self):
        for observer in self.observers:
            observer.update()
