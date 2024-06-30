from customtkinter import CTkToplevel, CTkLabel

from app.view.context import Context
from app.view.pages.components import SimpleTable


class CountInventoryItems(CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resizable(False, False)
        self._context = Context()
        self._data = self._context.controller.get_count_inventory_items()
        self._columns = [('name', 'نام'), ('quantity', 'تعداد')]
        CTkLabel(self, text='تعداد مواد اولیه موجود', font=('B Koodak Bold', 25)).pack(pady=15, padx=15)
        self._table = SimpleTable(self._data, self._columns, master=self)
        self._table.pack()
