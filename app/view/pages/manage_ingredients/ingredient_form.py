from customtkinter import CTkLabel, CTkButton, CTkEntry

from app.view.constants import normal_text_font
from app.view.pages.components import IForm


class IngredientForm(IForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        CTkLabel(self, text="نام", font=normal_text_font).pack()
        self._name_entry = CTkEntry(self, font=normal_text_font)
        self._name_entry.pack()
        self._name_entry.insert(0, self._current_values["name"])

        CTkLabel(self, text="واحد", font=normal_text_font).pack()
        self._unit_entry = CTkEntry(self, font=normal_text_font)
        self._unit_entry.pack()
        self._unit_entry.insert(0, self._current_values["unit"])

        CTkButton(self, text="ثبت", font=('B Koodak Bold', 25), command=self._submit).pack(pady=20)

    def _submit(self) -> None:
        name = self._name_entry.get()
        unit = self._unit_entry.get()

        self._callback({'id': self._current_values['id'], 'name': name, 'unit': unit})

        self.destroy()
