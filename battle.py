import math
import random

import utility

def calc_damage_str_vs_def(strength: int, defense: int, power: int = 16, cheer_attacker: int = 0, cheer_defender: int = 0) -> int:
    '''Calculates damage based on attacker strength and defender defense'''
    power_fac = power / 16

    strength_base = math.floor(((strength + cheer_attacker)**3 / 32) + 30)

    defense_eff = max(1, defense)
    defense_mod = 730 - math.floor((defense_eff * 51 - math.floor(defense_eff**2 / 11)) / 10)
    defense_buff_fac = (15 - cheer_defender) / 15
    defense_fac = round(defense_mod / 730 * defense_buff_fac, 3)

    damage_str_vs_def = math.floor(strength_base * defense_fac * power_fac)

    print(f'strength={strength}')
    print(f'defense={defense}')
    print(f'power={power}')
    print(f'cheer atk={cheer_attacker}')
    print(f'cheer def={cheer_defender}')
    print(f'power fac={power_fac}')
    print(f'str base={strength_base}')
    print(f'def eff={defense_eff}')
    print(f'def mod={defense_mod}')
    print(f'def buff fac={defense_buff_fac}')
    print(f'def fac={defense_fac}')
    print(f'damage str vs def ={damage_str_vs_def }')
    
    return damage_str_vs_def


def calc_damage_mag_vs_mdf(magic: int, magic_defense: int, power: int = 12, focus_attacker: int = 0, focus_defender: int = 0):
    '''Calculates damage based on attacker magic and defender magic defense'''
    power_fac = power / 16

    magic_base = math.floor(((magic + focus_attacker)**2 / 6) + power)
    
    mag_defense_eff = max(1, magic_defense)
    mag_defense_mod = 730 - math.floor((mag_defense_eff * 51 - math.floor(mag_defense_eff**2 / 11)) / 10)
    mag_defense_buff_fac = (15 - focus_defender) / 15
    mag_defense_fac = round(mag_defense_mod / 730 * mag_defense_buff_fac, 3)

    damage_mag_vs_mdf = math.floor(magic_base * mag_defense_fac * power_fac * 4)

    print(f'magic={magic}')
    print(f'magic_defense={magic_defense}')
    print(f'power={power}')
    print(f'focus atk={focus_attacker}')
    print(f'focus def={focus_defender}')
    print(f'power fac={power_fac}')
    print(f'mag base={magic_base}')
    print(f'mag def eff={mag_defense_eff}')
    print(f'mag def mod={mag_defense_mod}')
    print(f'mag def buff fac={mag_defense_buff_fac}')
    print(f'mag def fac={mag_defense_fac}')
    print(f'damage mag vs mdf={damage_mag_vs_mdf}')

    return damage_mag_vs_mdf


def vary_damage(damage):
    '''Randomly varies damage by a factor between 93.75% and 105.86%'''
    vary_factor = random.randint(240, 271) / 256
    damage_varied = math.floor(damage * vary_factor)

    print(f'dmg varied={damage_varied}')

    return damage_varied


def calc_accuracy(accuracy: int, evasion: int) -> int:
    '''Calculates accuracy based on attacker accuracy and defender evasion'''
    attacker_acnum = accuracy * 0.4 - evasion + 9

    match attacker_acnum:
        case x if x < 1:
            accuracy = 25
        case x if 1 <= x and x < 3:
            accuracy = 30
        case x if 3 <= x and x < 5:
            accuracy = 40
        case x if 5 <= x and x < 6:
            accuracy = 50
        case x if 6 <= x and x < 7:
            accuracy = 60
        case x if 7 <= x and x < 8:
            accuracy = 80
        case x if x >= 8:
            accuracy = 100

    return accuracy


def calc_hit_chance(accuracy: int, luck_attacker: int, luck_defender: int) -> int:
    '''Calculates chance of a successful hit based on attacker accuracy/luck and defender luck'''
    hit_chance = accuracy + luck_attacker - luck_defender
    return hit_chance


def is_hit(hit_chance: int) -> bool:
    '''Determines whether attack successfully hits'''
    if random.randint(0, 100) < hit_chance:
        return True
    else:
        return False
    
def get_tick(agility: int) -> int:
    '''Gets tick speed for a given agility'''
    tick = utility.lookup_tick_speed(agility)
    return tick


def get_initial_counter(agility: int, category: str) -> int:
    '''Gets initial counter for a given agility and creature category'''
    initial_counter = utility.lookup_initial_counter(agility, category)
    return initial_counter


def calc_counter(tick: int, attack_rank: int = 3, haste_status: float = 1.0) -> None:
    '''Determines the new counter following an attack to determine future turn order'''
    counter = tick * attack_rank * haste_status
    return counter