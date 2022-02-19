from UtilityComponents import utils
from abc import ABC, abstractmethod


class Action(ABC):
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


class StatAction(Action):
    def __init__(self, name, desc, player, stats):
        super().__init__(name, desc, player)

        if stats is None or len(stats) == 0:
            raise ValueError("stats value in constructor can't be empty or None for Action type StatAction")
        else:
            self.stats = stats

    def activate(self):
        for key, val in self.stats.items():
            if key in self.player.stats:
                utils.calculateStats(self.player, key, val)
                # if self.player.stats[key] + val < 0:
                #     self.player.stats[key] = 0
                # elif self.player.stats[key] + val > self.player.stats_max[key]:
                #     self.player.stats[key] = self.player.stats_max[key]
                # else:
                #     self.player.stats[key] += val
        return None

    def __str__(self):
        if self.stats is not None:
            str = f"{self.desc} : "
            for key, value in self.stats.items():
                str += f"{key} "
                if value >= 0:
                    str += f"+{value}\n"
                else:
                    str += f"{value}\n"
            return str


class SubAction(Action):
    def __init__(self, name, desc, player, sub_actions):
        super().__init__(name, desc, player)

        if sub_actions is None or len(sub_actions) == 0:
            raise ValueError("sub_actions value in constructor can't be empty or None for Action type SubAction")
        else:
            self.sub_actions = sub_actions

    def activate(self):
        '''
        SubAction activate method is special because the array of sub_actions is returned
        :return: array of sub_actions
        '''
        return self.sub_actions

    def __str__(self):
        return self.desc


class MoveAction(Action):
    def __init__(self, name, desc, player, zone):
        super().__init__(name, desc, player)

        if zone is None:
            raise ValueError("zone value in constructor can't be None for Action type MoveAction")
        else:
            self.zone = zone

    def activate(self):
        utils.calculateStats(self.player, "energy", -2)
        return None

    def __str__(self):
        return self.desc


class InventoryAction(Action):
    def __init__(self, name, desc, player, item):
        super().__init__(name, desc, player)

        if item is None:
            raise ValueError("item value in constructor can't be None for Action type InventoryAction")
        else:
            self.item = item

    def activate(self):
        self.player.inventory.addItem(self.item)

    def __str__(self):
        return self.desc


class BackAction(Action):
    def __init__(self, player):
        super().__init__(name="back", desc="Back", player=player)

    def activate(self):
        return None

    def __str__(self):
        return self.desc
