def calculateStats(player, key, val):
    if player.stats[key] + val < 0:
        player.stats[key] = 0
    elif player.stats[key] + val > player.stats_max[key]:
        player.stats[key] = player.stats_max[key]
    else:
        player.stats[key] += val


def findActionByName(name, arr):
    for a in arr:
        if name == a.name:
            return a
