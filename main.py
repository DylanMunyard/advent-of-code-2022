import sys

import day1
import day2
import day3
import day4
import day5
import day6
import day7
import day8
import day9
import day10
import day11
import day12
import day13
import day14

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
        case '7':
            day7.solve()
        case '8':
            day8.solve()
        case '9':
            day9.solve()
        case '10':
            day10.solve()
        case '11':
            day11.solve()
        case '12':
            day12.solve()
        case '13':
            day13.solve()
        case '14':
            day14.solve()
        case _:
            print(f'day {day} not solved')

