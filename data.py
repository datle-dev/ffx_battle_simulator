import csv
import random
from dataclasses import dataclass, field
from typing import Dict

from enums import CreatureType
from constants import PATH_TICK_SPEED, PATH_INITIAL_COUNTER


@dataclass
class Data:
    tick_speed: Dict = field(default_factory=dict)
    initial_counter_character: Dict = field(default_factory=dict)
    initial_counter_monster: Dict = field(default_factory=dict)


    def __post_init__(self) -> None:
        with open(PATH_TICK_SPEED) as file:
            csv_reader = csv.DictReader(file)
            agility = 0
            for row in csv_reader:
                agi_high = int(row['agi_high'])
                tick_speed = int(row['tick_speed'])

                self.tick_speed[agility] = tick_speed

                agility += 1

                while agility <= agi_high:
                    self.tick_speed[agility] = tick_speed

                    agility += 1

        with open(PATH_INITIAL_COUNTER) as file:
            csv_reader = csv.DictReader(file)
            agility = 1
            for row in csv_reader:
                agi_high = int(row['agi_high'])
                char_ic_low = int(row['char_ic_low'])
                char_ic_high = int(row['char_ic_high'])
                monster_ic_low = int(row['monster_ic_low'])
                monster_ic_high = int(row['monster_ic_high'])

                self.initial_counter_character[agility] = (char_ic_low, char_ic_high)
                self.initial_counter_monster[agility] = (monster_ic_low, monster_ic_high)

                agility += 1

                while agility <= agi_high:
                    self.initial_counter_character[agility] = (char_ic_low, char_ic_high)
                    self.initial_counter_monster[agility] = (monster_ic_low, monster_ic_high)
                    
                    agility += 1


    def lookup_tick_speed(self, agility):
        return self.tick_speed[agility]


    def lookup_initial_counter(self, agility, category):
        if category == CreatureType.CHARACTER:
            ic_low = self.initial_counter_character[agility][0]
            ic_high = self.initial_counter_character[agility][1]
            return random.randint(ic_low, ic_high)
        elif category == CreatureType.MONSTER:
            ic_low = self.inital_counter_monster[agility][0]
            ic_high = self.inital_counter_monster[agility][1]
            return random.randint(ic_low, ic_high)
