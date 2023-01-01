import json

from model.category import Category
from model.item import Item


class Parser:
    def parseJson(self, json_string):
        out = json.loads(json_string)
        categories_json = out["categories"]
        categories = []
        for c in categories_json:
            items = []
            for item_json in categories_json[c]:
                item = Item()
                item.path = item_json["path"]
                item.file_name = item_json["file_name"]
                item.title = item_json["title"]
                items.append(item)
            category = Category()
            category.title = c
            category.items = items
            categories.append(category)
        return categories
