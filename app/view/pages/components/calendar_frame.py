from typing import Callable
import datetime

from customtkinter import CTkButton, CTkToplevel
from tkcalendar import Calendar

from app.view.constants import normal_text_font


class CalendarFrame(CTkToplevel):
    def __init__(self, callback: Callable, default_date: datetime.date = datetime.date.today(), master=None, *args,
                 **kwargs) -> None:
        super().__init__(master=master, *args, **kwargs)
        self.resizable(False, False)
        self.geometry("400x300")

        self._callback = callback
        self._cal = Calendar(self, selectmode='day', year=default_date.year,
                             month=default_date.month, day=default_date.day)
        self._cal.pack(pady=20)
        self._btn = CTkButton(self, text='ثبت', font=normal_text_font, command=self._submit)
        self._btn.pack()

    def _submit(self) -> None:
        date = self._cal.selection_get()
        self._callback(date)
        self.destroy()
