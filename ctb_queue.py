from dataclasses import dataclass
from typing import List

from creature import Creature

@dataclass
class CTBQueue:
    participants: List[Creature]
    predicted_queue: List[Creature] = None
    next_attacker: Creature = None


    def __post_init__(self) -> None:
        self.get_queue()
        self.get_next_attacker()


    def get_queue(self) -> None:
        '''Predicts whose turn is next looking 10 turns ahead'''
        queue_members = [{'name': x.name, 'tick': x.tick, 'counter': x.counter, 'creature': x} for x in self.participants]
        predicted_queue = []

        while len(predicted_queue) < 10:
            # next attacker is one with lowest counter
            next_attacker = min(queue_members, key=lambda x: x['counter'])
            next_attacker_index = queue_members.index(next_attacker)

            # reduce all members counter by attacker counter to simulate advancement of time
            # decrement value needs to be assigned to separate value, otherwise it doesn't work
            counter_decrement = next_attacker['counter']
            for member in queue_members:
                member['counter'] -= counter_decrement

            # add attacker tick * 3 (default attack ability rank) to their counter
            # increment value needs to be assigned to separate value, otherwise it doesn't work
            counter_increment = next_attacker['tick'] * 3
            queue_members[next_attacker_index]['counter'] += counter_increment

            predicted_queue.append(next_attacker['creature'])
        
        self.predicted_queue = predicted_queue


    def get_next_attacker(self) -> None:
        self.next_attacker = self.predicted_queue[0]


    def advance_queue(self) -> None:
        '''Modifies the counter of participants based on the current entitiy's action'''
        counter_decrement = self.next_attacker.counter
        # print(counter_decrement)
        for member in self.participants:
            # print(member.name)
            member.counter -= counter_decrement
            # print(member.counter)

        counter_increment = self.next_attacker.tick * 3
        next_attacker_index = self.participants.index(self.next_attacker)
        self.participants[next_attacker_index].counter += counter_increment

        self.get_queue()
        self.get_next_attacker()


    def print_queue(self) -> None:
        for ind, member in enumerate(self.predicted_queue):
            print(f'{ind}: {member.name}')
