import datetime

from customtkinter import CTkLabel, CTkButton, CTkEntry, StringVar, CTkComboBox, CTkFrame

from tkinter import Spinbox

from app.view.constants import normal_text_font
from app.view.pages.components import CalendarFrame
from app.view.pages.components import IForm


class OrderForm(IForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._customers = [c for c in self._context['customers']]
        self._customer_names = [f"{c['name']},{c['last_name']}" for c in self._context['customers']]

        self._customer_combobox_var = StringVar(
            value=self._customer_names[
                next((i for i, v in enumerate(self._customers) if v['id'] == self._current_values['customer_id']), -1)])
        CTkLabel(self, text="مشتری", font=normal_text_font).pack()
        self._customer_combobox = CTkComboBox(master=self,
                                              values=[] if len(self._customer_names) == 0 else self._customer_names,
                                              font=normal_text_font,
                                              variable=self._customer_combobox_var)
        self._customer_combobox._dropdown_menu.config(font=normal_text_font)
        self._customer_combobox.pack()

        frame = CTkFrame(self, fg_color='transparent')
        frame.pack(padx=15)
        CTkLabel(frame, text="مبلغ پرداختی", font=normal_text_font).grid(row=0, column=1, padx=5, pady=5)
        self._paid_amount_entry = CTkEntry(frame, font=normal_text_font)
        self._paid_amount_entry.grid(row=1, column=1, padx=5, pady=5)
        self._paid_amount_entry.insert(0, self._current_values['paid_amount'])

        CTkLabel(frame, text="زمان آماده‌سازی (ساعت)", font=normal_text_font).grid(row=0, column=0, padx=5, pady=5)
        self._prep_time_entry = CTkEntry(frame, font=normal_text_font)
        self._prep_time_entry.grid(row=1, column=0, padx=5, pady=5)
        self._prep_time_entry.insert(0, self._current_values['preparation_time'])

        frame = CTkFrame(self, fg_color='transparent')
        frame.pack(padx=15)
        CTkLabel(frame, text="وضعیت", font=normal_text_font).grid(row=0, column=1, padx=5, pady=5)
        self._status_combobox_var = StringVar(
            value=self._current_values['status'])

        self._status_combobox = CTkComboBox(master=frame,
                                            values=['در حال آماده‌سازی', 'تکمیل شده'],
                                            font=normal_text_font,
                                            variable=self._status_combobox_var)
        self._status_combobox._dropdown_menu.config(font=normal_text_font)
        self._status_combobox.grid(row=1, column=1, padx=5, pady=5)
        self._selected_date = datetime.datetime.strptime(self._current_values['accept_time'], '%Y-%m-%d')

        self._calendar_frame = None
        CTkLabel(frame, text="زمان قبول", font=normal_text_font).grid(row=0, column=0, padx=5, pady=5)
        self._date_button = CTkButton(master=frame, text=str(datetime.date.today()), font=normal_text_font,
                                      command=self._choose_date)
        self._date_button.grid(row=1, column=0, padx=5, pady=5)

        self._all_foods = [item for item in self._context['foods']]
        self._selected_foods = self._current_values['foods_raw']

        self._foods_combobox_var = StringVar(value='' if len(self._all_foods) == 0 else self._all_foods[0]['name'])

        self._select_frame = CTkFrame(self, fg_color='transparent')
        self._select_frame.pack(pady=15)

        self._foods_combobox = CTkComboBox(master=self._select_frame,
                                           values=[] if len(self._all_foods) == 0 else (
                                               list(map(lambda x: x['name'], self._all_foods))),
                                           font=normal_text_font,
                                           variable=self._foods_combobox_var)
        self._foods_combobox._dropdown_menu.config(font=normal_text_font)
        self._foods_combobox.grid(column=2, row=0)

        self._amount_spinbox = Spinbox(self._select_frame, from_=0, to=100, increment=1, width=5)
        self._amount_spinbox.grid(column=1, row=0)
        CTkButton(self._select_frame, text="افزودن", font=normal_text_font,
                  command=self._add_ingredient).grid(column=0, row=0)

        self._selected_foods_frame = CTkFrame(self, fg_color='transparent')
        self._selected_foods_frame.pack(fill='both', expand=True)
        self._show_selected_foods()

    def _choose_date(self):
        def update(date):
            self._selected_date = date
            self._date_button.configure(text=str(date))

        self._calendar_frame = CalendarFrame(update, self._selected_date)
        self._calendar_frame.grab_set()

    def _add_ingredient(self) -> None:
        self._selected_foods[self._foods_combobox_var.get()] = self._amount_spinbox.get()
        self._show_selected_foods()

    def _show_selected_foods(self):
        def delete_item_from_selected(item_name):
            del self._selected_foods[item_name]
            self._show_selected_foods()

        for child in self._selected_foods_frame.winfo_children():
            child.pack_forget()
        CTkLabel(self._selected_foods_frame, text="غذاها", font=('B Koodak Bold', 18)).pack()
        for selected_ingredient, amount in self._selected_foods.items():
            CTkButton(self._selected_foods_frame, text=f"{selected_ingredient}: {amount}", font=normal_text_font,
                      fg_color=('gray80', 'gray10'),
                      command=lambda name=selected_ingredient: delete_item_from_selected(name)).pack()

        CTkButton(self._selected_foods_frame, text="ثبت", font=('B Koodak Bold', 25),
                  command=self._submit).pack(pady=20)

    def _submit(self) -> None:
        name, last_name = self._customer_combobox_var.get().split(',')
        customer_id = next((v['id'] for v in self._customers if v['name'] == name and v['last_name'] == last_name),
                           None)
        paid_amount = self._paid_amount_entry.get()
        accept_date = self._selected_date.strftime('%Y-%m-%d')
        status = 1 if self._status_combobox_var.get() == 'تکمیل شده' else 0
        preparation_time = self._prep_time_entry.get()

        def transform(data):
            item_idx = next((i for i, v in enumerate(self._all_foods) if v['name'] == data), -1)
            food = self._all_foods[item_idx]
            return food['id']

        self._callback({'customer_id': customer_id, 'paid_amount': paid_amount,
                        'foods': {transform(food): amount for food, amount in self._selected_foods.items()},
                        'accept_time': accept_date,
                        'status': status, 'preparation_time': preparation_time})

        self.destroy()
