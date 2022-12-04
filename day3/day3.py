
def part1():
    with open('./input.txt') as f:
        rucksacks = f.readlines()
    
    total = 0
    for rucksack in rucksacks:
        striped_rucksack = rucksack.strip()
        first_half = {}
        second_half = {}

        char_found = ''
        for i in range(len(striped_rucksack) // 2):
            j = i + len(striped_rucksack) // 2

            # handle first half
            if striped_rucksack[i] not in first_half:
                first_half[striped_rucksack[i]] = 1
            else:
                first_half[striped_rucksack[i]] += 1
            
            if striped_rucksack[i] in second_half:
                char_found = striped_rucksack[i]
                break

            if striped_rucksack[j] not in second_half:
                second_half[striped_rucksack[j]] = 1
            else:
                second_half[striped_rucksack[j]] += 1
            
            if striped_rucksack[j] in first_half:
                char_found = striped_rucksack[j]
                break
        
        if char_found.islower():
            total += ord(char_found) - 96
        else:
            total += ord(char_found) - 38

    print(total)

def part2():
    with open('./input.txt') as f:
        rucksacks = f.readlines()

    rucksacks_trio = [[rucksacks[i].strip(), rucksacks[i + 1].strip(), rucksacks[i + 2].strip()] for i in range(0, len(rucksacks), 3)]

    total = 0
    for group in rucksacks_trio:
        seen = {}
        for rucksack in group:
            rucksack_seen = {}
            for item in rucksack:
                if item not in rucksack_seen:
                    if item not in seen:
                        seen[item] = 1
                    else:
                        seen[item] += 1
                    
                rucksack_seen[item] = 1

        # getting item that has been seen 3 times
        for item in seen:
            if seen[item] == 3:
                if item.islower():
                    total += ord(item) - 96
                else:
                    total += ord(item) - 38

    print(total)
        

if __name__ == '__main__':
    part1()
    part2()