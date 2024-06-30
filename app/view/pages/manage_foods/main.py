from customtkinter import CTkButton
from app.view.constants import normal_text_font
from app.view.pages.components import IDataView

from .food_form import FoodForm


class ManageFoods(IDataView):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__('foods', 'غذا', 'غذاها', [('name', 'نام'), ('parts', 'اجزا'), ('price', 'قیمت')],
                         {'id': 0, 'name': '', 'price': '', 'parts': {}, 'parts_raw': {}}, FoodForm, *args, **kwargs)

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
        self._context.controller.add_food(data['name'], data['price'], data['parts'])

    def _delete_callback(self, confirmed: bool, entity_id: int):
        if confirmed:
            self._context.controller.remove_food(entity_id)

    def _update_callback(self, food_id, item):
        self._context.controller.update_food(food_id, item['name'], item['price'], item['parts'])

    def _report1(self):
        print("۱ گزارش اجرا شد")

    def _report2(self):
        print("۲ گزارش اجرا شد")

    def _report3(self):
        print("۳ گزارش اجرا شد")
