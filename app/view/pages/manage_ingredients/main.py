from customtkinter import CTkButton

from app.view.constants import normal_text_font
from app.view.pages.components import IDataView
from .ingredient_form import IngredientForm


class ManageIngredients(IDataView):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__('ingredients', 'ماده‌ی اولیه', 'مواد اولیه', [('name', 'نام'), ('unit', 'واحد')],
                         {'id': 0, 'name': '', 'unit': ''}, IngredientForm, *args,
                         **kwargs)

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
        self._context.controller.add_ingredient(data['name'], data['unit'])

    def _delete_callback(self, confirmed: bool, item_id: int):
        if confirmed:
            self._context.controller.remove_ingredient(item_id)

    def _update_callback(self, entity_id: int, item: dict):
        self._context.controller.update_ingredient(entity_id, item['name'], item['unit'])

    def _report1(self):
        print("۱ گزارش اجرا شد")

    def _report2(self):
        print("۲ گزارش اجرا شد")

    def _report3(self):
        print("۳ گزارش اجرا شد")
