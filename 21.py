from collections import defaultdict
from itertools import combinations, product
from math import ceil

weapons = {
    'dagger': {'cost': 8, 'damage': 4},
    'shortsword': {'cost': 10, 'damage': 5},
    'warhammer': {'cost': 25, 'damage': 6},
    'longsword': {'cost': 40, 'damage': 7},
    'greataxe': {'cost': 74, 'damage': 8}
}

armour = {
    'none': {'cost': 0},
    'leather': {'cost': 13, 'armour': 1},
    'chainmail': {'cost': 31, 'armour': 2},
    'splintmail': {'cost': 53, 'armour': 3},
    'bandedmail': {'cost': 75, 'armour': 4},
    'platemail': {'cost': 102, 'armour': 5}
}

rings = {
    'none1': {'cost': 0},
    'none2': {'cost': 0},
    'damage1': {'cost': 25, 'damage': 1},
    'damage2': {'cost': 50, 'damage': 2},
    'damage3': {'cost': 100, 'damage': 3},
    'defense1': {'cost': 20, 'armour': 1},
    'defense2': {'cost': 40, 'armour': 2},
    'defense3': {'cost': 80, 'armour': 3}
}

boss_stats = {
    'hp': 104,
    'damage': 8,
    'armour': 1
}

def get_loadouts():
    return product(weapons.values(), armour.values(), combinations(rings.values(), 2))

def get_stats(loadout):
    weapon, armour, (ring1, ring2) = loadout
    stats = defaultdict(int)
    stats['hp'] = 100
    for part in (weapon, armour, ring1, ring2):
        for k, v in part.items():
            stats[k] += v
    stats['loadout'] = loadout
    return stats

def will_win(my_stats, boss_stats):
    inflicted_dpt = max(1, my_stats['damage'] - boss_stats['armour'])
    received_dpt = max(1, boss_stats['damage'] - my_stats['armour'])
    boss_death_turn = ceil(boss_stats['hp'] / inflicted_dpt)
    my_death_turn = ceil(my_stats['hp'] / received_dpt)
    return my_death_turn >= boss_death_turn

stats = (s for s in (get_stats(l) for l in get_loadouts()) if will_win(s, boss_stats))
print(min(stats, key=lambda s: s['cost']))

stats = (s for s in (get_stats(l) for l in get_loadouts()) if not will_win(s, boss_stats))
print(max(stats, key=lambda s: s['cost']))
