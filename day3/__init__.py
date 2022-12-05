# 65->90 = A-Z (27-52) diff=38
# 97->122 = a-z (1-26) diff=96
import functools


def solve():
    def ascii_map(a):
        return ord(a)

    with open('day3/input.txt', 'r') as file:
        compartment_priority = list()
        group_priority = list()
        compartments = list()
        group = 0
        for line in file:
            items = line.strip()
            num_of_items = len(items)
            half_way = int(num_of_items / 2)
            compartment_1 = set(map(ascii_map, items[:half_way]))
            compartment_2 = set(map(ascii_map, items[half_way:]))
            compartment_priority += list(compartment_1 & compartment_2)
            compartments.append(set(map(ascii_map, items)))
            group = group + 1
            if group % 3 == 0:
                # find the shared item among a group of three
                group_priority += list(functools.reduce(lambda s1, s2: s1 & s2, compartments))
                compartments.clear()

        # part 1
        print(sum(map(lambda p: p - 38 if 65 <= p <= 90 else p - 96, compartment_priority)))
        # part 2
        print(sum(map(lambda p: p - 38 if 65 <= p <= 90 else p - 96, group_priority)))
