from typing import Callable

from app.controller import Controller
from .tools import singleton


@singleton
class Context:
    def __init__(self):
        self._data: dict = {}
        self._callbacks: list[tuple[Callable, str]] = []
        self.controller: Controller | None = None

    def add_callback(self, callback: Callable, watch_key: str) -> None:
        self._callbacks.append((callback, watch_key))

    def bulk_update(self, data: dict):
        keys = list(data.keys())
        for key, value in data.items():
            self._data[key] = value

        self._notify_callbacks(keys)

    def __setitem__(self, key, value):
        self._data[key] = value
        self._notify_callbacks(key)

    def __getitem__(self, key):
        return self._data[key]

    def _notify_callbacks(self, keys):
        keys = keys if isinstance(keys, list) else [keys]
        for callback, watch_key in self._callbacks:
            if watch_key in keys:
                callback()
