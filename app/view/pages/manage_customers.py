from customtkinter import CTkFrame, CTkLabel


class ManageCustomers(CTkFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        CTkLabel(master=self, text="مدیریت مشتریان", font=("B Koodak Bold", 25)).pack(
            fill="x", anchor="center"
        )
