from typing import Callable

from customtkinter import CTkFrame, CTkLabel, CTkButton, ThemeManager

from app.view.constants import normal_text_font


class Row(CTkFrame):
    def __init__(self, item, columns, delete_callback: Callable, update_callback: Callable, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__columns = columns
        self.__data = item

        self.configure(fg_color=ThemeManager.theme['CTk']['fg_color'])
        self.grid_columnconfigure(list(range(2, len(self.__columns) + 2)), weight=2)
        self.grid_columnconfigure((0, 1), weight=1)

        for colIdx, col in enumerate(reversed(self.__columns)):
            label = CTkLabel(master=self, text=self.__data[col], font=normal_text_font, anchor='e')
            label.grid(row=0, column=colIdx + 2)

        delete_button = CTkButton(master=self, text="حذف", command=lambda: delete_callback(self.__data['id']),
                                  font=normal_text_font, width=50)
        delete_button.grid(row=0, column=0)
        delete_button = CTkButton(master=self, text="ویرایش", command=lambda: update_callback(self.__data),
                                  font=normal_text_font, width=50)
        delete_button.grid(row=0, column=1)
