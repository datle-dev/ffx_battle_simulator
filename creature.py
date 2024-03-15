from dataclasses import dataclass

@dataclass
class Creature:
    name: str
    category: str
    level: int
    hp: int
    hp_max: int
    strength: int
    defense: int
    magic: int
    magic_defense: int
    agility: int
    accuracy: int
    evasion: int
    luck: int