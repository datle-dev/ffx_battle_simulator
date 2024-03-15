import math
import random

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