from GameComponents.Inventory import Inventory
from UtilityComponents.Color import Color


class Player():
    def __init__(self, name):
        self.name = name

        self.stats_max = {'hp': 15, 'energy': 20, 'hunger': 20, 'thirst': 15}
        self.stats = {'hp': 15, 'energy': 20, 'hunger': 20, 'thirst': 15}
        self.multipliers = {'mining': 1, 'foraging': 1}

        self.inventory = Inventory()

    def __str__(self):
        str = f"<p>{self.name}("
        for key, value in self.stats.items():
            if key == "hp" or key == "energy":
                if value < self.stats_max[key] // 2:
                    color = Color.RED
                else:
                    color = Color.GREEN
            else:
                if value > self.stats_max[key] // 2:
                    color = Color.RED
                else:
                    color = Color.GREEN
            str += f" {key}:<span id='test' style=\" color:{color.value};\" >{value}</span>"
        return str + " )</p>"
