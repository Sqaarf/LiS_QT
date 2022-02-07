from Action import SubAction, StatAction, MoveAction, BackAction
from Zone import Zone


class GameManager:
    def __init__(self, player):
        self.player = player

        self.HOME = Zone("Home")
        self.FOREST = Zone("Forest")
        self.RIVER = Zone("River")
        self.MOUNTAINS = Zone("Mountains")

        self.actions_list = [
            SubAction("Move to a place", self.player, sub_actions=[
                MoveAction("Go to the Home", self.player, self.HOME),
                MoveAction("Go to the Forest", self.player, self.FOREST),
                MoveAction("Go to the River", self.player, self.RIVER),
                MoveAction("Go to the Mountains", self.player, self.MOUNTAINS),
                BackAction(self.player)
            ]),
            StatAction("Eat berries", self.player, {'hunger': -2}),
            StatAction("Drink water", self.player, {'thirst': -2}),
            StatAction("Forage wood", self.player, {'energy': -2}),
            StatAction("Sleep", self.player, {'energy': 5})
        ]

    def addAction(self, a):
        self.actions_list.add(a)

    def removeAction(self, a):
        self.actions_list.remove(a)
