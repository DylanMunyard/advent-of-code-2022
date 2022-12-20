import re
from enum import Enum

r_packet_data_match = re.compile(r'(\d+)')


class PacketMatch(Enum):
    Same = 1
    Lower = 2
    Higher = 3


def listify(packet):
    items = []
    i = 0
    while i < len(packet):
        p = packet[i]
        if p == "[":
            num_parsed, list_items = listify(packet[i + 1:])
            items.append(list_items)
            i = num_parsed + i + 1
        elif p == "]":
            i = i + 1
            return i, items
        elif p == "," or p == " ":
            i = i + 1
        else:
            datum = r_packet_data_match.findall(packet[i:])
            if datum:
                items.append(int(datum[0]))
                i = i + len(datum[0])
            else:
                i = i + 1

    return i, items


def comparify(l1, l2):
    print(f'{l1} vs {l2}')

    for index in range(len(l1)):
        if index >= len(l2):
            # If the right list runs out of items first, the inputs are not in the right order.
            print(f'len{l2} < len{l1}')
            return PacketMatch.Higher

        left = l1[index]
        right = l2[index]

        if isinstance(left, int) and isinstance(right, int):
            print(f'int({left}) == int({right})')
            if left > right:
                # If the left integer is higher than the right integer, the inputs are not in the right order
                return PacketMatch.Higher
            if left < right:
                # If the left integer is lower than the right integer, the inputs are in the right order
                return PacketMatch.Lower
            # Otherwise, the inputs are the same integer; continue checking the next part of the input.

        elif isinstance(left, list) and isinstance(right, list):
            print(f'list({left}) == list({right})')
            # both values are lists, compare the first value of each list
            match = comparify(left, right)
            if match == PacketMatch.Same:
                continue
            return match

        elif isinstance(left, list):
            print(f'left list {left} > right scalar {right}')
            match = comparify(left, [right])
            if match == PacketMatch.Same:
                continue
            return match

        else:
            print(f'left scalar {left} > right list {right}')
            match = comparify([left], right)
            if match == PacketMatch.Same:
                continue
            return match

    # If the left list runs out of items first, the inputs are in the right order.
    # If the lists are the same length and no comparison makes a decision about the order,
    # continue checking the next part of the input.
    return PacketMatch.Same if len(l1) == len(l2) else PacketMatch.Lower


def solve():
    with open('day13/input.txt', 'r') as file:
        l1 = file.readline().strip()
        l2 = file.readline().strip()

        pairs = 0
        pair = 1
        while file.readline():
            _, list1 = listify(l1[1:len(l1) - 1])
            _, list2 = listify(l2[1:len(l2) - 1])

            match = comparify(list1, list2)
            pairs = pairs + pair if match == PacketMatch.Lower or match == PacketMatch.Same else pairs
            print(match)

            l1 = file.readline().strip()
            l2 = file.readline().strip()

            pair = pair + 1

        print(f'# pairs = {pairs}')