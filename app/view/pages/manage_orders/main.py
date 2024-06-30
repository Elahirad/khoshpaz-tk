import datetime

from customtkinter import CTkFrame, CTkButton
from app.view.constants import normal_text_font
from app.view.pages.components import DeleteDialog

from app.view.pages.components import IDataView
from .order_form import OrderForm


class ManageOrders(IDataView):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__('orders', 'سفارش', 'سفارش‌ها',
                         [('customer', 'مشتری'), ('foods', 'غذاها'), ('paid_amount', 'مبلغ پرداختی'),
                          ('accept_time', 'زمان قبول'),
                          ('status', 'وضعیت'), ('preparation_time', 'زمان آماده‌سازی')],
                         {'id': 0, 'customer_id': 1, 'foods': [], 'paid_amount': '',
                          'accept_time': datetime.date.today().strftime('%Y-%m-%d'), 'status': 'در حال آماده سازی',
                          'preparation_time': '',
                          'foods_raw': {}},
                         OrderForm
                         , *args, **kwargs)

        self._report_button1 = CTkButton(master=self._report_frame, text="۱ گزارش", command=self._report1,
                                         font=normal_text_font)
        self._report_button2 = CTkButton(master=self._report_frame, text="۲ گزارش", command=self._report2,
                                         font=normal_text_font)
        self._report_button3 = CTkButton(master=self._report_frame, text="۳ گزارش", command=self._report3,
                                         font=normal_text_font)
        self._report_button1.pack(side="right", padx=5)
        self._report_button2.pack(side="right", padx=5)
        self._report_button3.pack(side="right", padx=5)

    def _add_callback(self, data):
        self._context.controller.add_order(data['customer_id'], data['foods'], data['paid_amount'], data['accept_time'],
                                           data['status'], data['preparation_time'])

    def _delete_callback(self, confirmed: bool, item_id: int):
        if confirmed:
            self._context.controller.remove_order(item_id)

    def _update_callback(self, entity_id: int, item: dict):
        self._context.controller.update_order(entity_id, item['customer_id'], item['foods'], item['paid_amount'],
                                              item['accept_time'], item['status'], item['preparation_time'])

    def _report1(self):
        print("۱ گزارش اجرا شد")

    def _report2(self):
        print("۲ گزارش اجرا شد")

    def _report3(self):
        print("۳ گزارش اجرا شد")
