from tkinter import Button


def enter_item_list_event(event):
    event.widget.configure(bg="gray")


def leave_item_list_event(event):
    event.widget.configure(bg="SystemButtonFace")


def leave_app_event(event):
    self = event.widget
    if type(self) is Button:
        return
    else:
        self.destroy()


def click_item_list_event(event):
    from model.main_window import MainWindowModel
    import os

    button = event.widget
    category = MainWindowModel.cat_registry.active_category
    item = MainWindowModel.cat_registry.get_item_by_name_in_category(button["text"], category)
    os.startfile("%s\\%s" % (item.path, item.file_name))