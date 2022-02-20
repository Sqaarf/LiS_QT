from GameComponents.Action import *
from GameComponents.Item import *
from GameComponents.Zone import *


class GameManager:
    def __init__(self, player):
        self.player = player

        self.HOME = Zone("Home")
        self.FOREST = Zone("Forest")
        self.RIVER = Zone("River")
        self.MOUNTAINS = Zone("Mountains")

        self.default_move_action = SubAction("move", "Move to a place", self.player, sub_actions=[
            MoveAction("move_home", "Go to the Home", self.player, self.HOME),
            MoveAction("move_forest", "Go to the Forest", self.player, self.FOREST),
            MoveAction("move_river", "Go to the River", self.player, self.RIVER),
            MoveAction("move_mountains", "Go to the Mountains", self.player, self.MOUNTAINS),
            BackAction(self.player)
        ])

        self.default_craft_action = SubAction("craft", "Craft an item", self.player, sub_actions=[
            InventoryAction("craft_axe", "Craft an axe", self.player,
                            MultItem("axe", "An axe to chop wood !", self.player, {"mining": 1.5})),
            BackAction(self.player)
        ])

        self.actions_list = [
            self.default_move_action,
            self.default_craft_action,
            StatAction("eat_berries", "Eat berries", self.player, {'hunger': -2}),
            StatAction("drink_water", "Drink water", self.player, {'thirst': -2}),
            StatAction("forage_wood", "Forage wood", self.player, {'energy': -2}),
            StatAction("sleep", "Sleep", self.player, {'energy': 5})
        ]

    def addAction(self, a):
        self.actions_list.add(a)

    def removeAction(self, a):
        self.actions_list.remove(a)
