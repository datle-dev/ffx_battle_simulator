from dataclasses import dataclass
from functools import reduce
from typing import List

import battle
from creature import Creature
from enums import CreatureType

@dataclass
class Encounter:
    party: List[Creature]
    enemies: List[Creature]


    def __post_init__(self):
        self.init_tick_counter()


    def init_tick_counter(self):
        '''Initialize each party member/enemy's tick and counter'''
        for member in self.party:
            member.tick = battle.get_tick(member.agility)
            member.counter = battle.get_initial_counter(member.agility, member.category)
        for enemy in self.enemies:
            enemy.tick = battle.get_tick(enemy.agility)
            enemy.counter = battle.get_initial_counter(enemy.agility, enemy.category)


    def check_ko(self):
        '''Checks if all members of party or enemies are knocked out'''
        party_ko_status = [x.is_ko for x in self.party]
        enemy_ko_status = [x.is_ko for x in self.enemies]

        is_party_all_ko = bool(reduce(lambda x, y: x*y, party_ko_status))
        is_enemy_all_ko = bool(reduce(lambda x, y: x*y, enemy_ko_status))

        return is_party_all_ko, is_enemy_all_ko


    def get_attacker(self) -> Creature:
        '''Get the current attacker i.e. the creature with the lowest counter'''
        participants = self.party + self.enemies
        attacker = min(participants, key=lambda x: x.counter)
        return attacker
 

    def get_available_targets(self, attacker: Creature) -> List[Creature]:
        '''Get the available targets'''
        if attacker.category == CreatureType.CHARACTER:
            available_targets = [x for x in self.enemies if not x.is_ko]
        else:
            available_targets = [x for x in self.party if not x.is_ko]
        return available_targets


    def advance_counter(self, attacker: Creature, ability_rank: int = 3) -> None:
        '''Advance "time" by decrementing counter'''
        decrement = attacker.counter
        for member in self.party:
            member.counter -= decrement
        for enemy in self.enemies:
            enemy.counter -= decrement
        
        increment = battle.calc_counter(attacker.tick, ability_rank)
        attacker.counter += increment