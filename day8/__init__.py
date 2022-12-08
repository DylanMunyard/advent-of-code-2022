def solve():
    with open('day8/input.txt', 'r') as file:
        grid = list()

        def scenic_score(value_row, value_column, moves):
            """
            How many trees up,down,left,right until a taller tree or edge encountered
            :param value_row: the tree's row
            :param value_column: the tree's column
            :param moves: (row,column) position of a taller tree
            :return: the number of trees before a taller tree or the edge encountered
            """
            _, search_row, search_col = moves
            row_trees = abs(value_row - search_row)
            row_columns = abs(value_column - search_col)

            return row_trees + row_columns

        def move(direction, value_row, value_column):
            """
            Move either up, down, left, right looking for a taller tree
            :return: A boolean indicating whether the tree is the tallest, the row containing a taller tree,
            and the column containing a taller tree
            """
            value = grid[value_row][value_column]
            search_row = value_row
            search_column = value_column
            while 0 <= search_row < num_rows and 0 <= search_column < num_cols:
                if (not search_row == value_row or not search_column == value_column) and \
                        value <= grid[search_row][search_column]:
                    return False, search_row, search_column

                match direction:
                    case 'left':
                        search_column = search_column - 1
                    case 'right':
                        search_column = search_column + 1
                    case 'up':
                        search_row = search_row - 1
                    case 'down':
                        search_row = search_row + 1

            return True, max(0, min(search_row, num_rows - 1)), max(0, min(search_column, num_cols - 1))

        for line in file:
            row = line.strip()
            grid.append(list(row))

        num_cols, num_rows = len(grid), len(grid[0])
        num_edges = num_cols * 2 + num_rows * 2 - 4
        print(f'{num_cols}x{num_rows} (edge={num_edges})')

        # go row by row, starting at 1,1
        # from that position go left (col - 1), right (col + 1), up (row - 1) and down (row + 1).
        # if the value of the cell is greater (>) than each item until you reach the edge, it's visible
        # it can't be visible more than once!

        visible = []
        highest_scenic_score = 0
        for row in range(1, num_rows - 1):
            for col in range(1, num_cols - 1):
                left = move('left', row, col)
                up = move('up', row, col)
                down = move('down', row, col)
                right = move('right', row, col)

                if left[0]:
                    visible.append(grid[row][col])
                elif up[0]:
                    visible.append(grid[row][col])
                elif down[0]:
                    visible.append(grid[row][col])
                elif right[0]:
                    visible.append(grid[row][col])

                tree_scenic_score = scenic_score(row, col, up) * scenic_score(row, col, left) * \
                                    scenic_score(row, col, down) * scenic_score(row, col, right)

                highest_scenic_score = tree_scenic_score if highest_scenic_score < tree_scenic_score else highest_scenic_score

        # part 1
        print(len(visible) + num_edges)
        # part 2
        print(highest_scenic_score)
