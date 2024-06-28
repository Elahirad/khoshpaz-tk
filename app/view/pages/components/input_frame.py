from customtkinter import CTkFrame, CTkEntry, CTkButton

from app.view.constants import normal_text_font


class InputFrame(CTkFrame):
    def __init__(self, columns, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__columns = columns

        self.grid_columnconfigure(list(range(len(self.__columns) + 1)), weight=1)

        self.__entries: dict[str, CTkEntry] = {}

        for idx, column in enumerate(reversed(self.__columns)):
            self.__entries[column] = CTkEntry(master=self, placeholder_text=column, font=normal_text_font)
            self.__entries[column].grid(row=0, column=idx + 1, padx=5, pady=5)

        self.__add_button = CTkButton(master=self, text="افزودن", command=self.__add_item, font=normal_text_font)
        self.__add_button.grid(row=0, column=0, padx=5, pady=5)

    def __add_item(self) -> None:
        result: dict[str, str] = {}
        for column, entry in self.__entries.items():
            result[column] = entry.get()

        print(result)
