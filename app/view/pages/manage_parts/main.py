from customtkinter import CTkFrame, CTkLabel, CTkButton

from app.view.constants import normal_text_font
from app.view.pages.components import Table
from app.view.context import Context
from .part_input_form import PartInputForm
from .part_update_form import PartUpdateForm
from .part_delete import PartDelete


class ManageParts(CTkFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__context = Context()
        self.__context.add_callback(self.__update_table)
        self.data = self.__context['parts']

        CTkLabel(
            master=self, text="مدیریت اجزاء غذا", font=("B Koodak Bold", 25)
        ).pack(fill="x", anchor="center", pady=10)

        self.__columns = [('name', 'نام'), ('ingredients', 'مواد اولیه')]

        def show_input_modal():
            self.__input_window = PartInputForm(self.__add_callback)
            self.__input_window.grab_set()

        self.__input_window = None

        self.__update_window = None
        self.__delete_window = None

        self.__add_button_frame = CTkFrame(self, fg_color='transparent')
        self.__add_button_frame.pack(pady=10, padx=10, fill="x")
        self.__add_button = CTkButton(self.__add_button_frame, text='افزودن', font=('B Koodak Bold', 25),
                                      command=show_input_modal)
        self.__add_button.pack()

        self.__table = Table(self.data, self.__columns, master=self, width=self.winfo_width(),
                             height=self.winfo_height(), delete_callback=self.__delete_callback,
                             update_callback=self.__update_callback)
        self.__table.pack(pady=10, padx=10, fill="both", expand=True)

        # Report buttons
        self.__report_frame = CTkFrame(master=self, fg_color='transparent')
        self.__report_frame.pack(pady=10, fill="x")

        self.__report_button1 = CTkButton(master=self.__report_frame, text="۱ گزارش", command=self.__report1,
                                          font=normal_text_font)
        self.__report_button2 = CTkButton(master=self.__report_frame, text="۲ گزارش", command=self.__report2,
                                          font=normal_text_font)
        self.__report_button3 = CTkButton(master=self.__report_frame, text="۳ گزارش", command=self.__report3,
                                          font=normal_text_font)
        self.__report_button1.pack(side="right", padx=5)
        self.__report_button2.pack(side="right", padx=5)
        self.__report_button3.pack(side="right", padx=5)

    def __update_table(self):
        self.data = self.__context['parts']
        self.__table.pack_forget()
        self.__report_frame.pack_forget()
        self.__table = Table(self.data, self.__columns, master=self, width=self.winfo_width(),
                             height=self.winfo_height(), delete_callback=self.__delete_callback,
                             update_callback=self.__update_callback)
        self.__table.pack(pady=10, padx=10, fill="both", expand=True)
        self.__report_frame.pack(pady=10, fill="x")

    def __add_callback(self, name, ingredients):
        self.__context.controller.add_part(name, ingredients)

    def __delete_callback(self, item_id: int):
        def delete(confirmed: bool):
            if confirmed:
                self.__context.controller.remove_part(item_id)

        self.__delete_window = PartDelete(delete)
        self.__delete_window.grab_set()

    def __update_callback(self, item: dict):
        def update(data):
            self.__context.controller.update_part(item['id'], data['name'], data['ingredients'])

        self.__update_window = PartUpdateForm(item, update)
        self.__update_window.grab_set()

    def __report1(self):
        print("۱ گزارش اجرا شد")

    def __report2(self):
        print("۲ گزارش اجرا شد")

    def __report3(self):
        print("۳ گزارش اجرا شد")