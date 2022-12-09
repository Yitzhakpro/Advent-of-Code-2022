
def part1():
    with open('./input.txt') as f:
        seq = f.read()

    first = -1

    for i in range(len(seq)):
        if len(seq) - i == 4:
            first = len(seq) + 1
            break
        
        seen = [seq[i]]

        valid = True
        for j in range(1, 3):
            if seq[i + j] not in seen:
                seen.append(seq[i + j])
            else:
                valid = False

        if not valid:
            continue

        if seq[i + 3] not in seen:
            first = i + 3 + 1
            break          
        else:
            continue


    print(first)

def part2():
    with open('./input.txt') as f:
        seq = f.read()
    
    first = -1

    for i in range(len(seq)):
        if len(seq) - i == 14:
            first = len(seq) + 1
            break
        
        seen = [seq[i]]

        valid = True
        for j in range(1, 13):
            if seq[i + j] not in seen:
                seen.append(seq[i + j])
            else:
                valid = False

        if not valid:
            continue

        if seq[i + 13] not in seen:
            first = i + 13 + 1
            break
        else:
            continue


    print(first)


if __name__ == '__main__':
    part1()
    part2()

