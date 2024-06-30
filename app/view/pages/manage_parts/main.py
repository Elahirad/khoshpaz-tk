from customtkinter import CTkButton

from app.view.constants import normal_text_font
from app.view.pages.components import IDataView
from .part_form import PartForm


class ManageParts(IDataView):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__('parts', 'جزء غذا', 'اجزاء غذا', [('name', 'نام'), ('ingredients', 'مواد اولیه')],
                         {'id': 0, 'name': '', 'ingredients': [],
                          'ingredients_raw': {'برنج': '0.2'}}, PartForm, *args, **kwargs)

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
        self._context.controller.add_part(data['name'], data['ingredients'])

    def _delete_callback(self, confirmed: bool, item_id: int):
        if confirmed:
            self._context.controller.remove_part(item_id)

    def _update_callback(self, entity_id: int, item: dict):
        self._context.controller.update_part(entity_id, item['name'], item['ingredients'])

    def _report1(self):
        print("۱ گزارش اجرا شد")

    def _report2(self):
        print("۲ گزارش اجرا شد")

    def _report3(self):
        print("۳ گزارش اجرا شد")
