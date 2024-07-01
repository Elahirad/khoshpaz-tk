import unittest
from unittest.mock import MagicMock

from app.controller import Controller
from app.model import IDataStorage, Customer
from app.view import IView


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.view = MagicMock(spec=IView)
        self.data_storage = MagicMock(spec=IDataStorage)
        self.controller = Controller(self.view, self.data_storage)

    def test_get_customers(self):
        customer = Customer(id=1, name='محمد', last_name='باقری')
        self.data_storage.get_all.return_value = [customer]
        customers = self.controller.get_customers()
        self.assertEqual(len(customers), 1)
        self.assertEqual(customers[0]['name'], 'محمد')

    def test_add_customer(self):
        customer = Customer(id=1, name='محمد', last_name='باقری')
        self.data_storage.add.return_value = customer
        result = self.controller.add_customer('محمد', 'باقری')
        self.assertEqual(result['name'], 'محمد')
        self.view.show_message.assert_called_once()
        self.view.reload_data.assert_called_once_with(['customers'])

    def test_update_customer(self):
        customer = Customer(id=1, name='محمد', last_name='باقری')
        self.data_storage.get.return_value = customer
        self.data_storage.update.return_value = customer
        result = self.controller.update_customer(1, 'سارا', 'باقری')
        self.assertEqual(result['name'], 'سارا')
        self.view.show_message.assert_called_once()
        self.view.reload_data.assert_called_once_with(['customers'])

    def test_remove_customer(self):
        customer = Customer(id=1, name='محمد', last_name='باقری')
        self.data_storage.get.return_value = customer
        self.data_storage.get_all.return_value = []
        result = self.controller.remove_customer(1)
        self.assertTrue(result)
        self.view.show_message.assert_called_once()
        self.view.reload_data.assert_called_once_with(['customers'])
