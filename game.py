from dataclasses import dataclass

from data import Data
from encounter import Encounter
from state import State, InitState


@dataclass
class Game():
    state: State = None
    data: Data = None
    encounter: Encounter = None
    done: bool = False

    def __post_init__(self) -> None:
        self.data = Data()
        self.state = InitState()
        self.state.enter()

    def update(self) -> None:
        self.state.update()

        if self.state.quit:
            self.done = True
            return
        
        if self.state.done:
            self.switch_state()

    def switch_state(self) -> None:
        self.state.exit()
        self.state = self.state.next
        self.state.enter()


    def run(self) -> None:
        counter = 0

        print('beginning game...')
        print('entering main loop...')

        while not self.done:
            print(f'main loop iter={counter}')
            
            self.update()

            if self.done:
                print('ending game...')

            counter += 1



if __name__ == '__main__':
    game = Game()
    game.run()
    print('game done!')