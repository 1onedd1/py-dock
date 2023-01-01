from view.items import ItemsWindow


def leave_category_event(event):
    event.widget.configure(bg="SystemButtonFace")


def enter_category_event(event):
    button = event.widget
    master = button.master.master
    model = master.model
    button.configure(bg="gray")

    model.cat_registry.active_category = button["text"]
    items = model.cat_registry.get_items_by_category(button["text"])

    if len(model.tks_registry.tks) == 1:
        model.tks_registry.tks[0].destroy()
        model.tks_registry.clear()

    witems = ItemsWindow()
    witems.set_items(items)

    posX = master.winfo_x() + button.master.winfo_x() + button.winfo_x()
    posY = master.winfo_y() + master.winfo_height()
    witems.geometry(f"+{posX}+{posY}")
    model.tks_registry.add(witems)
