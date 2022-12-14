SAMPLE = False

class File:
    def __init__(self, parent, name, size):
        self.level = parent.level + 1 if parent else 0
        self.parent = parent
        self.name = name
        self.size = int(size)

    def __str__(self):
        indent = ''
        for _ in range(self.level):
            indent += '  '
        return f'{indent}- {self.name} (file, size={self.size}, parent={self.parent.name})'

class Directory:
    def __init__(self, parent, name):
        self.level = parent.level + 1 if parent else 0
        self.parent = parent
        self.name = name
        self.files = []
        self.directories = []

    def add_file(self, file):
        self.files.append(file)

    def add_directory(self, directory):
        self.directories.append(directory)

    def get_total_size(self):
        total_size = 0
        for file in self.files:
            total_size += file.size
        for directory in self.directories:
            total_size += directory.get_total_size()
        return total_size

    def __str__(self):
        indent = ''
        for _ in range(self.level):
            indent += '  '
        output = f'{indent}- {self.name} (dir, parent={self.parent.name if self.parent else ""})'
        for directory in self.directories:
            output += f'''
{str(directory)})'''
        for file in self.files:
            output += f'''
{str(file)}'''
        return output


with open(f"dec07{'-sample' if SAMPLE else ''}.txt") as file:
    lines = [line.rstrip() for line in file]
    iterator = iter(lines)
    root = Directory(None, '/')
    currentDirectory = root
    try:
        while True:
            line = next(iterator)

            if line.startswith('$'):
                commands = line.split(' ')
                if commands[1] == 'ls':
                    continue
                elif commands[1] == 'cd':
                    if commands[2] == '..':
                        currentDirectory = currentDirectory.parent
                    elif commands[2] == '/':
                        continue
                    else:
                        found = False
                        for directory in currentDirectory.directories:
                            if directory.name == commands[2]:
                                currentDirectory = directory
                                found = True
                                break
                        if not found:
                            raise
                else:
                    raise
            else:
                data = line.split(' ')
                if data[0] == 'dir':
                    currentDirectory.add_directory(Directory(currentDirectory, data[1]))
                else:
                    currentDirectory.add_file(File(currentDirectory, data[1], int(data[0])))

    except StopIteration:
        pass

    # print(root)

    small_size_dirs = []

    def find_small_size_dir(_dir):
        for dir in _dir.directories:
            dir_size = dir.get_total_size()
            if dir_size <= 100000:
                small_size_dirs.append(dir_size)
            find_small_size_dir(dir)

    find_small_size_dir(root)

    print(f'Part One: {sum(small_size_dirs)}')

    total_used = root.get_total_size()
    total_unused = 70000000 - total_used
    target = 30000000 - total_unused

    big_size_dirs = []
    def find_big_size_dir(_dir):
        for dir in _dir.directories:
            dir_size = dir.get_total_size()
            if dir_size >= target:
                big_size_dirs.append(dir_size)
            find_big_size_dir(dir)

    find_big_size_dir(root)

    print(f'Part Two: {min(big_size_dirs)}')
