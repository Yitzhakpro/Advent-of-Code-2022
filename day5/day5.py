import re
import copy

"""
[S]                 [T] [Q]        
[L]             [B] [M] [P]     [T]
[F]     [S]     [Z] [N] [S]     [R]
[Z] [R] [N]     [R] [D] [F]     [V]
[D] [Z] [H] [J] [W] [G] [W]     [G]
[B] [M] [C] [F] [H] [Z] [N] [R] [L]
[R] [B] [L] [C] [G] [J] [L] [Z] [C]
[H] [T] [Z] [S] [P] [V] [G] [M] [M]
 1   2   3   4   5   6   7   8   9 
"""
def part1(init_stack):
    print('--------------test-----------------')
    for i in init_stack:
        print(i)
    print('--------------test-----------------')

    with open('./input.txt') as f:
        procedures = f.readlines()
    
    for proc in procedures:
        [quantity, from_stack, to_stack] = [int(s) for s in re.findall(r'\b\d+\b', proc)]
        
        tmp_moving = init_stack[from_stack - 1][-quantity::]
        init_stack[from_stack - 1] = init_stack[from_stack - 1][:-quantity]
        init_stack[to_stack - 1] += list(reversed(tmp_moving))

    res = ''
    for stack in init_stack:
        res += stack[-1]

    print(res)


def part2(init_stack):
    print('--------------test-----------------')
    for i in init_stack:
        print(i)
    print('--------------test-----------------')


    with open('./input.txt') as f:
        procedures = f.readlines()
    
    for proc in procedures:
        [quantity, from_stack, to_stack] = [int(s) for s in re.findall(r'\b\d+\b', proc)]
        
        tmp_moving = init_stack[from_stack - 1][-quantity::]
        init_stack[from_stack - 1] = init_stack[from_stack - 1][:-quantity]
        init_stack[to_stack - 1] += tmp_moving

    res = ''
    for stack in init_stack:
        res += stack[-1]

    print(res)


if __name__ == '__main__':
    stacks = [
        ['H', 'R', 'B', 'D', 'Z', 'F', 'L', 'S'],
        ['T', 'B', 'M', 'Z', 'R'],
        ['Z', 'L', 'C', 'H', 'N', 'S'],
        ['S', 'C', 'F', 'J'],
        ['P', 'G', 'H', 'W', 'R', 'Z', 'B'],
        ['V', 'J', 'Z', 'G', 'D', 'N', 'M', 'T'],
        ['G', 'L', 'N', 'W', 'F', 'S', 'P', 'Q'],
        ['M', 'Z', 'R'],
        ['M', 'C', 'L', 'G', 'V', 'R', 'T']
    ]
    stacks_copy = copy.deepcopy(stacks)

    part1(stacks)
    part2(stacks_copy)