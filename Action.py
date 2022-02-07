import utils
from Player import Player
from abc import ABC, abstractmethod


class Action(ABC):
    def __init__(self, name, player):
        self.id = id(self)
        self.name = name
        self.player = player

    @abstractmethod
    def activate(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class StatAction(Action):
    def __init__(self, name, player, stats):
        super().__init__(name, player)

        if stats is None or len(stats) == 0:
            raise ValueError("stats value in constructor can't be empty or None for type STAT_ACTION")
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
            str = f"{self.name} : "
            for key, value in self.stats.items():
                str += f"{key} "
                if value >= 0:
                    str += f"+{value}\n"
                else:
                    str += f"{value}\n"
            return str


class SubAction(Action):
    def __init__(self, name, player, sub_actions):
        super().__init__(name, player)

        if sub_actions is None or len(sub_actions) == 0:
            raise ValueError("sub_actions value in constructor can't be empty or None for type SUB_ACTION")
        else:
            self.sub_actions = sub_actions

    def activate(self):
        '''
        SubAction activate method is special because the array of sub_actions is returned
        :return: array of sub_actions
        '''
        return self.sub_actions

    def __str__(self):
        return self.name


class MoveAction(Action):
    def __init__(self, name, player, zone):
        super().__init__(name, player)

        if zone is None:
            raise ValueError("zone value in constructor can't be None for type MOVE_ACTION")
        else:
            self.zone = zone

    def activate(self):
        utils.calculateStats(self.player, "energy", -2)
        return None

    def __str__(self):
        return self.name


# class Action:
#     def __init__(self, name, type, player, stats=None, sub_actions=None, zone_to_go=None):
#         self.id = id(self)
#         self.name = name
#         self.type = type
#         self.player = player
#
#         if type == ActionType.STAT_ACTION:
#             if stats is None or len(stats) == 0:
#                 raise ValueError("stats value in constructor can't be empty or None for type STAT_ACTION")
#             else:
#                 self.stats = stats
#         elif type == ActionType.SUB_ACTION:
#             if sub_actions is None or len(sub_actions) == 0:
#                 raise ValueError("sub_actions value in constructor can't be empty or None for type SUB_ACTION")
#             else:
#                 self.sub_actions = sub_actions
#         elif type == ActionType.MOVE_ACTION:
#             if zone_to_go is None:
#                 raise ValueError("zone_to_go value in constructor can't be None for type MOVE_ACTION")
#             else:
#                 self.zone_to_go = zone_to_go
#
#     def activate(self):
#         if self.type == ActionType.STAT_ACTION:
#             for key, val in self.stats.items():
#                 if key in self.player.stats:
#                     if self.player.stats[key] + val < 0:
#                         self.player.stats[key] = 0
#                     elif self.player.stats[key] + val > self.player.stats_max[key]:
#                         self.player.stats[key] = self.player.stats_max[key]
#                     else:
#                         self.player.stats[key] += val
#             return None
#         elif self.type == ActionType.SUB_ACTION:
#             return self.sub_actions
#
#     def __str__(self):
#         if self.stats is not None:
#             str = f"{self.name} : "
#             for key, value in self.stats.items():
#                 str += f"{key} "
#                 if value >= 0:
#                     str += f"+{value}\n"
#                 else:
#                     str += f"{value}\n"
#             return str

class BackAction(Action):
    def __init__(self, player):
        super().__init__(name="Back", player=player)

    def activate(self):
        return None

    def __str__(self):
        return self.name
