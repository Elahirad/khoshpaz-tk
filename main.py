from app import AppView
from app.controller import Controller
from app.model.datastorage import JSONStorage

if __name__ == "__main__":
    app = AppView(controller=None)
    ds = JSONStorage("data.json")
    # ds = CSVStorage('data')
    controller = Controller(view=app, data_storage=ds)
    app.mainloop()
