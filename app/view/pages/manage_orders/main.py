from customtkinter import CTkFrame, CTkLabel, CTkButton
from app.view.constants import normal_text_font
from app.view.pages.components import Table, DeleteDialog
from app.view.context import Context
from .order_input_form import OrderInputForm
from .order_update_form import OrderUpdateForm


class ManageOrders(CTkFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__context = Context()
        self.__context.add_callback(self.__update_table)
        self.data = self.__context['orders']

        CTkLabel(
            master=self, text="مدیریت سفارش‌ها", font=("B Koodak Bold", 25)
        ).pack(fill="x", anchor="center", pady=10)

        self.__columns = [('customer', 'مشتری'), ('foods', 'غذاها'), ('paid_amount', 'مبلغ پرداختی'),
                          ('accept_time', 'زمان قبول'),
                          ('status', 'وضعیت'), ('preparation_time', 'زمان آماده‌سازی')]

        def show_input_modal():
            self.__input_window = OrderInputForm(self.__add_callback)
            self.__input_window.grab_set()

        self.__input_window = None

        self.__update_window = None
        self.__delete_window = None

        self.__add_button_frame = CTkFrame(self, fg_color='transparent')
        self.__add_button_frame.pack(pady=10, padx=10, fill="x")
        self.__add_button = CTkButton(self.__add_button_frame, text='افزودن', font=('B Koodak Bold', 25),
                                      command=show_input_modal)
        self.__add_button.pack()

        self.__table = Table(self.data, self.__columns, master=self, width=self.winfo_width(),
                             height=self.winfo_height(), delete_callback=self.__delete_callback,
                             update_callback=self.__update_callback)
        self.__table.pack(pady=10, padx=10, fill="both", expand=True)

        # Report buttons
        self.__report_frame = CTkFrame(master=self, fg_color='transparent')
        self.__report_frame.pack(pady=10, fill="x")

        self.__report_button1 = CTkButton(master=self.__report_frame, text="۱ گزارش", command=self.__report1,
                                          font=normal_text_font)
        self.__report_button2 = CTkButton(master=self.__report_frame, text="۲ گزارش", command=self.__report2,
                                          font=normal_text_font)
        self.__report_button3 = CTkButton(master=self.__report_frame, text="۳ گزارش", command=self.__report3,
                                          font=normal_text_font)
        self.__report_button1.pack(side="right", padx=5)
        self.__report_button2.pack(side="right", padx=5)
        self.__report_button3.pack(side="right", padx=5)

    def __update_table(self):
        self.data = self.__context['orders']
        self.__table.pack_forget()
        self.__report_frame.pack_forget()
        self.__table = Table(self.data, self.__columns, master=self, width=self.winfo_width(),
                             height=self.winfo_height(), delete_callback=self.__delete_callback,
                             update_callback=self.__update_callback)
        self.__table.pack(pady=10, padx=10, fill="both", expand=True)
        self.__report_frame.pack(pady=10, fill="x")

    def __add_callback(self, customer_id, paid_amount, foods, accept_time, status, preparation_time):
        self.__context.controller.add_order(customer_id, foods, paid_amount, accept_time, status, preparation_time)

    def __delete_callback(self, item_id: int):
        def delete(confirmed: bool):
            if confirmed:
                self.__context.controller.remove_order(item_id)

        self.__delete_window = DeleteDialog('حذف سفارش ؟', delete)
        self.__delete_window.grab_set()

    def __update_callback(self, item: dict):
        def update(data):
            self.__context.controller.update_order(item['id'], data['customer_id'], data['foods'], data['paid_amount'],
                                                   data['accept_time'], data['status'], data['preparation_time'])

        self.__update_window = OrderUpdateForm(item, update)
        self.__update_window.grab_set()

    def __report1(self):
        print("۱ گزارش اجرا شد")

    def __report2(self):
        print("۲ گزارش اجرا شد")

    def __report3(self):
        print("۳ گزارش اجرا شد")
