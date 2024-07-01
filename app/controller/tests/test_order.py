import unittest
from unittest.mock import MagicMock

from app.controller import Controller
from app.model import IDataStorage, Order, Food, Part, Ingredient, Customer
from app.view import IView


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.view = MagicMock(spec=IView)
        self.data_storage = MagicMock(spec=IDataStorage)
        self.controller = Controller(self.view, self.data_storage)

    def test_get_orders(self):
        order = Order(id=1, customer_id=1, foods={1: 1}, paid_amount=10.0, accept_time='2023-01-01', status=0,
                      preparation_time=30.0)
        food = Food(id=1, name='پیتزا', price=10.0, parts={1: 1})
        part = Part(id=1, name='جزء اول', ingredients={1: 100})
        ingredient = Ingredient(id=1, name='Salt', unit='g')
        self.data_storage.get_all.return_value = [order]
        self.data_storage.get.side_effect = [food, part, ingredient, Customer(id=1, name='محمد', last_name='باقری')]
        orders = self.controller.get_orders()
        self.assertEqual(len(orders), 1)
        self.assertIn('پیتزا', orders[0]['foods'][0])

    def test_add_order(self):
        order = Order(id=1, customer_id=1, foods={1: 1}, paid_amount=10.0, accept_time='2023-01-01', status=0,
                      preparation_time=30.0)
        self.data_storage.add.return_value = order
        result = self.controller.add_order(1, {1: 1}, 10.0, '2023-01-01', 0, 30.0)
        self.assertEqual(result['customer_id'], 1)
        self.view.show_message.assert_called_once()
        self.view.reload_data.assert_called_once_with(['orders'])

    def test_update_order(self):
        order = Order(id=1, customer_id=1, foods={1: 1}, paid_amount=10.0, accept_time='2023-01-01', status=0,
                      preparation_time=30.0)
        self.data_storage.get.return_value = order
        self.data_storage.update.return_value = order
        result = self.controller.update_order(1, 2, {2: 1}, 12.0, '2023-02-01', 1, 40.0)
        self.assertEqual(result['customer_id'], 2)
        self.view.show_message.assert_called_once()
        self.view.reload_data.assert_called_once_with(['orders'])

    def test_remove_order(self):
        order = Order(id=1, customer_id=1, foods={1: 1}, paid_amount=10.0, accept_time='2023-01-01', status=0,
                      preparation_time=30.0)
        self.data_storage.get.return_value = order
        result = self.controller.remove_order(1)
        self.assertTrue(result)
        self.view.show_message.assert_called_once()
        self.view.reload_data.assert_called_once_with(['orders'])
