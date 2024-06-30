import datetime

from customtkinter import CTkLabel, CTkButton, CTkEntry, StringVar, CTkComboBox, CTkFrame

from app.view.constants import normal_text_font
from app.view.pages.components import CalendarFrame, IForm


class InventoryForm(IForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._ingredients = [i for i in self._context['ingredients']]
        self._ingredient_names = [i['name'] for i in self._context['ingredients']]

        print(self._ingredients)

        self._ingredient_combobox_var = StringVar(
            value='' if len(self._ingredients) == 0 else self._ingredients[
                next((i for i, v in enumerate(self._ingredients) if v['id'] == self._current_values['ingredient_id']),
                     -1)][
                'name'])
        CTkLabel(self, text="ماده", font=normal_text_font).pack()
        self._ingredient_combobox = CTkComboBox(master=self,
                                                values=[] if len(
                                                    self._ingredient_names) == 0 else self._ingredient_names,
                                                font=normal_text_font,
                                                state='disabled' if len(self._ingredients) == 0 else 'normal',
                                                variable=self._ingredient_combobox_var)
        self._ingredient_combobox._dropdown_menu.config(font=normal_text_font)
        self._ingredient_combobox.pack()

        frame = CTkFrame(self, fg_color='transparent')
        frame.pack(padx=15)
        CTkLabel(frame, text="مقدار", font=normal_text_font).grid(row=0, column=1, padx=5, pady=5)
        self._amount_entry = CTkEntry(frame, font=normal_text_font)
        self._amount_entry.grid(row=1, column=1, padx=5, pady=5)
        self._amount_entry.insert(0, self._current_values['quantity'])

        CTkLabel(frame, text="قیمت", font=normal_text_font).grid(row=0, column=0, padx=5, pady=5)
        self._price_entry = CTkEntry(frame, font=normal_text_font)
        self._price_entry.grid(row=1, column=0, padx=5, pady=5)
        self._price_entry.insert(0, self._current_values['price'])

        frame = CTkFrame(self, fg_color='transparent')
        frame.pack(padx=15)

        self._selected_entrance_date = datetime.datetime.strptime(self._current_values['entrance_date'], '%Y-%m-%d')

        self._entrance_date_calendar_frame = None
        CTkLabel(frame, text="زمان ورود", font=normal_text_font).grid(row=0, column=1, padx=5, pady=5)
        self._entrance_date_button = CTkButton(master=frame, text=str(datetime.date.today()), font=normal_text_font,
                                               command=self._choose_entrance_date)
        self._entrance_date_button.grid(row=1, column=1, padx=5, pady=5)

        self.__selected_manufacture_date = datetime.datetime.strptime(self._current_values['manufacture_date'],
                                                                      '%Y-%m-%d')

        self._manufacture_date_calendar_frame = None
        CTkLabel(frame, text="تاریخ تولید", font=normal_text_font).grid(row=0, column=0, padx=5, pady=5)
        self._manufacture_date_button = CTkButton(master=frame, text=str(datetime.date.today()), font=normal_text_font,
                                                  command=self._choose_manufacture_date)
        self._manufacture_date_button.grid(row=1, column=0, padx=5, pady=5)

        self._selected_expire_date = datetime.datetime.strptime(self._current_values['expire_date'], '%Y-%m-%d')

        self._expire_date_calendar_frame = None
        CTkLabel(self, text="تاریخ انقضاء", font=normal_text_font).pack(padx=5, pady=5)
        self._expire_date_button = CTkButton(master=self, text=str(datetime.date.today()), font=normal_text_font,
                                             command=self._choose_expire_date)
        self._expire_date_button.pack()

        CTkButton(self, text="ثبت", font=('B Koodak Bold', 25),
                  command=self._submit).pack(pady=20)

    def _choose_entrance_date(self):
        def update(date):
            self._selected_entrance_date = date
            self._entrance_date_button.configure(text=str(date))

        self._entrance_date_calendar_frame = CalendarFrame(update, self._selected_entrance_date)
        self._entrance_date_calendar_frame.grab_set()

    def _choose_manufacture_date(self):
        def update(date):
            self.__selected_manufacture_date = date
            self._manufacture_date_button.configure(text=str(date))

        self._manufacture_date_calendar_frame = CalendarFrame(update, self.__selected_manufacture_date)
        self._manufacture_date_calendar_frame.grab_set()

    def _choose_expire_date(self):
        def update(date):
            self._selected_expire_date = date
            self._expire_date_button.configure(text=str(date))

        self._expire_date_calendar_frame = CalendarFrame(update, self._selected_expire_date)
        self._expire_date_calendar_frame.grab_set()

    def _submit(self) -> None:
        ingredient_id = next((v['id'] for v in self._ingredients if v['name'] == self._ingredient_combobox_var.get()),
                             None)
        quantity = float(self._amount_entry.get())
        price = float(self._price_entry.get())
        entrance_date = self._selected_entrance_date.strftime('%Y-%m-%d')
        manufacture_date = self.__selected_manufacture_date.strftime('%Y-%m-%d')
        expire_date = self._selected_expire_date.strftime('%Y-%m-%d')

        self._callback(
            {'ingredient_id': ingredient_id, 'quantity': quantity, 'price': price, 'entrance_date': entrance_date,
             'manufacture_date': manufacture_date,
             'expire_date': expire_date})

        self.destroy()
