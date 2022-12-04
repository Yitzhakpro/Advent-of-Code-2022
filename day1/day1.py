def part1():
    with open('./input.txt') as f:
        calories_input = f.readlines()

    all_invs = []

    tmp_sum = 0
    for row in calories_input:
        if row == '\n':
            all_invs.append(tmp_sum)
            tmp_sum = 0
        else:
            tmp_sum += int(row)
    
    print(max(all_invs))
    

def part2():
    with open('./input.txt') as f:
        calories_input = f.readlines()

    all_invs = []

    tmp_sum = 0
    for row in calories_input:
        if row == '\n':
            all_invs.append(tmp_sum)
            tmp_sum = 0
        else:
            tmp_sum += int(row)
    
    print(sum(sorted(all_invs)[-3::]))

if __name__ == '__main__':
    part1()
    part2()