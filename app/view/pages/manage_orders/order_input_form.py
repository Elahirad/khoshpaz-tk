import datetime
from typing import Callable

from customtkinter import CTkLabel, CTkButton, CTkEntry, CTkToplevel, StringVar, CTkComboBox, CTkFrame

from tkinter import Spinbox

from app.view.constants import normal_text_font
from app.view.context import Context
from app.view.pages.components import CalendarFrame


class OrderInputForm(CTkToplevel):
    def __init__(self, callback: Callable, master=None, *args, **kwargs) -> None:
        super().__init__(master=master, *args, **kwargs)
        self.geometry("400x600")
        self.resizable(False, False)

        self.__context = Context()

        self.__callback = callback
        CTkLabel(
            master=self, text="افزودن سفارش", font=("B Koodak Bold", 25)
        ).pack(fill="x", anchor="center", pady=10)

        self.__customers = [c for c in self.__context['customers']]
        self.__customer_names = [f"{c['name']},{c['last_name']}" for c in self.__context['customers']]

        self.__customer_combobox_var = StringVar(
            value='' if len(self.__customer_names) == 0 else self.__customer_names[0])
        CTkLabel(self, text="مشتری", font=normal_text_font).pack()
        self.__customer_combobox = CTkComboBox(master=self,
                                               values=[] if len(self.__customer_names) == 0 else self.__customer_names,
                                               font=normal_text_font,
                                               variable=self.__customer_combobox_var)
        self.__customer_combobox._dropdown_menu.config(font=normal_text_font)
        self.__customer_combobox.pack()

        frame = CTkFrame(self, fg_color='transparent')
        frame.pack(padx=15)
        CTkLabel(frame, text="مبلغ پرداختی", font=normal_text_font).grid(row=0, column=1, padx=5, pady=5)
        self.__paid_amount_entry = CTkEntry(frame, font=normal_text_font)
        self.__paid_amount_entry.grid(row=1, column=1, padx=5, pady=5)

        CTkLabel(frame, text="زمان آماده‌سازی (ساعت)", font=normal_text_font).grid(row=0, column=0, padx=5, pady=5)
        self.__prep_time_entry = CTkEntry(frame, font=normal_text_font)
        self.__prep_time_entry.grid(row=1, column=0, padx=5, pady=5)

        frame = CTkFrame(self, fg_color='transparent')
        frame.pack(padx=15)
        CTkLabel(frame, text="وضعیت", font=normal_text_font).grid(row=0, column=1, padx=5, pady=5)
        self.__status_combobox_var = StringVar(
            value='در حال آماده‌سازی')

        self.__status_combobox = CTkComboBox(master=frame,
                                             values=['در حال آماده‌سازی', 'تکمیل شده'],
                                             font=normal_text_font,
                                             variable=self.__status_combobox_var)
        self.__status_combobox._dropdown_menu.config(font=normal_text_font)
        self.__status_combobox.grid(row=1, column=1, padx=5, pady=5)

        self.__selected_date = datetime.date.today()

        self.__calendar_frame = None
        CTkLabel(frame, text="زمان قبول", font=normal_text_font).grid(row=0, column=0, padx=5, pady=5)
        self.__date_button = CTkButton(master=frame, text=str(datetime.date.today()), font=normal_text_font,
                                       command=self.__choose_date)
        self.__date_button.grid(row=1, column=0, padx=5, pady=5)

        self.__all_foods = [item for item in self.__context['foods']]
        self.__selected_foods = {}

        self.__foods_combobox_var = StringVar(value='' if len(self.__all_foods) == 0 else self.__all_foods[0]['name'])

        self._select_frame = CTkFrame(self, fg_color='transparent')
        self._select_frame.pack(pady=15)

        self.__foods_combobox = CTkComboBox(master=self._select_frame,
                                            values=[] if len(self.__all_foods) == 0 else (
                                                list(map(lambda x: x['name'], self.__all_foods))),
                                            font=normal_text_font,
                                            variable=self.__foods_combobox_var)
        self.__foods_combobox._dropdown_menu.config(font=normal_text_font)
        self.__foods_combobox.grid(column=2, row=0)

        self.__amount_spinbox = Spinbox(self._select_frame, from_=0, to=100, increment=1, width=5)
        self.__amount_spinbox.grid(column=1, row=0)
        CTkButton(self._select_frame, text="افزودن", font=normal_text_font,
                  command=self.__add_ingredient).grid(column=0, row=0)

        self.__selected_foods_frame = CTkFrame(self, fg_color='transparent')
        self.__selected_foods_frame.pack(fill='both', expand=True)
        self.__show_selected_foods()

    def __choose_date(self):
        def update(date):
            self.__selected_date = date
            self.__date_button.configure(text=str(date))

        self.__calendar_frame = CalendarFrame(update, self.__selected_date)
        self.__calendar_frame.grab_set()

    def __add_ingredient(self) -> None:
        self.__selected_foods[self.__foods_combobox_var.get()] = self.__amount_spinbox.get()
        self.__show_selected_foods()

    def __show_selected_foods(self):
        def delete_item_from_selected(item_name):
            del self.__selected_foods[item_name]
            self.__show_selected_foods()

        for child in self.__selected_foods_frame.winfo_children():
            child.pack_forget()
        CTkLabel(self.__selected_foods_frame, text="غذاها", font=('B Koodak Bold', 18)).pack()
        for selected_ingredient, amount in self.__selected_foods.items():
            CTkButton(self.__selected_foods_frame, text=f"{selected_ingredient}: {amount}", font=normal_text_font,
                      fg_color=('gray80', 'gray10'),
                      command=lambda name=selected_ingredient: delete_item_from_selected(name)).pack()

        CTkButton(self.__selected_foods_frame, text="ثبت", font=('B Koodak Bold', 25),
                  command=self.__submit).pack(pady=20)

    def __submit(self) -> None:
        name, last_name = self.__customer_combobox_var.get().split(',')
        customer_id = next((v['id'] for v in self.__customers if v['name'] == name and v['last_name'] == last_name),
                           None)
        paid_amount = self.__paid_amount_entry.get()
        accept_date = self.__selected_date.strftime('%Y-%m-%d')
        status = 1 if self.__status_combobox_var.get() == 'تکمیل شده' else 0
        preparation_time = self.__prep_time_entry.get()

        def transform(data):
            item_idx = next((i for i, v in enumerate(self.__all_foods) if v['name'] == data), -1)
            food = self.__all_foods[item_idx]
            return food['id']

        self.__callback(customer_id=customer_id, paid_amount=paid_amount,
                        foods={transform(food): amount for food, amount in self.__selected_foods.items()},
                        accept_time=accept_date,
                        status=status, preparation_time=preparation_time)

        self.destroy()
