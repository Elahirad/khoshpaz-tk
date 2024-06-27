from customtkinter import CTkFrame, CTkLabel


class ManageIngredients(CTkFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        CTkLabel(
            master=self, text="مدیریت مواد اولیه", font=("B Koodak Bold", 25)
        ).pack(fill="x", anchor="center")
