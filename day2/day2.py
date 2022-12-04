
def getGameResult(op_move, my_mov):
    if op_move == 'A':
        if my_mov == 'X':
            return 'draw'
        elif my_mov == 'Y':
            return 'win'
        else:
            return 'lose'
    if op_move == 'B':
        if my_mov == 'X':
            return 'lose'
        elif my_mov == 'Y':
            return 'draw'
        else:
            return 'win'
    if op_move == 'C':
        if my_mov == 'X':
            return 'win'
        elif my_mov == 'Y':
            return 'lose'
        else:
            return 'draw'

def part1():
    with open('./input.txt') as f:
        strat = f.readlines()
    
    scores = {
        'X': 1,
        'Y': 2,
        'Z': 3,
        'lose': 0,
        'draw': 3,
        'win': 6
    }
    
    score = 0
    for game in strat:
        [op_move, my_mov] = game.strip().split(' ')
        score += scores[my_mov]
        score += scores[getGameResult(op_move, my_mov)]

    print(score)

def gameResultToAction(game_result, op_move):
    if op_move == 'A':
        if game_result == 'X':
            return 'SCISSORS'
        elif game_result == 'Y':
            return 'ROCK'
        else:
            return 'PAPER'
    if op_move == 'B':
        if game_result == 'X':
            return 'ROCK'
        elif game_result == 'Y':
            return 'PAPER'
        else:
            return 'SCISSORS'
    if op_move == 'C':
        if game_result == 'X':
            return 'PAPER'
        elif game_result == 'Y':
            return 'SCISSORS'
        else:
            return 'ROCK'

def part2():
    with open('./input.txt') as f:
        strat = f.readlines()
    
    scores = {
        'ROCK': 1,
        'PAPER': 2,
        'SCISSORS': 3,
        'X': 0,
        'Y': 3,
        'Z': 6
    }
    
    score = 0
    for game in strat:
        [op_move, game_result] = game.strip().split(' ')
        score += scores[gameResultToAction(game_result, op_move)]
        score += scores[game_result]

    print(score)

if __name__ == '__main__':
    part1()
    part2()