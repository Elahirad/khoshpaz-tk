from abc import ABC, abstractmethod


class IView(ABC):
    def __init__(self):
        self.controller = None

    @abstractmethod
    def show_message(self, title, message, icon='info'): pass

    @abstractmethod
    def reload_app_data(self): pass

    @abstractmethod
    def reload_data(self, context_indexes: list[str]): pass
