from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name, desc, player):
        self.id = id(self)
        self.name = name
        self.desc = desc
        self.player = player

    @abstractmethod
    def activate(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class StatItem(Item):
    def __init__(self, name, desc, player, stats):
        super().__init__(name, desc, player)

        if stats is None or len(stats) == 0:
            raise ValueError("stats value in constructor can't be empty or None for Item type StatItem")
        else:
            self.stats = stats

    def activate(self):
        pass
        # for key, value in self.stats.items():
        #     self.player.stats_max[key]

    def __str__(self):
        return self.desc


class MultItem(Item):
    def __init__(self, name, desc, player, multipliers):
        super().__init__(name, desc, player)

        if multipliers is None or len(multipliers) == 0:
            raise ValueError("multipliers value in constructor can't be empty or None for Item type MultItem")
        else:
            self.multipliers = multipliers

    def activate(self):
        pass

    def __str__(self):
        return self.desc
