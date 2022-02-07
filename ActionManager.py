from Action import Action
from ActionType import ActionType


class ActionManager:
    def __init__(self, player):
        self.player = player
        self.actions_list = [
            Action("Move to a place", ActionType.SUB_ACTION, self.player),
            Action("Eat berries", ActionType.STAT_ACTION, self.player, {'hunger': -2}),
            Action("Drink water", ActionType.STAT_ACTION, self.player, {'thirst': -2}),
            Action("Forage wood", ActionType.STAT_ACTION, self.player, {'energy': -2}),
            Action("Sleep", ActionType.STAT_ACTION, self.player, {'energy': 5})
        ]

    def add(self, a):
        self.actions_list.add(a)

    def remove(self, a):
        self.actions_list.remove(a)

    def findByName(self, name):
        for a in self.actions_list:
            if name == a.name:
                return a
