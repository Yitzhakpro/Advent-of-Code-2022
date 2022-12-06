
def part1():
    with open('./input.txt') as f:
        sections = f.readlines()
    
    count = 0
    for sec in sections:
        [first, second] = sec.split(',')
        [first_start, first_end] = first.split('-')
        [second_start, second_end] = second.split('-')

        if int(first_start) < int(second_start):
            if int(first_end) == 16:
                print(first_end, second_end)
            if int(first_end) >= int(second_end):
                count += 1
        elif int(second_start) < int(first_start):
            if int(second_end) >= int(first_end):
                count += 1
        else:
            count += 1

    print(count)


def part2():
    with open('./input.txt') as f:
        sections = f.readlines()
    
    count = 0
    for sec in sections:
        [first, second] = sec.split(',')
        [first_start, first_end] = first.split('-')
        [second_start, second_end] = second.split('-')

        if int(first_start) == int(second_start) or int(first_end) == int(second_end):
            count += 1
        elif int(second_start) > int(first_start) and int(second_start) <= int(first_end):
            count += 1
        elif int(first_start) > int(second_start) and int(first_start) <= int(second_end):
            count += 1
        # else:
            # print(f'first: {first_start} - {first_end}. second: {second_start} - {second_end}')

    print(count)

if __name__ == '__main__':
    part1()
    part2()
