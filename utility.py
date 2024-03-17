import csv
import random
from enums import CreatureType

tick_speed_lookup = {}
character_initial_counter = {}
monster_initial_counter = {}


with open('data/tick_speed.csv') as file:
    csv_reader = csv.DictReader(file)
    agility = 0
    for row in csv_reader:
        agi_high = int(row['agi_high'])
        tick_speed = int(row['tick_speed'])

        tick_speed_lookup[agility] = tick_speed

        agility += 1

        while agility <= agi_high:
            tick_speed_lookup[agility] = tick_speed

            agility += 1


with open('data/initial_counter.csv') as file:
    csv_reader = csv.DictReader(file)
    agility = 1
    for row in csv_reader:
        agi_high = int(row['agi_high'])
        char_ic_low = int(row['char_ic_low'])
        char_ic_high = int(row['char_ic_high'])
        monster_ic_low = int(row['monster_ic_low'])
        monster_ic_high = int(row['monster_ic_high'])

        character_initial_counter[agility] = (char_ic_low, char_ic_high)
        monster_initial_counter[agility] = (monster_ic_low, monster_ic_high)

        agility += 1

        while agility <= agi_high:
            character_initial_counter[agility] = (char_ic_low, char_ic_high)
            monster_initial_counter[agility] = (monster_ic_low, monster_ic_high)
            
            agility += 1


def lookup_tick_speed(agility):
    return tick_speed_lookup[agility]


def lookup_initial_counter(agility, category):
    if category == CreatureType.CHARACTER:
        ic_low = character_initial_counter[agility][0]
        ic_high = character_initial_counter[agility][1]
        return random.randint(ic_low, ic_high)
    elif category == CreatureType.MONSTER:
        ic_low = monster_initial_counter[agility][0]
        ic_high = monster_initial_counter[agility][1]
        return random.randint(ic_low, ic_high)
