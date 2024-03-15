from typing import List

from creature import Creature

def get_queue(participants: List[Creature], num_turns: int = 10) -> List[Creature]:
    '''Predicts order of next 10 turns'''
    queue_members = [{'name': x.name, 'tick': x.tick, 'counter': x.counter, 'creature': x} for x in participants]
    predicted_queue = []

    while len(predicted_queue) < num_turns:
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
    
    return predicted_queue