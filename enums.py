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