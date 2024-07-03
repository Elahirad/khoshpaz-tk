from customtkinter import CTkFrame, CTkLabel, ThemeManager

from app.view.constants import normal_text_font


class SimpleRow(CTkFrame):
    def __init__(self, item: dict, columns: list[tuple[str, str]], *args,
                 **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._columns = columns
        self._data = item

        self.configure(fg_color=ThemeManager.theme['CTk']['fg_color'])
        self.grid_columnconfigure(list(range(0, len(self._columns))), weight=1)

        for colIdx, col in enumerate(reversed(self._columns)):
            if isinstance(self._data[col[0]], list):
                for rowIdx, row in enumerate(self._data[col[0]]):
                    label = CTkLabel(master=self, text=row, font=normal_text_font, anchor='e')
                    label.grid(row=rowIdx, column=colIdx)
            else:
                label = CTkLabel(master=self, text=self._data[col[0]], font=normal_text_font, anchor='e')
                label.grid(row=0, column=colIdx)
