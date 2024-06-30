from typing import Callable

from customtkinter import CTkLabel, CTkButton, CTkEntry, CTkFrame, CTkToplevel

from app.view.constants import normal_text_font
from app.view.pages.components import IForm


class CustomerForm(IForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        CTkLabel(self, text="نام", font=normal_text_font).pack()
        self._name_entry = CTkEntry(self, font=normal_text_font)
        self._name_entry.pack()
        self._name_entry.insert(0, self._current_values["name"])

        CTkLabel(self, text="نام خانوادگی", font=normal_text_font).pack()
        self._last_name_entry = CTkEntry(self, font=normal_text_font)
        self._last_name_entry.pack()
        self._last_name_entry.insert(0, self._current_values["last_name"])

        CTkButton(self, text="ثبت", font=('B Koodak Bold', 25), command=self._submit).pack(pady=20)

    def _submit(self) -> None:
        name = self._name_entry.get()
        last_name = self._last_name_entry.get()

        self._callback({'id': self._current_values['id'], 'name': name, 'last_name': last_name})

        self.destroy()
