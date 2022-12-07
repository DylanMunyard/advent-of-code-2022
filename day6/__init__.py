def solve():
    with open('day6/input.txt', 'r') as file:
        for line in file:
            sequence = line.strip()

            part1_found = False
            part2_found = False
            for i in range(len(sequence)):
                if not part1_found and len(set(sequence[i:i + 4])) == 4:
                    print(f'{sequence[i:i + 4]} after {i + 4} characters')
                    part1_found = True

                if not part2_found and len(set(sequence[i:i + 14])) == 14:
                    print(f'{sequence[i:i + 14]} after {i + 14} characters')
                    part2_found = True

                if part1_found and part2_found:
                    break
