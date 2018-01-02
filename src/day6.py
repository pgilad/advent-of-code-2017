def find_max(memory_banks):
    max_value = max(memory_banks)
    indices = [index for index, value in enumerate(memory_banks) if value == max_value]
    # return the first one
    return indices[0]

def redistribute_blocks(memory_banks, index):
    next_memory_banks = list(memory_banks)
    value = memory_banks[index]
    next_memory_banks[index] = 0
    max_index = len(memory_banks) - 1

    next_index = index
    while value > 0:
        next_index = 0 if next_index + 1 > max_index else next_index + 1
        next_memory_banks[next_index] += 1
        value -= 1

    return next_memory_banks

def has_appeared_before(history, memory_bank):
    for index, past_memory_bank in enumerate(history):
        if past_memory_bank == memory_bank:
            return True, index

    return False, -1


def solve(memory_banks):
    history = []
    steps = 0
    while(True):
        steps += 1
        history.append(memory_banks)
        next_index = find_max(memory_banks)
        next_memory_banks = redistribute_blocks(memory_banks, next_index)

        appeared, index = has_appeared_before(history, next_memory_banks)
        if appeared:
            print next_memory_banks
            return steps, steps - index

        memory_banks = next_memory_banks


def main():
    with open('./day6.txt') as input_file:
        pattern = input_file.read().split('\n')[0]
        memory_banks = pattern.split('\t')
        memory_banks = [int(memory) for memory in memory_banks]
        steps, loop_size = solve(memory_banks)
        print "steps: {}, loop size: {}".format(steps, loop_size)

if __name__ == "__main__":
    main()
