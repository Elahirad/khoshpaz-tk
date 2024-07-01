import unittest
from unittest.mock import MagicMock

from app.controller import Controller
from app.model import IDataStorage, Food, Part, Ingredient
from app.view import IView


class TestFood(unittest.TestCase):
    def setUp(self):
        self.view = MagicMock(spec=IView)
        self.data_storage = MagicMock(spec=IDataStorage)
        self.controller = Controller(self.view, self.data_storage)

    def test_get_foods(self):
        food = Food(id=1, name='پیتزا', price=10.0, parts={1: 1})
        part = Part(id=1, name='جزء اول', ingredients={1: 100})
        ingredient = Ingredient(id=1, name='نمک', unit='g')
        self.data_storage.get_all.return_value = [food]
        self.data_storage.get.side_effect = [part, ingredient]
        foods = self.controller.get_foods()
        self.assertEqual(len(foods), 1)
        self.assertIn('جزء اول', foods[0]['parts'][0])

    def test_add_food(self):
        food = Food(id=1, name='پیتزا', price=10.0, parts={1: 1})
        self.data_storage.add.return_value = food
        result = self.controller.add_food('پیتزا', 10.0, {1: 1})
        self.assertEqual(result['name'], 'پیتزا')
        self.view.show_message.assert_called_once()
        self.view.reload_data.assert_called_once_with(['foods'])

    def test_update_food(self):
        food = Food(id=1, name='پیتزا', price=10.0, parts={1: 1})
        self.data_storage.get.return_value = food
        self.data_storage.update.return_value = food
        result = self.controller.update_food(1, 'برگر', 12.0, {2: 1})
        self.assertEqual(result['name'], 'برگر')
        self.view.show_message.assert_called_once()
        self.view.reload_data.assert_called_once_with(['foods'])

    def test_remove_food(self):
        food = Food(id=1, name='پیتزا', price=10.0, parts={1: 1})
        self.data_storage.get.return_value = food
        self.data_storage.get_all.return_value = []
        result = self.controller.remove_food(1)
        self.assertTrue(result)
        self.view.show_message.assert_called_once()
        self.view.reload_data.assert_called_once_with(['foods'])
