import unittest
from unittest.mock import MagicMock

from app.controller import Controller
from app.model import IDataStorage, IngredientInventoryItem, Ingredient
from app.view import IView


class InventoryTest(unittest.TestCase):
    def setUp(self):
        self.view = MagicMock(spec=IView)
        self.data_storage = MagicMock(spec=IDataStorage)
        self.controller = Controller(self.view, self.data_storage)

    def test_get_inventory_items(self):
        inventory_item = IngredientInventoryItem(id=1, ingredient_id=1, quantity=10.0, price=5.0,
                                                 entrance_date='2023-01-01', manufacture_date='2023-01-01',
                                                 expire_date='2024-01-01')
        ingredient = Ingredient(id=1, name='نمک', unit='گرم')
        self.data_storage.get_all.return_value = [inventory_item]
        self.data_storage.get.return_value = ingredient
        inventory_items = self.controller.get_inventory_items()
        self.assertEqual(len(inventory_items), 1)
        self.assertEqual(inventory_items[0]['ingredient'], 'نمک')

    def test_add_inventory_item(self):
        inventory_item = IngredientInventoryItem(id=1, ingredient_id=1, quantity=10.0, price=5.0,
                                                 entrance_date='2023-01-01', manufacture_date='2023-01-01',
                                                 expire_date='2024-01-01')
        self.data_storage.add.return_value = inventory_item
        result = self.controller.add_inventory_item(1, 10.0, 5.0, '2023-01-01', '2023-01-01', '2024-01-01')
        self.assertEqual(result['quantity'], 10.0)
        self.view.show_message.assert_called_once()
        self.view.reload_data.assert_called_once_with(['inventory'])

    def test_update_inventory_item(self):
        inventory_item = IngredientInventoryItem(id=1, ingredient_id=1, quantity=10.0, price=5.0,
                                                 entrance_date='2023-01-01', manufacture_date='2023-01-01',
                                                 expire_date='2024-01-01')
        self.data_storage.get.return_value = inventory_item
        self.data_storage.update.return_value = inventory_item
        result = self.controller.update_inventory_item(1, 1, 15.0, 7.0, '2023-01-01', '2023-01-01', '2024-01-01')
        self.assertEqual(result['quantity'], 15.0)
        self.view.show_message.assert_called_once()
        self.view.reload_data.assert_called_once_with(['inventory'])

    def test_remove_inventory_item(self):
        inventory_item = IngredientInventoryItem(id=1, ingredient_id=1, quantity=10.0, price=5.0,
                                                 entrance_date='2023-01-01', manufacture_date='2023-01-01',
                                                 expire_date='2024-01-01')
        self.data_storage.get.return_value = inventory_item
        result = self.controller.remove_inventory_item(1)
        self.assertTrue(result)
        self.view.show_message.assert_called_once()
        self.view.reload_data.assert_called_once_with(['inventory'])
