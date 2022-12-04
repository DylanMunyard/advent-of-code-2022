def solve():
    with open('day1/input.txt', 'r') as file:
        cals = []
        calories = 0
        for line in file:
            if line.strip() == "":
                cals.append(calories)
                calories = 0
                continue
            calories = calories + int(line.strip())
        print(max(cals))
        print(sum(sorted(cals)[-3:]))
