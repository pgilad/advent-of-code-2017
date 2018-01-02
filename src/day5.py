def solve():
    with open('./day5.txt') as input_file:
        pattern = input_file.read()
        steps_list = pattern.split('\n')
        steps_list = [int(line) for line in steps_list if line.strip() != ""]
        max_steps = 1000000000
        steps = 0
        current = 0
        limit = len(steps_list) - 1

        while(steps <= max_steps):
            steps += 1
            value = steps_list[current]
            next_index = current + value

            if (next_index > limit or next_index < 0):
                return steps

            steps_list[current] = value + 1
            current = next_index

        return -1


def solve2():
    with open('./day5.txt') as input_file:
        pattern = input_file.read()
        steps_list = pattern.split('\n')
        steps_list = [int(line) for line in steps_list if line.strip() != ""]
        max_steps = 1000000000
        steps = 0
        current = 0
        limit = len(steps_list) - 1

        while(steps <= max_steps):
            steps += 1
            value = steps_list[current]
            next_index = current + value

            if (next_index > limit or next_index < 0):
                return steps

            diff = -1 if value >= 3 else 1
            steps_list[current] = value + diff
            current = next_index

        return -1


if __name__ == "__main__":
    print solve()
    print solve2()
