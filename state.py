from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict

import prompt
from enums import Command

@dataclass
class State(ABC):
    done: bool = False
    quit: bool = False
    next: str = None

    @abstractmethod
    def enter(self):
        ...

    @abstractmethod
    def update(self):
        ...
    
    @abstractmethod
    def exit(self):
        ...

@dataclass
class InitState(State):
    def enter(self) -> None:
        print('entered InitState state')
        # initstate runs once, so set self.done = True immediately on completion
        # of enter()
        self.done = True

    def update(self) -> None:
        pass

    def exit(self) -> None:
        self.next = ChooseCommandState()
        print('exiting InitState state')

@dataclass
class ChooseCommandState(State):
    def enter(self) -> None:
        print('entered ChooseCommandState state')

    def update(self) -> None:
        print('updating ChooseCommandState state')
        commands = [Command.ATTACK, Command.ITEM]
        command_input = prompt.get_command_input(commands)

        match command_input:
            case Command.ATTACK:
                print('attacking enemy...')
                self.done = True
                self.next = ChooseTargetState()
            case Command.ITEM:
                print('using item...')

        # print('0: Do nothing')
        # print('1: Go to ChooseTargetState')
        # print('q: Quit')
        # user_input = input('Choose command:')
        # if user_input == '0':
        #     return
        # elif user_input == '1':
        #     self.done = True
        #     self.next = ChooseTargetState()
        # elif user_input == 'q':
        #     self.done = True
        #     self.quit = True
        # else:
        #     print('not valid input')

        if self.done:
            self.exit()


    def exit(self) -> None:
        print('exiting ChooseCommandState state')

@dataclass
class ChooseTargetState(State):
    def enter(self) -> None:
        print('entered ChooseTargetState state')

    def update(self) -> None:
        print('updating ChooseTargetState state')
        print('0: Do nothing')
        print('1: Go to ChooseCommandState')
        print('q: Quit')
        user_input = input('Choose command:')
        if user_input == '0':
            return
        elif user_input == '1':
            self.done = True
            self.next = ChooseCommandState()
        elif user_input == 'q':
            self.done = True
            self.quit = True
        else:
            print('not valid input')
        if self.done:
            self.exit()

    def exit(self) -> None:
        self.next = ChooseCommandState()
        print('exiting ChooseTargetState state')