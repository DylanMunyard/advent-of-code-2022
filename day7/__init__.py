import re
import functools

re_file_output = re.compile(r'(\d+) (.*)')
re_cd_up = re.compile(r'\$ cd \.\.')
re_ls = re.compile(r'\$ ls')
re_cd_down = re.compile(r'\$ cd (\w+)')


def dir_name(directory_stack):
    return functools.reduce(lambda d1, d2: f'{d1}/{d2}' if not d1 == "/" else f'/{d2}', directory_stack)


def dir_size(files):
    size = 0
    for file in files:
        file_listing = re_file_output.findall(file)
        if file_listing:
            size = size + int(file_listing[0][0])
    return size


def solve():
    with open('day7/input.txt', 'r') as file:
        directory_stack = ["/"]
        directories = {}

        line = file.readline()
        while line:
            line = line.strip()
            if re_cd_up.match(line):
                print(f'cd up from {directory_stack.pop()}')
                line = file.readline()
                continue

            elif re_ls.match(line):
                print(f'ls contents of {dir_name(directory_stack)}')
                directories[dir_name(directory_stack)] = list()
                line = file.readline()
                while not line.startswith("$") and line:
                    file_listing = re_file_output.findall(line)
                    if file_listing:
                        print(f'{file_listing[0][1]} ({file_listing[0][0]})')
                        directories[dir_name(directory_stack)].append(line.strip())
                    line = file.readline()
                continue

            elif len(re_cd_down.findall(line)) > 0:
                cd = re_cd_down.findall(line)[0]
                print(f'cd to {cd}')
                directory_stack.append(cd)
                line = file.readline()
                continue

            line = file.readline()

        print(directories)

        # for each directory, sum up the total directory size
        directory_sizes = []
        for root in directories:
            total_size = 0
            for sub_dir in directories:  # todo is there a list comprehension to filter by keys that start with root?
                if not sub_dir.startswith(root):
                    continue
                total_size = total_size + dir_size(directories[sub_dir])
            directory_sizes.append(total_size)

        # part 1
        print(sum(filter(lambda d: d <= 100000, directory_sizes)))

        # part 2
        need_to_free = 30000000 - (70000000 - directory_sizes[0])
        print(min(filter(lambda d: d >= need_to_free, directory_sizes)))
