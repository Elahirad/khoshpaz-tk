from customtkinter import CTkToplevel, CTkLabel

from app.view.context import Context
from app.view.pages.components import SimpleTable


class DurationOfStayInventoryItems(CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resizable(False, False)
        self._context = Context()
        self._data = self._context.controller.get_duration_of_stay_in_inventory()
        self._columns = [['id', 'آیدی'], ('name', 'نام'), ('duration', 'مدت زمان(روز)')]
        CTkLabel(self, text='مدت حضور مواد در انبار', font=('B Koodak Bold', 25)).pack(pady=15, padx=15)
        self._table = SimpleTable(self._data, self._columns, master=self)
        self._table.pack()
