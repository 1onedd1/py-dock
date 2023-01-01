from tkinter import *
from controller.main_window import *


class MainWindow(Tk):
    def __init__(self, model):
        super().__init__(className='Drag and drop icon')
        self.model = model
        self.geometry('+%d+%d' % (self.winfo_screenwidth()/2, self.winfo_screenheight()/2))
        self.overrideredirect(1)
        self.__frame__ = Frame()
        self.__init_categories__()

    def __init_categories__(self):
        columns_counter = 0
        for cat in self.model.cat_registry.categories:
            items = []
            for i in cat.items:
                items.append(i.title)
            b = self.__create_category__(cat)
            b.grid(column=columns_counter, row=0)
            columns_counter = columns_counter + 1
        self.__frame__.pack()

    def __create_category__(self, item):
        b = Button(self.__frame__)
        b.configure(text=item.title, state="disabled")
        b.bind("<Enter>", enter_category_event)
        b.bind("<Leave>", leave_category_event)
        return b
