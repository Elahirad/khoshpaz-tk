import datetime

from customtkinter import CTkButton
from app.view.constants import normal_text_font

from .inventory_form import InventoryForm

from app.view.pages.components import IDataView
from app.view.reports import *


class ManageInventory(IDataView):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__('inventory', 'ماده‌ی موجود در انبار', 'مواد موجود در انبار',
                         [('id', 'آیدی'), ('ingredient', 'ماده اولیه'), ('quantity', 'تعداد'), ('price', 'قیمت'),
                          ('entrance_date', 'تاریخ ورود'),
                          ('manufacture_date', 'تاریخ تولید'), ('expire_date', 'تاریخ انقضا')],
                         {'id': 0, 'ingredient_id': 1, 'quantity': '', 'price': '',
                          'entrance_date': datetime.date.today().strftime("%Y-%m-%d"),
                          'manufacture_date': datetime.date.today().strftime("%Y-%m-%d"),
                          'expire_date': datetime.date.today().strftime("%Y-%m-%d")}, InventoryForm, *args,
                         **kwargs)

        self._report_frame1 = None
        self._report_frame2 = None
        self._report_frame3 = None
        self._report_frame4 = None
        self._report_frame5 = None

        self._report_button1 = CTkButton(master=self._report_frame, text="گزارش موجودی بحرانی", command=self._report1,
                                         font=normal_text_font)
        self._report_button2 = CTkButton(master=self._report_frame, text="گزارش باارزش‌ترین موارد",
                                         command=self._report2,
                                         font=normal_text_font)
        self._report_button3 = CTkButton(master=self._report_frame, text="گزارش موارد تاریخ گذشته",
                                         command=self._report3,
                                         font=normal_text_font)
        self._report_button4 = CTkButton(master=self._report_frame, text="گزارش مدت حضور مواد",
                                         command=self._report4,
                                         font=normal_text_font)
        self._report_button5 = CTkButton(master=self._report_frame, text="گزارش تعداد مواد",
                                         command=self._report5,
                                         font=normal_text_font)
        self._report_button1.pack(side="right", padx=5)
        self._report_button2.pack(side="right", padx=5)
        self._report_button3.pack(side="right", padx=5)
        self._report_button4.pack(side="right", padx=5)
        self._report_button5.pack(side="right", padx=5)

    def _add_callback(self, data):
        self._context.controller.add_inventory_item(data['ingredient_id'], data['quantity'], data['price'],
                                                    data['entrance_date'], data['manufacture_date'],
                                                    data['expire_date'])

    def _delete_callback(self, confirmed: bool, item_id: int):
        if confirmed:
            self._context.controller.remove_inventory_item(item_id)

    def _update_callback(self, entity_id: int, item: dict):
        self._context.controller.update_inventory_item(entity_id, item['ingredient_id'], item['quantity'],
                                                       item['price'], item['entrance_date'],
                                                       item['manufacture_date'], item['expire_date'])

    def _report1(self):
        self._report_frame1 = CriticalInventoryItems()
        self._report_frame1.grab_set()

    def _report2(self):
        self._report_frame2 = ValuableInventoryItems()
        self._report_frame2.grab_set()

    def _report3(self):
        self._report_frame3 = ExpiredInventoryItems()
        self._report_frame3.grab_set()

    def _report4(self):
        self._report_frame4 = DurationOfStayInventoryItems()
        self._report_frame4.grab_set()

    def _report5(self):
        self._report_frame5 = CountInventoryItems()
        self._report_frame5.grab_set()
