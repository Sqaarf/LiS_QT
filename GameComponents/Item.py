class Item:
    def __init__(self, name, desc, player):
        self.id = id(self)
        self.name = name
        self.desc = desc
        self.player = player
