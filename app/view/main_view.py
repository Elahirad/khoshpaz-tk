from customtkinter import CTkFrame
from app.view.constants import *
from app.view.pages import (
    ManageIngredients,
    ManageParts,
    ManageOrders,
    ManageFoods,
    ManageCustomers,
    ManageInventory
)

from app.view.context import Context


class MainView(CTkFrame):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._context = Context()
        self._context.add_callback(self._build_view, 'mode')

        self._manage_ingredients = ManageIngredients(
            self, width=self.winfo_width(), height=self.winfo_height(), fg_color='transparent'
        )
        self._manage_inventory = ManageInventory(
            self, width=self.winfo_width(), height=self.winfo_height(), fg_color='transparent'
        )
        self._manage_parts = ManageParts(
            self, width=self.winfo_width(), height=self.winfo_height(), fg_color='transparent'
        )
        self._manage_orders = ManageOrders(
            self, width=self.winfo_width(), height=self.winfo_height(), fg_color='transparent'
        )
        self._manage_foods = ManageFoods(
            self, width=self.winfo_width(), height=self.winfo_height(), fg_color='transparent'
        )
        self._manage_customers = ManageCustomers(
            self, width=self.winfo_width(), height=self.winfo_height(), fg_color='transparent'
        )

        self._build_view()

    def _build_view(self) -> None:
        frames: list[CTkFrame] = [
            self._manage_foods,
            self._manage_ingredients,
            self._manage_inventory,
            self._manage_customers,
            self._manage_parts,
            self._manage_orders,
        ]
        for frame in frames:
            frame.pack_forget()
        mode = self._context['mode']
        if mode == MANAGE_INGREDIENTS:
            self._manage_ingredients.pack(fill="both", anchor="e", expand=True)
        if mode == MANAGE_INVENTORY:
            self._manage_inventory.pack(fill="both", anchor="e", expand=True)
        elif mode == MANAGE_PARTS:
            self._manage_parts.pack(fill="both", anchor="e", expand=True)
        elif mode == MANAGE_FOODS:
            self._manage_foods.pack(fill="both", anchor="e", expand=True)
        elif mode == MANAGE_ORDERS:
            self._manage_orders.pack(fill="both", anchor="e", expand=True)
        elif mode == MANAGE_CUSTOMERS:
            self._manage_customers.pack(fill="both", anchor="e", expand=True)
