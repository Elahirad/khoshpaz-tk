import datetime
import unittest
from unittest.mock import MagicMock

from app.controller import Controller
from app.model import IDataStorage, Food, Order, Customer
from app.view import IView


class TestCateringReports(unittest.TestCase):

    def setUp(self):
        self.view = MagicMock(spec=IView)
        self.data_storage = MagicMock(spec=IDataStorage)
        self.controller = Controller(self.view, self.data_storage)

    def test_get_most_purchased_foods(self):
        foods = [Food(id=1, name='پیتزا', price=10.0, parts={}), Food(id=2, name='چلو کباب', price=12.0, parts={})]
        orders = [Order(id=1, customer_id=1, foods={1: 2, 2: 1}, paid_amount=34.0, accept_time='2023-01-01', status=1,
                        preparation_time=30.0)]
        self.data_storage.get_all.side_effect = [foods, orders]
        result = self.controller.get_most_purchased_foods()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], 'پیتزا')
        self.assertEqual(result[0]['count'], 2)

    def test_get_pending_orders(self):
        orders = [Order(id=1, customer_id=1, foods={}, paid_amount=34.0, accept_time='2023-01-01', status=0,
                        preparation_time=30.0)]
        customers = [Customer(id=1, name='محمد', last_name='باقری')]
        self.data_storage.get_all.side_effect = [orders, customers]
        result = self.controller.get_pending_orders()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['customer'], 'محمد باقری')

    def test_get_most_valuable_customers(self):
        customers = [Customer(id=1, name='محمد', last_name='باقری'), Customer(id=2, name='سارا', last_name='موسوی')]
        orders = [Order(id=1, customer_id=1, foods={}, paid_amount=100.0, accept_time='2023-01-01', status=1,
                        preparation_time=30.0),
                  Order(id=2, customer_id=2, foods={}, paid_amount=200.0, accept_time='2023-01-01', status=1,
                        preparation_time=30.0)]
        self.data_storage.get_all.side_effect = [customers, orders]
        result = self.controller.get_most_valuable_customers()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], 'سارا موسوی')
        self.assertEqual(result[0]['paid_amount'], 200.0)

    def test_get_current_month_income(self):
        current_date = datetime.datetime.now()
        accept_time = (current_date - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
        orders = [Order(id=1, customer_id=1, foods={}, paid_amount=100.0, accept_time=accept_time, status=1,
                        preparation_time=30.0),
                  Order(id=2, customer_id=2, foods={}, paid_amount=200.0, accept_time=accept_time, status=1,
                        preparation_time=30.0)]
        self.data_storage.get_all.return_value = orders
        result = self.controller.get_current_month_income()
        self.assertEqual(result, 300.0)
