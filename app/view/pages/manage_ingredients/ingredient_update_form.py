from typing import Callable

from customtkinter import CTkLabel, CTkButton, CTkEntry, CTkFrame, CTkToplevel

from app.view.constants import normal_text_font


class IngredientUpdateForm(CTkToplevel):
    def __init__(self, current_values: dict[str, str], callback: Callable, master=None, *args, **kwargs) -> None:
        super().__init__(master=master, *args, **kwargs)
        self.geometry("400x300")
        self.resizable(False, False)

        self.__current_values = current_values

        self.__callback = callback
        CTkLabel(
            master=self, text="ویرایش ماده اولیه", font=("B Koodak Bold", 25)
        ).pack(fill="x", anchor="center", pady=10)

        CTkLabel(self, text="نام", font=normal_text_font).pack()
        self.__name_entry = CTkEntry(self, font=normal_text_font)
        self.__name_entry.pack()
        self.__name_entry.insert(0, self.__current_values["name"])

        CTkLabel(self, text="واحد", font=normal_text_font).pack()
        self.__unit_entry = CTkEntry(self, font=normal_text_font)
        self.__unit_entry.pack()
        self.__unit_entry.insert(0, self.__current_values["unit"])

        CTkButton(self, text="ثبت", font=('B Koodak Bold', 25), command=self.__submit).pack(pady=20)

    def __submit(self) -> None:
        name = self.__name_entry.get()
        unit = self.__unit_entry.get()

        self.__callback({'id': self.__current_values['id'], 'name': name, 'unit': unit})

        self.destroy()
