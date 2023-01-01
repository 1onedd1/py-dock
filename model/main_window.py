from registry.category import CategoryRegistry
from registry.tk import TksRegistry


class MainWindowModel:
    cat_registry = []
    tks_registry = []

    def __init__(self):
        MainWindowModel.cat_registry = CategoryRegistry()
        MainWindowModel.tks_registry = TksRegistry()

    def __init__(self, cat_reg):
        MainWindowModel.cat_registry = cat_reg
        MainWindowModel.tks_registry = TksRegistry()
