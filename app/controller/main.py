from app.view.interface import IView
from app.model import IDataStorage
from app.model import Ingredient


class Controller:
    def __init__(self, view: IView, data_storage: IDataStorage) -> None:
        self.view = view
        self.view.controller = self
        self.data_storage = data_storage
        self.view.reload_app_data()

    def get_ingredients(self, item_id=None):
        if item_id:
            return self.data_storage.get(Ingredient, item_id).__dict__
        return list(map(lambda o: o.__dict__, self.data_storage.get_all(Ingredient)))

    def add_ingredient(self, name, unit):
        ing = Ingredient(1, name, unit)
        ing = self.data_storage.add(ing).__dict__
        self.view.show_message('موفق', 'با موفقیت اضافه شد', 'check')
        return ing

    def update_ingredient(self, item_id, name, unit) -> dict:
        ing = self.data_storage.get(Ingredient, item_id)
        if ing:
            ing.name = name
            ing.unit = unit
            ing = self.data_storage.update(ing)
            self.view.show_message('موفق', 'با موفقیت آپدیت شد', 'check')
            return ing.__dict__
        else:
            self.view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')

    def remove_ingredient(self, item_id) -> bool:
        ing = self.data_storage.get(Ingredient, item_id)
        if ing:
            self.data_storage.remove(Ingredient, item_id)
            self.view.show_message('موفق', 'با موفقیت حذف شد', 'check')
            return True
        else:
            self.view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')
            return False
