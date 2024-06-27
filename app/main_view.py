from customtkinter import CTkFrame, ThemeManager
from app.constants import *
from app.pages import (
    ManageIngredients,
    ManageEcoPacks,
    ManageFoods,
    ManageParts,
    ManageOrders,
)
from app.types import Observer, IApp


class MainView(CTkFrame, Observer):

    def __init__(self, app: IApp, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__app: IApp = app

        self.__manage_ingredients = ManageIngredients(
            self, width=680, height=650, fg_color=ThemeManager.theme["CTk"]["fg_color"]
        )
        self.__manage_ingredients.pack_propagate(False)
        self.__manage_parts = ManageParts(
            self, width=680, height=650, fg_color=ThemeManager.theme["CTk"]["fg_color"]
        )
        self.__manage_parts.pack_propagate(False)
        self.__manage_orders = ManageOrders(
            self, width=680, height=650, fg_color=ThemeManager.theme["CTk"]["fg_color"]
        )
        self.__manage_orders.pack_propagate(False)
        self.__manage_eco_packs = ManageEcoPacks(
            self, width=680, height=650, fg_color=ThemeManager.theme["CTk"]["fg_color"]
        )
        self.__manage_eco_packs.pack_propagate(False)
        self.__manage_foods = ManageFoods(
            self, width=680, height=650, fg_color=ThemeManager.theme["CTk"]["fg_color"]
        )
        self.__manage_foods.pack_propagate(False)
        self.__build_view()

    def __build_view(self) -> None:
        frames: list[CTkFrame] = [
            self.__manage_foods,
            self.__manage_eco_packs,
            self.__manage_ingredients,
            self.__manage_parts,
            self.__manage_orders,
        ]
        for frame in frames:
            frame.pack_forget()
        if self.__app.mode == MANAGE_INGREDIENTS:
            self.__manage_ingredients.pack(fill="both", anchor="e", side="right")
        elif self.__app.mode == MANAGE_ECO_PACKS:
            self.__manage_eco_packs.pack(fill="both", anchor="e", side="right")
        elif self.__app.mode == MANAGE_PARTS:
            self.__manage_parts.pack(fill="both", anchor="e", side="right")
        elif self.__app.mode == MANAGE_FOODS:
            self.__manage_foods.pack(fill="both", anchor="e", side="right")
        elif self.__app.mode == MANAGE_ORDERS:
            self.__manage_orders.pack(fill="both", anchor="e", side="right")

    def update(self) -> None:
        self.__build_view()
