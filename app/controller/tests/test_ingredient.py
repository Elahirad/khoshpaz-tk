import unittest
from unittest.mock import MagicMock

from app.controller import Controller
from app.model import IDataStorage, Ingredient
from app.view import IView


class TestIngredient(unittest.TestCase):
    def setUp(self):
        self.view = MagicMock(spec=IView)
        self.data_storage = MagicMock(spec=IDataStorage)
        self.controller = Controller(self.view, self.data_storage)

    def test_get_ingredients(self):
        self.data_storage.get_all.return_value = [Ingredient(id=1, name='نمک', unit='گرم')]
        ingredients = self.controller.get_ingredients()
        self.assertEqual(len(ingredients), 1)
        self.assertEqual(ingredients[0]['name'], 'نمک')

    def test_add_ingredient(self):
        ingredient = Ingredient(id=1, name='نمک', unit='گرم')
        self.data_storage.add.return_value = ingredient
        result = self.controller.add_ingredient('نمک', 'گرم')
        self.assertEqual(result['name'], 'نمک')
        self.view.show_message.assert_called_once()
        self.view.reload_data.assert_called_once_with(['ingredients'])

    def test_update_ingredient(self):
        ingredient = Ingredient(id=1, name='نمک', unit='گرم')
        self.data_storage.get.return_value = ingredient
        self.data_storage.update.return_value = ingredient
        result = self.controller.update_ingredient(1, 'Sugar', 'kg')
        self.assertEqual(result['name'], 'Sugar')
        self.view.show_message.assert_called_once()
        self.view.reload_data.assert_called_once_with(['ingredients'])

    def test_remove_ingredient(self):
        ingredient = Ingredient(id=1, name='نمک', unit='گرم')
        self.data_storage.get.return_value = ingredient
        self.data_storage.get_all.return_value = []
        result = self.controller.remove_ingredient(1)
        self.assertTrue(result)
        self.view.show_message.assert_called_once()
        self.view.reload_data.assert_called_once_with(['ingredients'])
