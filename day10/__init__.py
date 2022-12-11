import re


def cycles(instruction):
    return 1 if instruction.startswith("noop") else 2


def solve():
    r_add_amount = re.compile(r"addx (-?\d+)")
    signal_amounts = []
    crt = list(list('.' for _ in range(0, 40)) for _ in range(0, 6))
    with open('day10/input.txt', 'r') as file:
        x = 1
        cycle = 1
        instruction = file.readline().strip()
        instruction_cycles = cycles(instruction)
        instruction_ticks = 0
        line = 0
        while True:

            match cycle:
                case 20 | 60 | 100 | 140 | 180 | 220:
                    signal_amounts.append(x * cycle)

            sprite = [pixel for pixel in range(x - 1, x - 1 + 3)]
            crt[line][(cycle - 1) % 40] = "#" if (cycle - 1) % 40 in sprite else ' '

            if cycle % 40 == 0:
                line = line + 1

            cycle = cycle + 1
            instruction_ticks = instruction_ticks + 1

            if instruction_ticks % instruction_cycles == 0:
                addx_instruction = r_add_amount.findall(instruction)
                if addx_instruction:
                    x = x + int(addx_instruction[0])

                instruction = file.readline().strip()
                instruction_cycles = cycles(instruction)
                instruction_ticks = 0

                if instruction == "":
                    break

        # part 1
        print(signal_amounts)
        print(sum(signal_amounts))

        # part 2
        for line in crt:
            print(''.join(pixel for pixel in line))
