from app.view.interface import IView
from app.model import IDataStorage
from app.model import Ingredient, Part


class Controller:
    def __init__(self, view: IView, data_storage: IDataStorage) -> None:
        self.view = view
        self.view.controller = self
        self.data_storage = data_storage
        self.view.reload_app_data()

    def get_ingredients(self, item_id: int = None) -> list[dict] | dict:
        if item_id:
            return self.data_storage.get(Ingredient, item_id).__dict__
        return list(map(lambda o: o.__dict__, self.data_storage.get_all(Ingredient)))

    def add_ingredient(self, name: str, unit: str) -> dict:
        ing = Ingredient(1, name, unit)
        ing = self.data_storage.add(ing).__dict__
        self.view.show_message('موفق', 'با موفقیت اضافه شد', 'check')
        self.view.reload_app_data()
        return ing

    def update_ingredient(self, item_id: int, name: str, unit: str) -> dict:
        ingredient = self.data_storage.get(Ingredient, item_id)
        if ingredient:
            ingredient.name = name
            ingredient.unit = unit
            ingredient = self.data_storage.update(ingredient)
            self.view.show_message('موفق', 'با موفقیت آپدیت شد', 'check')
            self.view.reload_app_data()
            return ingredient.__dict__
        else:
            self.view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')

    def remove_ingredient(self, item_id: int) -> bool:
        ing = self.data_storage.get(Ingredient, item_id)
        if ing:
            self.data_storage.remove(Ingredient, item_id)
            self.view.show_message('موفق', 'با موفقیت حذف شد', 'check')
            self.view.reload_app_data()
            return True
        else:
            self.view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')
            return False

    def get_parts(self, item_id: int = None) -> list[dict] | dict:
        if item_id:
            part = self.data_storage.get(Part, item_id).__dict__
            ingredients = part['ingredients']
            ingredients_raw = {}
            new_ingredients = []
            for ing_id, amount in ingredients.items():
                ingredient = self.get_ingredients(int(ing_id))
                ingredients_raw[ingredient['name']] = amount
                new_ingredients.append(f"{ingredient['name']}: {amount} {ingredient['unit']}")
            part['ingredients'] = new_ingredients
            part['ingredients_raw'] = ingredients_raw
            return part
        parts = list(map(lambda o: o.__dict__, self.data_storage.get_all(Part)))
        for idx, part in enumerate(parts):
            ingredients = part['ingredients']
            ingredients_raw = {}
            new_ingredients = []
            for ing_id, amount in ingredients.items():
                ingredient = self.get_ingredients(int(ing_id))
                ingredients_raw[ingredient['name']] = amount
                new_ingredients.append(f"{ingredient['name']}: {amount} {ingredient['unit']}")
            part['ingredients'] = new_ingredients
            part['ingredients_raw'] = ingredients_raw
        return parts

    def add_part(self, name: str, ingredients: dict[int, float]):
        part = Part(1, name, ingredients)
        part = self.data_storage.add(part).__dict__
        self.view.show_message('موفق', 'با موفقیت اضافه شد', 'check')
        self.view.reload_app_data()
        return part

    def update_part(self, item_id: int, name: str, ingredients: dict[int, float]) -> dict:
        part = self.data_storage.get(Part, item_id)
        if part:
            part.name = name
            part.ingredients = ingredients
            part = self.data_storage.update(part)
            self.view.show_message('موفق', 'با موفقیت آپدیت شد', 'check')
            self.view.reload_app_data()
            return part.__dict__
        else:
            self.view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')

    def remove_part(self, item_id: int) -> bool:
        part = self.data_storage.get(Part, item_id)
        if part:
            self.data_storage.remove(Part, item_id)
            self.view.show_message('موفق', 'با موفقیت حذف شد', 'check')
            self.view.reload_app_data()
            return True
        else:
            self.view.show_message('خطا', 'مشکلی پیش آمد', 'cancel')
            return False
