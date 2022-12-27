import functools
import re


def phat_stacks(num_stacks, row_of_crates):
    """
    Assign each crate to a stack
    """
    stacks = list()
    for i in range(num_stacks):
        stacks.append(row_of_crates[i * 3 + i:i * 3 + i + 3])
    return stacks


def instruction(move):
    """
    Extract how many crates to move between stacks
    """
    r_match = re.compile(r'(\d+)')
    # move 11 from 3 to 8 => (11,3,8)
    return list(map(lambda d: int(d), r_match.findall(move)))


def solve():
    with open('day5/sample.txt', 'r') as file:
        crate_input = list()
        moves = list()
        is_crane_instruction = False
        # step 1: parse our input into rows of crates and instructions
        for line in file:
            line = line.replace("\r\n", "").replace("\n", "")
            if line == "":
                continue

            if not is_crane_instruction and line.startswith("move"):
                is_crane_instruction = True

            if not is_crane_instruction:
                crate_input.append(line)
            else:
                moves.append(line)

        # step 2: assign crates to their stack, in their stacked order (0: top, len-1: bottom)
        num_stacks = crate_input[len(crate_input) - 2].count("[")
        stacks = {k: list() for k in range(num_stacks)}
        for row_of_crates in crate_input[:-1]:
            crates = phat_stacks(num_stacks, row_of_crates)
            print(crates)
            for stack in range(len(crates)):
                crate = crates[stack]
                if not crate.strip() == "":
                    stacks[stack].append(crate)

        # step 3: execute each move
        for move in moves:
            instructions = instruction(move)
            how_many = instructions[0]
            from_stack = instructions[1] - 1
            to_stack = instructions[2] - 1
            print(f'move {stacks[from_stack][0:how_many]} to stack {to_stack}')
            # part 1:
            # crates_to_move = list(reversed(stacks[from_stack][0:how_many]))
            # part 2:
            crates_to_move = stacks[from_stack][0:how_many]
            crates_to_move.extend(stacks[to_stack])
            stacks[to_stack] = crates_to_move
            del stacks[from_stack][0:how_many]
            for s in stacks:
                print(f'{s} => {stacks[s]}')
            print("")

        solution = ""
        for s in stacks:
            solution = solution + stacks[s][0]

        print(solution.replace("[", "").replace("]", ""))
