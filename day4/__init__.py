def solve():
    with open('day4/input.txt', 'r') as file:
        fully_contains = 0
        overlaps = 0
        for line in file:
            items = line.strip()
            elf1 = items.split(",")[0].split("-")
            elf2 = items.split(",")[1].split("-")

            if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
                fully_contains = fully_contains + 1

            elif int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1]):
                fully_contains = fully_contains + 1

            if int(elf1[0]) <= int(elf2[0]) <= int(elf1[1]):
                overlaps = overlaps + 1

            elif int(elf2[0]) <= int(elf1[0]) <= int(elf2[1]):
                overlaps = overlaps + 1

        print(fully_contains)
        print(overlaps)
