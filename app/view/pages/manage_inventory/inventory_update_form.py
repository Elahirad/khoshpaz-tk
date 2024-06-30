import datetime
from typing import Callable

from customtkinter import CTkLabel, CTkButton, CTkEntry, CTkToplevel, StringVar, CTkComboBox, CTkFrame

from app.view.constants import normal_text_font
from app.view.context import Context
from app.view.pages.components import CalendarFrame


class InventoryUpdateForm(CTkToplevel):
    def __init__(self, current_values: dict, callback: Callable, master=None, *args, **kwargs) -> None:
        super().__init__(master=master, *args, **kwargs)
        self.geometry("400x600")
        self.resizable(False, False)

        self.__context = Context()

        self.__current_values = current_values

        self.__callback = callback
        CTkLabel(
            master=self, text="ویرایش ماده موجود در انبار", font=("B Koodak Bold", 25)
        ).pack(fill="x", anchor="center", pady=10)

        self.__ingredients = [i for i in self.__context['ingredients']]
        self.__ingredient_names = [i['name'] for i in self.__context['ingredients']]

        self.__ingredient_combobox_var = StringVar(
            value=self.__ingredients[
                next(i for i, v in enumerate(self.__ingredients) if v['id'] == self.__current_values['ingredient_id'])][
                'name'])
        CTkLabel(self, text="ماده", font=normal_text_font).pack()
        self.__ingredient_combobox = CTkComboBox(master=self,
                                                 values=[] if len(
                                                     self.__ingredient_names) == 0 else self.__ingredient_names,
                                                 font=normal_text_font,
                                                 variable=self.__ingredient_combobox_var)
        self.__ingredient_combobox._dropdown_menu.config(font=normal_text_font)
        self.__ingredient_combobox.pack()

        frame = CTkFrame(self, fg_color='transparent')
        frame.pack(padx=15)
        CTkLabel(frame, text="مقدار", font=normal_text_font).grid(row=0, column=1, padx=5, pady=5)
        self.__amount_entry = CTkEntry(frame, font=normal_text_font)
        self.__amount_entry.grid(row=1, column=1, padx=5, pady=5)
        self.__amount_entry.insert(0, self.__current_values['quantity'])

        CTkLabel(frame, text="قیمت", font=normal_text_font).grid(row=0, column=0, padx=5, pady=5)
        self.__price_entry = CTkEntry(frame, font=normal_text_font)
        self.__price_entry.grid(row=1, column=0, padx=5, pady=5)
        self.__price_entry.insert(0, self.__current_values['price'])

        frame = CTkFrame(self, fg_color='transparent')
        frame.pack(padx=15)

        self.__selected_entrance_date = datetime.datetime.strptime(self.__current_values['entrance_date'], '%Y-%m-%d')

        self.__entrance_date_calendar_frame = None
        CTkLabel(frame, text="زمان ورود", font=normal_text_font).grid(row=0, column=1, padx=5, pady=5)
        self.__entrance_date_button = CTkButton(master=frame, text=str(datetime.date.today()), font=normal_text_font,
                                                command=self.__choose_entrance_date)
        self.__entrance_date_button.grid(row=1, column=1, padx=5, pady=5)

        self.__selected_manufacture_date = datetime.datetime.strptime(self.__current_values['manufacture_date'],
                                                                      '%Y-%m-%d')

        self.__manufacture_date_calendar_frame = None
        CTkLabel(frame, text="تاریخ تولید", font=normal_text_font).grid(row=0, column=0, padx=5, pady=5)
        self.__manufacture_date_button = CTkButton(master=frame, text=str(datetime.date.today()), font=normal_text_font,
                                                   command=self.__choose_manufacture_date)
        self.__manufacture_date_button.grid(row=1, column=0, padx=5, pady=5)

        self.__selected_expire_date = datetime.datetime.strptime(self.__current_values['expire_date'], '%Y-%m-%d')

        self.__expire_date_calendar_frame = None
        CTkLabel(self, text="تاریخ انقضاء", font=normal_text_font).pack(padx=5, pady=5)
        self.__expire_date_button = CTkButton(master=self, text=str(datetime.date.today()), font=normal_text_font,
                                              command=self.__choose_expire_date)
        self.__expire_date_button.pack()

        CTkButton(self, text="ثبت", font=('B Koodak Bold', 25),
                  command=self.__submit).pack(pady=20)

    def __choose_entrance_date(self):
        def update(date):
            self.__selected_entrance_date = date
            self.__entrance_date_button.configure(text=str(date))

        self.__entrance_date_calendar_frame = CalendarFrame(update, self.__selected_entrance_date)
        self.__entrance_date_calendar_frame.grab_set()

    def __choose_manufacture_date(self):
        def update(date):
            self.__selected_manufacture_date = date
            self.__manufacture_date_button.configure(text=str(date))

        self.__manufacture_date_calendar_frame = CalendarFrame(update, self.__selected_manufacture_date)
        self.__manufacture_date_calendar_frame.grab_set()

    def __choose_expire_date(self):
        def update(date):
            self.__selected_expire_date = date
            self.__expire_date_button.configure(text=str(date))

        self.__expire_date_calendar_frame = CalendarFrame(update, self.__selected_expire_date)
        self.__expire_date_calendar_frame.grab_set()

    def __submit(self) -> None:
        ingredient_id = next((v['id'] for v in self.__ingredients if v['name'] == self.__ingredient_combobox_var.get()),
                             None)
        quantity = float(self.__amount_entry.get())
        price = float(self.__price_entry.get())
        entrance_date = self.__selected_entrance_date.strftime('%Y-%m-%d')
        manufacture_date = self.__selected_manufacture_date.strftime('%Y-%m-%d')
        expire_date = self.__selected_expire_date.strftime('%Y-%m-%d')

        self.__callback(
            {'ingredient_id': ingredient_id, 'quantity': quantity, 'price': price, 'entrance_date': entrance_date,
             'manufacture_date': manufacture_date,
             'expire_date': expire_date})

        self.destroy()
