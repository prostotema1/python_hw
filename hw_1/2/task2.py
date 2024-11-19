import sys
from collections import deque


def print_tail_elements(filepath: str):
    try:
        last_lines = deque(maxlen=10)

        with open(filepath, 'r') as file:
            print(f"Parsing file: {filepath}")
            for line in file:
                last_lines.append(line)

        for line in last_lines:
            print(f"{line}",end="")
        print()

    except FileNotFoundError:
        print(f"Файл '{filepath}' не найден.", file=sys.stderr)
        sys.exit(1)


def print_last_stdint():
    print("Parsing stdint")
    last_lines = deque(maxlen=17)
    for line in sys.stdin:
        last_lines.append(line)

    for line in last_lines:
        print(f"{line}",end="")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for file in sys.argv[1:]:
            print_tail_elements(file)
    else:
        print_last_stdint()
