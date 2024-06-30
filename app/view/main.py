from typing import Optional

from customtkinter import (
    set_appearance_mode,
    set_default_color_theme,
    CTk
)

from CTkMessagebox import CTkMessagebox

from app.view.constants import *
from app.view.main_view import MainView
from app.view.sidebar import SideBar
from .context import Context

from app.view.interface import IView

from app.controller import Controller


class AppView(CTk, IView):

    def __init__(self, controller: Optional[Controller], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.controller = controller
        self.__main_view = None
        self.__sidebar = None
        self.__context = Context()
        self.__context['mode'] = MANAGE_ORDERS
        self.__context['ingredients'] = []
        self.__context['parts'] = []
        self.__context['customers'] = []
        self.__context['foods'] = []
        self.__context['orders'] = []
        self.__context['inventory'] = []
        # Geometry
        self.geometry("950x700")
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
        self.__sidebar = SideBar(self, width=170, height=self.winfo_height())
        self.__sidebar.pack_propagate(False)
        self.__sidebar.pack(fill="y", anchor="e", side="right")

        # Main view
        self.__main_view = MainView(
            self,
            width=self.winfo_width() - 170,
            height=self.winfo_height(),
            fg_color='transparent',
        )
        self.__main_view.pack_propagate(False)
        self.__main_view.pack(fill="both", anchor="e", side="right")

    def show_message(self, title, message, icon='info'):
        self.after(100,
                   lambda: CTkMessagebox(master=self, title=title, message=message, icon=icon, font=normal_text_font))

    def reload_app_data(self):
        if self.__context.controller is None:
            self.__context.controller = self.controller
        ingredients = self.controller.get_ingredients()
        parts = self.controller.get_parts()
        customers = self.controller.get_customers()
        foods = self.controller.get_foods()
        orders = self.controller.get_orders()
        inventory = self.controller.get_inventory_items()
        self.__context.bulk_update(
            {'ingredients': ingredients, 'parts': parts, 'customers': customers, 'foods': foods, 'orders': orders,
             'inventory': inventory})
