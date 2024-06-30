from typing import Callable
from .tools import singleton

from app.controller import Controller


@singleton
class Context:
    def __init__(self):
        self._data: dict = {}
        self._callbacks: list[Callable] = []
        self.controller: Controller | None = None

    def add_callback(self, callback: Callable) -> None:
        self._callbacks.append(callback)

    def remove_callback(self, callback: Callable) -> None:
        self._callbacks.remove(callback)

    def bulk_update(self, data: dict):
        for key, value in data.items():
            self._data[key] = value

        self._notify_callbacks()

    def __setitem__(self, key, value):
        self._data[key] = value
        self._notify_callbacks()

    def __getitem__(self, key):
        return self._data[key]

    def _notify_callbacks(self):
        for callback in self._callbacks:
            callback()
