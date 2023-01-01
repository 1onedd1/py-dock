from tkinter import *

from controller.items_window import *


class ItemsWindow(Toplevel):
    items = []

    def __init__(self, **kw):
        super().__init__(**kw)
        self.overrideredirect(1)
        self.bind("<Leave>", leave_app_event)

    def set_items(self, items):
        ItemsWindow.items = []
        # items is array of item class
        self.__init_items__(items)

    def __init_items__(self, items):
        items_counter = 0
        for i in items:
            b = self.__create_item__(i)
            b.grid(column=0, row=items_counter, sticky="ew")
            ItemsWindow.items.append(b)
            items_counter = items_counter + 1

    def __create_item__(self, item):
        b = Button(self)
        b.configure(text=item.title)
        b.bind("<Button-1>", click_item_list_event)
        b.bind("<Enter>", enter_item_list_event)
        b.bind("<Leave>", leave_item_list_event)
        return b

