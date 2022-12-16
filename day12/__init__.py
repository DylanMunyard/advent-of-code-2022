# end = (2, 5)
end = (20, 55)


class Cell:
    def __init__(self, value, initial_steps, visited, x, y):
        self.value = value
        self.steps = initial_steps
        self.path = f'({x},{y})'
        self.visited = visited
        self.x = x
        self.y = y
        self.neighbours = list()

    def elevation(self):
        height = self.value
        if self.value == "S":
            height = "a"
        if self.value == "E":
            height = "z"
        return ord(height)


class QueueItem:
    def __init__(self, value):
        self.value = value


class PriorityQueue:
    queue = list()

    def __init__(self, size):
        self.queue = list(QueueItem for _ in range(size))

    def len(self):
        return len(self.queue)

    def pop(self):
        return self.queue.pop(0)

    def update(self, neighbour):
        """
        Swaps the item in the queue with its priority position (based on #steps)
        :param neighbour: the item to re-prioritise
        :return: None
        """
        item = None
        for i in self.queue:
            if i.value == neighbour:
                item = i
                break

        if item is not None:
            self.queue.remove(item)

        index = 0
        for item in self.queue:
            if item.value.steps > neighbour.steps:
                break
            index = index + 1

        self.queue.insert(index, QueueItem(neighbour))


class Grid:
    heightmap = list()

    def __init__(self, rows, columns):
        self.rows = rows
        self.cols = columns

    def starting_cells(self, target):
        cells = []
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.heightmap[r][c]
                if cell.value == target:
                    cells.append((r, c))
        return cells

    def visit_cells(self, starting_cell, lowest_steps):
        pq = PriorityQueue(self.rows * self.cols)
        pq.queue[0] = QueueItem(self.heightmap[starting_cell[0]][starting_cell[1]])
        i = 1
        for r in range(self.rows):
            for c in range(self.cols):
                if r == starting_cell[0] and c == starting_cell[1]:
                    # starting point
                    continue

                cell = self.heightmap[r][c]
                pq.queue[i] = QueueItem(cell)
                i = i + 1

        while pq.len() > 0:
            item = pq.pop().value
            if item.value == "E":
                break

            if item.steps >= lowest_steps:
                break

            for neighbour in item.neighbours:
                if neighbour.visited:
                    continue

                if neighbour.steps > item.steps + 1:
                    neighbour.path = f'{item.path},({neighbour.x},{neighbour.y})'

                neighbour.steps = min(
                    item.steps + 1,
                    neighbour.steps
                )

                pq.update(neighbour)
            item.visited = True


def calculate_neighbours(self):
    for row in range(self.rows):
        for col in range(self.cols):
            cell = self.heightmap[row][col]
            indices = (row, col + 1), (row, col - 1), (row - 1, col), (row + 1, col)

            for index in indices:
                r = index[0]
                c = index[1]

                if r < 0 or c < 0:
                    continue

                if r > self.rows - 1 or c > self.cols - 1:
                    continue

                # aoc rules:
                # - the elevation of the destination square can be at most one higher
                # - the elevation of the destination square can be much lower than the elevation of your current square.
                neighbour = self.heightmap[r][c]
                if neighbour.elevation() - cell.elevation() > 1:
                    continue

                cell.neighbours.append(neighbour)


def build_grid(heightmap, starting_cell):
    rows = len(heightmap)
    cols = len(heightmap[0].strip())
    initial_steps = rows * cols * 10
    grid = Grid(rows, cols)
    grid.heightmap = list()

    for row in heightmap:
        grid.heightmap.append(list(Cell for _ in row.strip()))

    for r in range(grid.rows):
        for c in range(grid.cols):
            value = heightmap[r][c]

            grid.heightmap[r][c] = Cell(value, initial_steps, False, r, c)

    grid.heightmap[starting_cell[0]][starting_cell[1]].steps = 0
    calculate_neighbours(grid)

    return grid


def solve():
    with open('day12/input.txt', 'r') as file:
        # Similar to https://github.com/DylanMunyard/advent-of-code-2021/blob/main/day15/Cave.go
        inputs = file.readlines()

        sample_grid = build_grid(inputs, (0, 0))
        lowest_steps = sample_grid.rows * sample_grid.cols * 10

        # part 1
        starting_cells = sample_grid.starting_cells("S")
        for starting_cell in starting_cells:
            grid = build_grid(inputs, starting_cell)
            grid.visit_cells(starting_cell, lowest_steps)
            print(f'{grid.heightmap[end[0]][end[1]].value} #steps={grid.heightmap[end[0]][end[1]].steps}, path={grid.heightmap[end[0]][end[1]].path}')

        # part 2
        starting_cells = sample_grid.starting_cells("a")
        steps = []
        for starting_cell in starting_cells[4:]:
            print(len(steps))
            grid = build_grid(inputs, starting_cell)
            grid.visit_cells(starting_cell, lowest_steps)
            if grid.heightmap[end[0]][end[1]].steps < lowest_steps:
                lowest_steps = grid.heightmap[end[0]][end[1]].steps

            steps.append(grid.heightmap[end[0]][end[1]].steps)
        print(sorted(steps)[0])

