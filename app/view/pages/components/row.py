from typing import Callable

from customtkinter import CTkFrame, CTkLabel, CTkButton, ThemeManager

from app.view.constants import normal_text_font


class Row(CTkFrame):
    def __init__(self, item: dict, columns: list[tuple[str, str]], delete_callback: Callable,
                 update_callback: Callable,
                 *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._columns = columns
        self._data = item

        self.configure(fg_color=ThemeManager.theme['CTk']['fg_color'])
        self.grid_columnconfigure(list(range(2, len(self._columns) + 2)), weight=2)
        self.grid_columnconfigure((0, 1), weight=1)

        for colIdx, col in enumerate(reversed(self._columns)):
            if isinstance(self._data[col[0]], list):
                for rowIdx, row in enumerate(self._data[col[0]]):
                    label = CTkLabel(master=self, text=row, font=normal_text_font, anchor='e')
                    label.grid(row=rowIdx, column=colIdx + 2)
            else:
                label = CTkLabel(master=self, text=self._data[col[0]], font=normal_text_font, anchor='e')
                label.grid(row=0, column=colIdx + 2)

        delete_button = CTkButton(master=self, text="حذف", command=lambda: delete_callback(self._data['id']),
                                  font=normal_text_font, width=50)
        delete_button.grid(row=0, column=0)
        update_button = CTkButton(master=self, text="ویرایش", command=lambda: update_callback(self._data),
                                  font=normal_text_font, width=50)
        update_button.grid(row=0, column=1)
