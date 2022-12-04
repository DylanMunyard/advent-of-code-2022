def solve():
    a_win = 6
    a_draw = 3
    a_goose_egg = 0

    def paper_weight(hand):
        match hand:
            case 'A' | 'X':
                return 1
            case 'B' | 'Y':
                return 2
            case 'C' | 'Z':
                return 3

    def hand_name(hand):
        match hand:
            case 'A' | 'X':
                return 'Rock'
            case 'B' | 'Y':
                return 'Paper'
            case 'C' | 'Z':
                return 'Scissors'

    def score_hand(hand1, hand2):
        if hand1 == hand2:
            print(f'{hand_name(game[0])} vs {hand_name(game[2])} is a draw')
            return a_draw + hand2
        elif hand2 - hand1 == 1:
            print(f'player2 wins {hand_name(game[0])} vs {hand_name(game[2])}')
            return a_win + hand2
        elif hand2 - hand1 == -2:
            print(f'player2 rock beats scissors {hand_name(game[0])} vs {hand_name(game[2])}')
            return a_win + hand2
        else:
            print(f'player2 loses {hand_name(game[0])} vs {hand_name(game[2])}')
            return a_goose_egg + hand2

    with open('day2/input.txt', 'r') as file:
        their_score = 0  # part 1
        our_score = 0  # part 2

        for line in file:
            game = line.strip()
            # part1
            player1 = paper_weight(game[0])
            player2 = paper_weight(game[2])
            their_score = their_score + score_hand(player1, player2)

            # part2
            outcome = game[2]
            match outcome:
                case 'X':
                    player2 = player1 - 1 if player1 > 1 else 3
                case 'Y':
                    player2 = player1
                case 'Z':
                    player2 = player1 + 1 if player1 < 3 else 1
            our_score = our_score + score_hand(player1, player2)

        print(their_score)
        print(our_score)
