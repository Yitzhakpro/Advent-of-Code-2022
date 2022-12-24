from collections import defaultdict

def part1():
    with open('./input.txt') as f:
        output = f.read().strip()
        lines = [x for x in output.split('\n')]

    SIZE_BY_PATH = defaultdict(int)
    path = []
    for line in lines:
        words = line.strip().split()
        if words[1] == 'cd':
            if words[2] == '..':
                path.pop()
            else:
                path.append(words[2])
        elif words[1] == 'ls':
            continue
        else:
            try:
                size_of_file = int(words[0])
                for i in range(len(path) + 1):
                    SIZE_BY_PATH['/'.join(path[:i])] += size_of_file
            except:
                pass
    
    res = 0
    for path, size in SIZE_BY_PATH.items():
        if size <= 100_000:
            res += size
    print(res)

def part2():
    with open('./input.txt') as f:
        output = f.read().strip()
        lines = [x for x in output.split('\n')]

    SIZE_BY_PATH = defaultdict(int)
    path = []
    for line in lines:
        words = line.strip().split()
        if words[1] == 'cd':
            if words[2] == '..':
                path.pop()
            else:
                path.append(words[2])
        elif words[1] == 'ls':
            continue
        else:
            try:
                size_of_file = int(words[0])
                for i in range(len(path) + 1):
                    SIZE_BY_PATH['/'.join(path[:i])] += size_of_file
            except:
                pass
    
    current_unused = 70_000_000 - SIZE_BY_PATH['/']
    need_to_free = 30_000_000 - current_unused

    best = 1e7
    for path, size in SIZE_BY_PATH.items():
        if size >= need_to_free:
            best = min(best, size)

    print(best)

if __name__ == '__main__':
    part1()
    part2()
