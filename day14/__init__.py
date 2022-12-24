point = lambda x, y: f'{x},{y}'
get_coord = lambda coord: lambda p: int(p.split(",")[coord])


def get_floor(cave):
    return int(max(cave, key=get_coord(1)).split(",")[1])


def draw(cave, floor):
    left_wall = int(min(cave, key=get_coord(0)).split(",")[0])
    right_wall = int(max(cave, key=get_coord(0)).split(",")[0])

    y = 0
    while y < floor + 1:
        x = left_wall - 10
        line = f"{y} "
        while x <= right_wall + 100:
            line = line + cave[point(x, y)] if point(x, y) in cave else line + "."
            x = x + 1
        print(line)
        y = y + 1


def build_cave():
    with open('day14/input.txt', 'r') as file:
        cave = {}
        for line in file:
            line = line.strip()

            # split our input into (x,y) coordinates
            rock_paths = list(
                map(lambda p: (int(p[0]), int(p[1])),
                    map(lambda coord: coord.split(","), line.split(' -> '))))

            # draw the rock path
            x1, y1 = rock_paths[0]
            for x2, y2 in rock_paths[1:]:
                cave[point(x1, y1)] = "#"
                while not x1 == x2:
                    x1 += 1 if x1 < x2 else -1
                    cave[point(x1, y1)] = "#"

                cave[point(x1, y1)] = "#"
                while not y1 == y2:
                    y1 += 1 if y1 < y2 else -1
                    cave[point(x1, y1)] = "#"

        return cave


def let_the_sand_hit_the_floor(cave, floor):
    y = 0
    x = 500
    sand = 0
    while y < floor:
        # stop this loop when sand comes to a rest
        if not point(x, y + 1) in cave:
            y = y + 1
        elif not point(x - 1, y + 1) in cave:
            y = y + 1
            x = x - 1
        elif not point(x + 1, y + 1) in cave:
            y = y + 1
            x = x + 1
        elif not point(x, y) in cave:
            cave[point(x, y)] = "o"
            y = 0
            x = 500
            sand = sand + 1
        else:
            break

    return sand


def solve():
    cave = build_cave()
    floor = get_floor(cave)
    print(f'part #1 {let_the_sand_hit_the_floor(cave, floor)}')
    draw(cave, floor)

    cave = build_cave()
    left_wall = int(min(cave, key=get_coord(0)).split(",")[0])
    right_wall = int(max(cave, key=get_coord(0)).split(",")[0])
    for x in range(left_wall - 700, right_wall + 700):
        cave[point(x, floor + 2)] = "#"
    print(f'part #2 {let_the_sand_hit_the_floor(cave, floor + 2)}')
    draw(cave, floor + 2)

