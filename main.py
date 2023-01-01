from io.reader import Reader
from model.main_window import MainWindowModel
from registry.category import CategoryRegistry
from util.parser import Parser
from view.main import MainWindow


if __name__ == '__main__':
    res = Reader().read("./config.json")
    categories = Parser().parseJson(res)
    cat_registry = CategoryRegistry(categories)
    mwm = MainWindowModel(cat_registry)

    win = MainWindow(mwm)
    win.mainloop()
