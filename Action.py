from ActionType import ActionType
from Player import Player


class Action:
    def __init__(self, name, type, player, stats=None, sub_actions=None):
        self.id = id(self)
        self.name = name
        self.type = type
        self.player = player
        self.stats = stats
        self.sub_actions = sub_actions

    def activate(self):
        if self.type == ActionType.STAT_ACTION:
            if self.stats is not None:
                for key, val in self.stats.items():
                    if key in self.player.stats:
                        if self.player.stats[key] + val < 0:
                            self.player.stats[key] = 0
                        elif self.player.stats[key] + val > self.player.stats_max[key]:
                            self.player.stats[key] = self.player.stats_max[key]
                        else:
                            self.player.stats[key] += val
            return None
        elif self.type == ActionType.SUB_ACTION and self.sub_actions is not None:
            return self.sub_actions


    def __str__(self):
        if self.stats is not None:
            str = f"{self.name} : "
            for key, value in self.stats.items():
                str += f"{key} "
                if value >= 0:
                    str += f"+{value}\n"
                else:
                    str += f"{value}\n"
            return str
