from enum import Enum, StrEnum

class Character(StrEnum):
    TIDUS = 'Tidus'
    WAKKA = 'Wakka'
    AURON = 'Auron'
    LULU = 'Lulu'

class CreatureType(StrEnum):
    CHARACTER = 'character'
    MONSTER = 'monster'

class Monster(StrEnum):
    DINGO = 'Dingo'

class Formula(StrEnum):
    STR_VS_DEF = 'str_vs_def'
    STR_IGN_DEF = 'str_ign_def'
    MAG_VS_MDF = 'mag_vs_mdf'
    MAG_IGN_MDF = 'mag_ign_mdf'

class Element(StrEnum):
    FIRE = 'fire'
    LIGHTNING = 'lightning'
    WATER = 'water'
    ICE = 'ice'
    HOLY = 'holy'

class BlackMagic(StrEnum):
    FIRE = 'fire'
    THUNDER = 'thunder'
    WATER = 'water'
    BLIZZARD = 'blizzard'
    FIRA = 'fira'
    THUNDARA = 'thundara'
    WATERA = 'watera'
    BLIZZARA = 'blizzara'

class Command(StrEnum):
    ATTACK = 'attack'
    ITEM = 'item'
    SKILL = 'skill'
    SPECIAL = 'special'
    WHT_MAGIC = 'wht_magic'
    BLK_MAGIC = 'blk_magic'

class Skill(StrEnum):
    DARK_ATTACK = 'dark_attack'
    POWER_BREAK = 'power_break'

class Special(StrEnum):
    CHEER = 'cheer'
    PRAY = 'pray'