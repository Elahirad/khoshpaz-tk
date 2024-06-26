from customtkinter import CTkFrame, CTkLabel


class ManageEcoPacks(CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        CTkLabel(
            master=self, text="مدیریت بسته‌های اقتصادی", font=("B Koodak Bold", 25)
        ).pack(fill="x", anchor="center")
