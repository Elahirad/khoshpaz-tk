from app.view.pages.components import IDataView

from .food_form import FoodForm


class ManageFoods(IDataView):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__('foods', 'غذا', 'غذاها', [('name', 'نام'), ('parts', 'اجزا'), ('price', 'قیمت')],
                         {'id': 0, 'name': '', 'price': '', 'parts': {}, 'parts_raw': {}}, FoodForm, *args, **kwargs)

        self._report_frame.pack_forget()

    def _update_table(self):
        super()._update_table()
        self._report_frame.pack_forget()

    def _add_callback(self, data):
        self._context.controller.add_food(data['name'], data['price'], data['parts'])

    def _delete_callback(self, confirmed: bool, entity_id: int):
        if confirmed:
            self._context.controller.remove_food(entity_id)

    def _update_callback(self, food_id, item):
        self._context.controller.update_food(food_id, item['name'], item['price'], item['parts'])
