from app.view.pages.components import IDataView
from .part_form import PartForm


class ManageParts(IDataView):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__('parts', 'جزء غذا', 'اجزاء غذا', [('name', 'نام'), ('ingredients', 'مواد اولیه')],
                         {'id': 0, 'name': '', 'ingredients': [],
                          'ingredients_raw': {}}, PartForm, *args, **kwargs)

        self._report_frame.pack_forget()

    def _update_frame(self):
        super()._update_table()
        self._report_frame.pack_forget()

    def _add_callback(self, data):
        self._context.controller.add_part(data['name'], data['ingredients'])

    def _delete_callback(self, confirmed: bool, item_id: int):
        if confirmed:
            self._context.controller.remove_part(item_id)

    def _update_callback(self, entity_id: int, item: dict):
        self._context.controller.update_part(entity_id, item['name'], item['ingredients'])
