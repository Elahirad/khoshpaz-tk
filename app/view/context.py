from typing import Callable
from .tools import singleton

from app.controller import Controller


@singleton
class Context:
    def __init__(self):
        self.__data: dict = {}
        self.__callbacks: list[Callable] = []
        self.controller: Controller | None = None

    def add_callback(self, callback: Callable) -> None:
        self.__callbacks.append(callback)

    def remove_callback(self, callback: Callable) -> None:
        self.__callbacks.remove(callback)

    def __setitem__(self, key, value):
        self.__data[key] = value
        self.__notify_callbacks()

    def __getitem__(self, key):
        return self.__data[key]

    def __notify_callbacks(self):
        for callback in self.__callbacks:
            callback()
