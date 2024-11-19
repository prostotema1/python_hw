import sys

def read_from_file(filepath: str):
    line_counter = 1
    try:
        with open(filepath, 'r') as f:
            for line in f:
                print(f"\t{line_counter} {line}")
                line_counter += 1
            print(f"\t{line_counter} ")
    except FileNotFoundError:
        print(f"Файл '{filepath}' не найден.", file=sys.stderr)
        sys.exit(1)


def read_from_stream(input_stream):
    line_counter = 1
    for line in input_stream:
        print(f"\t{line_counter} {line.rstrip()}")
        line_counter += 1
    print(f"\t{line_counter} ")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        read_from_file(sys.argv[1])
    else:
        read_from_stream(sys.stdin)