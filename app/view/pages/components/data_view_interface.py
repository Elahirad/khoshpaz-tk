from customtkinter import CTkFrame, CTkLabel, CTkButton
from typing import Type

from app.view.pages.components import Table, DeleteDialog
from app.view.context import Context
from .form_interface import IForm


class IDataView(CTkFrame):
    def __init__(self, name_in_context: str, singular_name: str, plural_name: str, columns: list[tuple[str, str]],
                 empty_values: dict, form: Type[IForm], *args,
                 **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._form = form
        self._name_in_context = name_in_context
        self._empty_values = empty_values
        self._singular_name = singular_name
        self._plural_name = plural_name
        self._context = Context()
        self._context.add_callback(self._update_table)
        self.data = self._context[self._name_in_context]

        CTkLabel(
            master=self, text=f"مدیریت {self._plural_name}", font=("B Koodak Bold", 25)
        ).pack(fill="x", anchor="center", pady=10)

        self._columns = columns

        self._form_window = None

        self._delete_window = None

        self._add_button_frame = CTkFrame(self, fg_color='transparent')
        self._add_button_frame.pack(pady=10, padx=10, fill="x")
        self._add_button = CTkButton(self._add_button_frame, text='افزودن', font=('B Koodak Bold', 25),
                                     command=self._show_input_modal)
        self._add_button.pack()

        self._table = Table(self.data, self._columns, master=self, width=self.winfo_width(),
                            height=self.winfo_height(), delete_callback=self._show_delete_modal,
                            update_callback=self._show_update_modal)
        self._table.pack(pady=10, padx=10, fill="both", expand=True)

        # Report buttons
        self._report_frame = CTkFrame(master=self, fg_color='transparent')
        self._report_frame.pack(pady=10, fill="x")

    def _update_table(self):
        self.data = self._context[self._name_in_context]
        self._table.pack_forget()
        self._report_frame.pack_forget()
        self._table = Table(self.data, self._columns, master=self, width=self.winfo_width(),
                            height=self.winfo_height(), delete_callback=self._show_delete_modal,
                            update_callback=self._show_update_modal)
        self._table.pack(pady=10, padx=10, fill="both", expand=True)
        self._report_frame.pack(pady=10, fill="x")

    def _add_callback(self, data):
        pass

    def _update_callback(self, entity_id, data):
        pass

    def _delete_callback(self, confirmed, entity_id):
        pass

    def _show_delete_modal(self, entity_id: int):
        self._delete_window = DeleteDialog(f'حذف {self._singular_name} ؟',
                                           lambda confirmed, eid=entity_id: self._delete_callback(entity_id,
                                                                                                  confirmed))
        self._delete_window.grab_set()

    def _show_update_modal(self, entity: dict):
        self.__update_window = self._form(f'ویرایش {self._singular_name}', entity,
                                          lambda data, eid=entity['id']: self._update_callback(eid, data))
        self.__update_window.grab_set()

    def _show_input_modal(self):
        self._form_window = self._form(f'افزودن {self._singular_name}', self._empty_values,
                                       self._add_callback)
        self._form_window.grab_set()
