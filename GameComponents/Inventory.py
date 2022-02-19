class Inventory:
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, name):
        for item in self.items:
            if name == item.name:
                self.items.remove(item)

