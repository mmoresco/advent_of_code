from util import *
from enum import Enum

Choice = Enum('Choice', ['ROCK', 'PAPER', 'SCISSOR'])
Outcome = Enum('Outcome', ['WIN', 'TIE', 'LOSS'])
a_to_choice = {
        'A': Choice.ROCK,
        'B': Choice.PAPER,
        'C': Choice.SCISSOR
        }

x_to_choice = {
        'X': Choice.ROCK,
        'Y': Choice.PAPER,
        'Z': Choice.SCISSOR
        }

x_to_outcome = {
        'X': Outcome.LOSS,
        'Y': Outcome.TIE,
        'Z': Outcome.WIN
        }

choice_score = {
        Choice.ROCK: 1,
        Choice.PAPER: 2,
        Choice.SCISSOR: 3
        }

outcome_score = {
        Outcome.WIN: 6,
        Outcome.TIE: 3,
        Outcome.LOSS: 0
        }

beats = {
        Choice.PAPER: Choice.ROCK,
        Choice.ROCK: Choice.SCISSOR,
        Choice.SCISSOR: Choice.PAPER
        }

loses = dict((reversed(item) for item in beats.items()))

def outcome(theirs, mine):
    if theirs == mine:
        return Outcome.TIE

    if beats[theirs] == mine:
        return Outcome.LOSS

    return Outcome.WIN

def determine_choice(theirs, outcome):
    if outcome == Outcome.TIE:
        return theirs

    if outcome == Outcome.WIN:
        return loses[theirs]

    return beats[theirs]

def score_round(theirs, mine=None, result=None):
    if mine:
        result = outcome(theirs, mine)
    else:
        mine = determine_choice(theirs, result)

    return choice_score[mine] + outcome_score[result]

def decrypt_round(theirs, mine):
    return a_to_choice[theirs], x_to_choice[mine], None

def decrypt_round_correctly(theirs, outcome):
    return a_to_choice[theirs], None, x_to_outcome[outcome]

def score(rounds, decrypter):
    return sum([score_round(*decrypter(first, second)) for first, second in rounds])

def parse(lines):
    return [line.strip().split(' ') for line in lines]

test_input = ["A Y", "B X", "C Z"]

# PART 1
test_rounds = parse(test_input)
assert score(test_rounds, decrypt_round) == 15

rounds = parse(Input(2))
print ("Part 1:", score(rounds, decrypt_round))

# PART 2
assert score(test_rounds, decrypt_round_correctly) == 12
print ("Part 2:", score(rounds, decrypt_round_correctly))
