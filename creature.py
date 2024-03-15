from dataclasses import dataclass, field
import json


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
    tick: int = field(default=0)
    counter: int = field(default=0)


def load_party_member(name, json_path) -> Creature:
    with open(json_path) as f:
        main_characters = json.load(f)

    party_member = Creature(
        name=main_characters[name]['name'],
        category=main_characters[name]['category'],
        level=main_characters[name]['level'],
        hp=main_characters[name]['hp'],
        hp_max=main_characters[name]['hp_max'],
        strength=main_characters[name]['strength'],
        defense=main_characters[name]['defense'],
        magic=main_characters[name]['magic'],
        magic_defense=main_characters[name]['magic_defense'],
        agility=main_characters[name]['agility'],
        accuracy=main_characters[name]['accuracy'],
        evasion=main_characters[name]['evasion'],
        luck=main_characters[name]['luck'],
    )

    return party_member
