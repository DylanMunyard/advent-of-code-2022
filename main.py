import sys

import day1
import day2
import day3
import day4
import day5
import day6

if __name__ == '__main__':
    day = sys.argv[1] if len(sys.argv) >= 2 else '1'
    match day:
        case '1':
            day1.solve()
        case '2':
            day2.solve()
        case '3':
            day3.solve()
        case '4':
            day4.solve()
        case '5':
            day5.solve()
        case '6':
            day6.solve()
        case _:
            print(f'day {day} not solved')

