def move_tail(tail_pos, head_pos):
    if is_adjacent(tail_pos, head_pos):
        return tail_pos

    new_tail = tail_pos
    vertical_diff = head_pos[0] - tail_pos[0]
    horizontal_diff = head_pos[1] - tail_pos[1]

    if vertical_diff > 0:
        new_tail = (new_tail[0] + 1, new_tail[1])
    elif vertical_diff < 0:
        new_tail = (new_tail[0] - 1, new_tail[1])

    if horizontal_diff > 0:
        new_tail = (new_tail[0], new_tail[1] + 1)
    elif horizontal_diff < 0:
        new_tail = (new_tail[0], new_tail[1] - 1)

    return new_tail


def is_adjacent(tail_pos, head_pos):
    # tail is ...
    # on top of head
    if tail_pos[0] == head_pos[0] and tail_pos[1] == head_pos[1]:
        return True
    # to the left
    if tail_pos[0] == head_pos[0] and tail_pos[1] == head_pos[1] - 1:
        return True
    # to the right
    if tail_pos[0] == head_pos[0] and tail_pos[1] == head_pos[1] + 1:
        return True
    # below
    if tail_pos[0] == head_pos[0] - 1 and tail_pos[1] == head_pos[1]:
        return True
    # above
    if tail_pos[0] == head_pos[0] + 1 and tail_pos[1] == head_pos[1]:
        return True
    # to the bottom left
    if tail_pos[0] == head_pos[0] - 1 and tail_pos[1] == head_pos[1] - 1:
        return True
    # to the bottom right
    if tail_pos[0] == head_pos[0] - 1 and tail_pos[1] == head_pos[1] + 1:
        return True
    # to the top left
    if tail_pos[0] == head_pos[0] + 1 and tail_pos[1] == head_pos[1] - 1:
        return True
    # to the top right
    if tail_pos[0] == head_pos[0] + 1 and tail_pos[1] == head_pos[1] + 1:
        return True

    return False


def solve():

    with open('day9/input.txt', 'r') as file:
        moves = []

        for line in file:
            line = line.strip()
            moves.append(line.split(' '))

        # tail_size = 1  # part 1
        tail_size = 9  # part 2

        tail = [(0, 0) for _ in range(0, tail_size)]
        head_pos = (0, 0)
        tail_tracks = {tail[-1]}  # track where the tail moves

        for move in moves:
            print(f'{move[0]}:{move[1]}')
            for step in range(int(move[1])):
                match move[0]:
                    case 'R':
                        head_pos = (head_pos[0], head_pos[1] + 1)
                    case 'L':
                        head_pos = (head_pos[0], head_pos[1] - 1)
                    case 'U':
                        head_pos = (head_pos[0] + 1, head_pos[1])
                    case 'D':
                        head_pos = (head_pos[0] - 1, head_pos[1])

                tail[0] = move_tail(tail[0], head_pos)
                for knot_index in range(1, len(tail)):
                    tail[knot_index] = move_tail(tail[knot_index], tail[knot_index - 1])
                print(list(reversed(tail)))
                tail_tracks.add(tail[-1])

        print(len(tail_tracks))
