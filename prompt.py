from typing import List

from enums import Command
from creature import Creature


def get_command_input(commands: List[Command]) -> Command:
    for ind, command in enumerate(commands):
        print(f'({ind}): {command.value.capitalize()}')
    
    user_input = input(f'Choose a command: ')

    while user_input not in [x.value for x in commands]:
        print('invalid user input!')
        user_input = input(f'Choose a command: ')

    return Command(user_input)


def get_target_input(targets: List[Creature]) -> Creature:
    for ind, target in enumerate(targets):
        print(f'({ind}): {target.name}')

    user_input = input(f'Choose a target: ')

    while user_input not in [x.name for x in targets]:
        print('invalid user input!')
        user_input = input(f'Choose a target: ')

    user_index = [ind for ind, x in enumerate(targets) if x.name == user_input][0]

    return targets[user_index]
