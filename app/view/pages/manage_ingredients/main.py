from app.view.pages.components import IDataView
from .ingredient_form import IngredientForm


class ManageIngredients(IDataView):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__('ingredients', 'ماده‌ی اولیه', 'مواد اولیه', [('name', 'نام'), ('unit', 'واحد')],
                         {'id': 0, 'name': '', 'unit': ''}, IngredientForm, *args,
                         **kwargs)

        self._report_frame.pack_forget()

    def _update_frame(self):
        super()._update_table()
        self._report_frame.place_forget()

    def _add_callback(self, data):
        self._context.controller.add_ingredient(data['name'], data['unit'])

    def _delete_callback(self, confirmed: bool, item_id: int):
        if confirmed:
            self._context.controller.remove_ingredient(item_id)

    def _update_callback(self, entity_id: int, item: dict):
        self._context.controller.update_ingredient(entity_id, item['name'], item['unit'])
