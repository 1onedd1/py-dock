class CategoryRegistry:
    def __init__(self):
        self.categories = []
        self.active_category = ""

    def __init__(self, registry):
        self.categories = registry
        self.active_category = ""

    def get_items_by_category(self, category):
        for c in self.categories:
            if c.title == category:
                return c.items
        return []

    def get_item_by_name_in_category(self, name_item, name_category):
        items = self.get_items_by_category(name_category)
        for i in items:
            if i.title == name_item:
                return i
        return None

