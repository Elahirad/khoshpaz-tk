import unittest
from unittest.mock import MagicMock

from app.view.context import Context


class TestContext(unittest.TestCase):

    def setUp(self):
        self.context = Context()
        self.context._data.clear()
        self.context._callbacks.clear()
        self.context.controller = None

    def test_singleton_behavior(self):
        context1 = Context()
        context2 = Context()
        self.assertIs(context1, context2)

    def test_add_callback(self):
        callback = MagicMock()
        self.context.add_callback(callback, 'test_key')
        self.assertIn((callback, 'test_key'), self.context._callbacks)

    def test_bulk_update(self):
        callback = MagicMock()
        self.context.add_callback(callback, 'key1')
        data = {'key1': 'value1', 'key2': 'value2'}
        self.context.bulk_update(data)
        self.assertEqual(self.context._data['key1'], 'value1')
        self.assertEqual(self.context._data['key2'], 'value2')
        callback.assert_called_once()

    def test_setitem(self):
        callback = MagicMock()
        self.context.add_callback(callback, 'key1')
        self.context['key1'] = 'value1'
        self.assertEqual(self.context._data['key1'], 'value1')
        callback.assert_called_once()

    def test_getitem(self):
        self.context._data['key1'] = 'value1'
        self.assertEqual(self.context['key1'], 'value1')

    def test_notify_callbacks(self):
        callback1 = MagicMock()
        callback2 = MagicMock()
        self.context.add_callback(callback1, 'key1')
        self.context.add_callback(callback2, 'key2')
        self.context._notify_callbacks(['key1', 'key2'])
        callback1.assert_called_once()
        callback2.assert_called_once()

    def test_notify_callbacks_with_single_key(self):
        callback = MagicMock()
        self.context.add_callback(callback, 'key1')
        self.context._notify_callbacks('key1')
        callback.assert_called_once()
