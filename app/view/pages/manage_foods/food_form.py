from customtkinter import CTkLabel, CTkButton, CTkEntry, StringVar, CTkComboBox, CTkFrame

from tkinter import Spinbox

from app.view.constants import normal_text_font
from app.view.pages.components import IForm


class FoodForm(IForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        CTkLabel(self, text="نام", font=normal_text_font).pack()
        self._name_entry = CTkEntry(self, font=normal_text_font)
        self._name_entry.pack()
        self._name_entry.insert(0, self._current_values["name"])

        CTkLabel(self, text="قیمت", font=normal_text_font).pack()
        self._price_entry = CTkEntry(self, font=normal_text_font)
        self._price_entry.pack()
        self._price_entry.insert(0, self._current_values["price"])

        self._all_parts = [item for item in self._context['parts']]
        self._selected_parts = self._current_values['parts_raw']

        self._combobox_var = StringVar(value='' if len(self._all_parts) == 0 else self._all_parts[0]['name'])

        self._select_frame = CTkFrame(self, fg_color='transparent')
        self._select_frame.pack(pady=15)

        self._combobox = CTkComboBox(master=self._select_frame,
                                     values=list(map(lambda x: x['name'], self._all_parts)),
                                     font=normal_text_font,
                                     state='disabled' if len(self._all_parts) == 0 else 'normal',
                                     variable=self._combobox_var)
        self._combobox._dropdown_menu.config(font=normal_text_font)
        self._combobox.grid(column=2, row=0)

        self._amount_spinbox = Spinbox(self._select_frame, from_=0, to=100, increment=1, width=5)
        self._amount_spinbox.grid(column=1, row=0)
        CTkButton(self._select_frame, text="افزودن", font=normal_text_font,
                  command=self._add_ingredient).grid(column=0, row=0)

        self._selected_parts_frame = CTkFrame(self, fg_color='transparent')
        self._selected_parts_frame.pack(fill='both', expand=True)
        self._show_selected_parts()

    def _add_ingredient(self) -> None:
        self._selected_parts[self._combobox_var.get()] = self._amount_spinbox.get()
        self._show_selected_parts()

    def _show_selected_parts(self):
        def delete_item_from_selected(item_name):
            del self._selected_parts[item_name]
            self._show_selected_parts()

        for child in self._selected_parts_frame.winfo_children():
            child.pack_forget()
        CTkLabel(self._selected_parts_frame, text="اجزا", font=('B Koodak Bold', 18)).pack()
        for selected_ingredient, amount in self._selected_parts.items():
            CTkButton(self._selected_parts_frame, text=f"{selected_ingredient}: {amount}", font=normal_text_font,
                      fg_color=('gray80', 'gray10'),
                      command=lambda name=selected_ingredient: delete_item_from_selected(name)).pack()

        CTkButton(self._selected_parts_frame, text="ثبت", font=('B Koodak Bold', 25),
                  command=self._submit).pack(pady=20)

    def _submit(self) -> None:
        name = self._name_entry.get()
        price = self._price_entry.get()

        def transform(data):
            item_idx = next((i for i, v in enumerate(self._all_parts) if v['name'] == data), -1)
            part = self._all_parts[item_idx]
            return part['id']

        self._callback({'name': name, 'price': price,
                        'parts': {transform(part): amount for part, amount in self._selected_parts.items()}})

        self.destroy()
