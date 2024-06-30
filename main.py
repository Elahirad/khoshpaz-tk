from app import AppView
from app.model.datastorage import JSONStorage
from app.controller import Controller

if __name__ == "__main__":
    app = AppView(controller=None)
    ds = JSONStorage("data.json")
    controller = Controller(view=app, data_storage=ds)
    app.mainloop()
