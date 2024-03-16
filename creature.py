from dataclasses import dataclass, field
import json


@dataclass
class Creature:
    name: str
    category: str
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

def load_creature(name, json_path) -> Creature:
    with open(json_path) as f:
        entities = json.load(f)

    entity = Creature(
        name=entities[name]['name'],
        category=entities[name]['category'],
        level=entities[name]['level'],
        hp=entities[name]['hp'],
        hp_max=entities[name]['hp_max'],
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
