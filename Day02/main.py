import functools

f = open("real.txt", "r")
#f = open("test.txt", "r")
turns = list(map(lambda e: e.split(" "), f.read().split("\n")))
print(turns)
print()

ROCK: str = 'rock'
PAPER = 'paper'
SCISSOR = 'scissor'

score_map = {
    (ROCK, ROCK): 1 + 3,     (ROCK, PAPER): 2 + 6,      (ROCK, SCISSOR): 3 + 0,
    (PAPER, ROCK): 1 + 0,    (PAPER, PAPER): 2 + 3,     (PAPER, SCISSOR): 3 + 6,
    (SCISSOR, ROCK): 1 + 6,  (SCISSOR, PAPER): 2 + 0,   (SCISSOR, SCISSOR): 3 + 3
}

LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

move_map = {
    (ROCK, LOSE): SCISSOR,      (ROCK, DRAW): ROCK,         (ROCK, WIN): PAPER,
    (PAPER, LOSE): ROCK,        (PAPER, DRAW): PAPER,       (PAPER, WIN): SCISSOR,
    (SCISSOR, LOSE): PAPER,     (SCISSOR, DRAW): SCISSOR,   (SCISSOR, WIN): ROCK
}


def calc_score(player_a: str, player_b: str):
    return score_map.get((player_a, player_b))


def calc_score_for_turn(turn):
    player_a = {'A': ROCK, 'B': PAPER, 'C': SCISSOR}.get(turn[0])
    player_b = {'X': ROCK, 'Y': PAPER, 'Z': SCISSOR}.get(turn[1])
    return calc_score(player_a, player_b)


def calc_score_for_turn_partb(turn):
    player_a = {'A': ROCK, 'B': PAPER, 'C': SCISSOR}.get(turn[0])
    player_b = move_map[(player_a, turn[1])]
    return calc_score(player_a, player_b)


score = [calc_score_for_turn_partb(turn) for turn in turns]
print(f'Score is is {sum(score)}')
