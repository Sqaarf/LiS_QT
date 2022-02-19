def calculateStats(player, key, val):
    if player.stats[key] + val < 0:
        player.stats[key] = 0
    elif player.stats[key] + val > player.stats_max[key]:
        player.stats[key] = player.stats_max[key]
    else:
        player.stats[key] += val


def findAction(desc, arr):
    for a in arr:
        if desc == a.desc:
            return a
