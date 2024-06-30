from customtkinter import CTkToplevel, CTkLabel

from app.view.context import Context
from app.view.pages.components import SimpleTable


class CriticalInventoryItems(CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resizable(False, False)
        self._context = Context()
        self._data = self._context.controller.get_critical_inventory_items()
        self._columns = [('name', 'نام'), ('quantity', 'مقدار')]
        CTkLabel(self, text='موارد دارای موجودی بحرانی', font=('B Koodak Bold', 25)).pack(pady=15, padx=15)
        self._table = SimpleTable(self._data, self._columns, master=self)
        self._table.pack()
