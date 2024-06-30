from typing import Callable

from customtkinter import CTkLabel, CTkButton, CTkEntry, CTkToplevel, StringVar, CTkComboBox, CTkFrame

from tkinter import Spinbox

from app.view.constants import normal_text_font
from app.view.context import Context


class PartUpdateForm(CTkToplevel):
    def __init__(self, current_values: dict, callback: Callable, master=None, *args, **kwargs) -> None:
        super().__init__(master=master, *args, **kwargs)
        self.geometry("400x600")
        self.resizable(False, False)

        self.__current_values = current_values

        self.__context = Context()

        self.__callback = callback
        CTkLabel(
            master=self, text="افزودن جزء غذا", font=("B Koodak Bold", 25)
        ).pack(fill="x", anchor="center", pady=10)

        CTkLabel(self, text="نام", font=normal_text_font).pack()
        self.__name_entry = CTkEntry(self, font=normal_text_font)
        self.__name_entry.pack()
        self.__name_entry.insert(0, current_values['name'])

        self.__all_ingredients = [item for item in self.__context['ingredients']]
        self.__selected_ingredients = current_values['ingredients_raw']

        self.__combobox_var = StringVar(value=self.__all_ingredients[0]['name'])

        self._select_frame = CTkFrame(self, fg_color='transparent')
        self._select_frame.pack(pady=15)

        self.__combobox = CTkComboBox(master=self._select_frame,
                                      values=list(map(lambda x: x['name'], self.__all_ingredients)),
                                      font=normal_text_font,
                                      variable=self.__combobox_var)
        self.__combobox._dropdown_menu.config(font=normal_text_font)
        self.__combobox.grid(column=2, row=0)

        self.__amount_spinbox = Spinbox(self._select_frame, from_=0, to=100, increment=0.1, width=5)
        self.__amount_spinbox.grid(column=1, row=0)
        CTkButton(self._select_frame, text="افزودن", font=normal_text_font,
                  command=self.__add_ingredient).grid(column=0, row=0)

        self.__selected_ingredients_frame = CTkFrame(self, fg_color='transparent')
        self.__selected_ingredients_frame.pack(fill='both', expand=True)
        self.__show_selected_ingredients()

    def __add_ingredient(self) -> None:
        self.__selected_ingredients[self.__combobox_var.get()] = self.__amount_spinbox.get()
        self.__show_selected_ingredients()

    def __show_selected_ingredients(self):
        def delete_item_from_selected(item_name):
            del self.__selected_ingredients[item_name]
            self.__show_selected_ingredients()

        for child in self.__selected_ingredients_frame.winfo_children():
            child.pack_forget()
        CTkLabel(self.__selected_ingredients_frame, text="مواد اولیه", font=('B Koodak Bold', 18)).pack()
        for selected_ingredient, amount in self.__selected_ingredients.items():
            CTkButton(self.__selected_ingredients_frame, text=f"{selected_ingredient}: {amount}", font=normal_text_font,
                      fg_color=('gray80', 'gray10'),
                      command=lambda name=selected_ingredient: delete_item_from_selected(name)).pack()

        CTkButton(self.__selected_ingredients_frame, text="ثبت", font=('B Koodak Bold', 25),
                  command=self.__submit).pack(pady=20)

    def __submit(self) -> None:
        name = self.__name_entry.get()

        def transform(data):
            item_idx = next((i for i, v in enumerate(self.__all_ingredients) if v['name'] == data), -1)
            ingredient = self.__all_ingredients[item_idx]
            return ingredient['id']

        self.__callback({'name': name, 'ingredients': {transform(ing): amount for ing, amount in
                                                       self.__selected_ingredients.items()}})

        self.destroy()
