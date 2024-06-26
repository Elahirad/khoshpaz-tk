from customtkinter import CTkFrame, ThemeManager
from app.constants import *
from app.pages import (
    ManageIngredients,
    ManageEcoPacks,
    ManageFoods,
    ManageParts,
    ManageOrders,
)
from app.types import Observer


class MainView(CTkFrame, Observer):

    def __init__(self, master: CTkFrame, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master = master

        self.manage_ingredients = ManageIngredients(
            self, width=680, height=650, fg_color=ThemeManager.theme["CTk"]["fg_color"]
        )
        self.manage_ingredients.pack_propagate(0)
        self.manage_parts = ManageParts(
            self, width=680, height=650, fg_color=ThemeManager.theme["CTk"]["fg_color"]
        )
        self.manage_parts.pack_propagate(0)
        self.manage_orders = ManageOrders(
            self, width=680, height=650, fg_color=ThemeManager.theme["CTk"]["fg_color"]
        )
        self.manage_orders.pack_propagate(0)
        self.manage_eco_packs = ManageEcoPacks(
            self, width=680, height=650, fg_color=ThemeManager.theme["CTk"]["fg_color"]
        )
        self.manage_eco_packs.pack_propagate(0)
        self.manage_foods = ManageFoods(
            self, width=680, height=650, fg_color=ThemeManager.theme["CTk"]["fg_color"]
        )
        self.manage_foods.pack_propagate(0)
        self.build_view()

    def build_view(self):
        frames: list[CTkFrame] = [
            self.manage_foods,
            self.manage_eco_packs,
            self.manage_ingredients,
            self.manage_parts,
            self.manage_orders,
        ]
        for frame in frames:
            frame.pack_forget()
        if self.master.mode == MANAGE_INGREDIENTS:
            self.manage_ingredients.pack(fill="both", anchor="e", side="right")
        elif self.master.mode == MANAGE_ECO_PACKS:
            self.manage_eco_packs.pack(fill="both", anchor="e", side="right")
        elif self.master.mode == MANAGE_PARTS:
            self.manage_parts.pack(fill="both", anchor="e", side="right")
        elif self.master.mode == MANAGE_FOODS:
            self.manage_foods.pack(fill="both", anchor="e", side="right")
        elif self.master.mode == MANAGE_ORDERS:
            self.manage_orders.pack(fill="both", anchor="e", side="right")

    def update(self):
        self.build_view()
