from typing import Union
from dataclasses import dataclass, field
import json

from enums import Character, Monster, CreatureType

@dataclass
class Creature:
    _name: Union[Character, Monster]
    category: CreatureType
    level: int
    hp: int
    hp_max: int
    mp: int
    mp_max: int
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
    is_ko: bool = False

    # _name is StrEnum, so set use @property and @setter for convenience
    # when printing the name attribute
    @property
    def name(self) -> str:
        return self._name.value
    
    @name.setter
    def name(self, value_as_enum: Character | Monster) -> None:
        self._name = value_as_enum

    def apply_damage(self, damage: int) -> None:
        self.hp -= damage

    def apply_heal(self, heal: int) -> None:
        self.hp += heal

    def update_ko_status(self) -> None:
        if self.hp <= 0:
            self.hp = 0
            self.is_ko = True
        else:
            self.is_ko = False

def load_creature(name: Character | Monster, json_path: str) -> Creature:
    '''Creates Creature object from Character or Monster enum'''
    with open(json_path) as f:
        entities = json.load(f)

    if entities[name]['category'] == CreatureType.CHARACTER:
        entity = Creature(
            _name=Character(entities[name]['name']),
            category=CreatureType(entities[name]['category']),
            level=entities[name]['level'],
            hp=entities[name]['hp'],
            hp_max=entities[name]['hp_max'],
            mp=entities[name]['mp'],
            mp_max=entities[name]['mp_max'],
            strength=entities[name]['strength'],
            defense=entities[name]['defense'],
            magic=entities[name]['magic'],
            magic_defense=entities[name]['magic_defense'],
            agility=entities[name]['agility'],
            accuracy=entities[name]['accuracy'],
            evasion=entities[name]['evasion'],
            luck=entities[name]['luck'],
        )
    elif entities[name]['category'] == CreatureType.MONSTER:
        entity = Creature(
            _name=Monster(entities[name]['name']),
            category=CreatureType(entities[name]['category']),
            level=entities[name]['level'],
            hp=entities[name]['hp'],
            hp_max=entities[name]['hp_max'],
            mp=entities[name]['mp'],
            mp_max=entities[name]['mp_max'],
            strength=entities[name]['strength'],
            defense=entities[name]['defense'],
            magic=entities[name]['magic'],
            magic_defense=entities[name]['magic_defense'],
            agility=entities[name]['agility'],
            accuracy=entities[name]['accuracy'],
            evasion=entities[name]['evasion'],
            luck=entities[name]['luck'],
        )

    return entity