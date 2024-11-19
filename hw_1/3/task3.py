import sys


def parse_file(filepath):
    try:
        rows,words,bites = 0,0,0
        with open(filepath, 'r') as file:
            print(f"Parsing file: {filepath}")
            for line in file:
                rows += 1
                words += len(line.split(" "))
                bites += len(line.encode('utf-8'))

        return rows,words,bites

    except FileNotFoundError:
        print(f"Файл '{filepath}' не найден.", file=sys.stderr)
        sys.exit(1)

def parse_stdint():
    rows, words, bites = 0, 0, 0
    for line in sys.stdin:
        rows += 1
        words += len(line.split(" "))
        bites += len(line.encode('utf-8'))
    print(f"\t{rows}\t{words}\t{bites}")

if __name__ == '__main__':
    if len(sys.argv ) > 1:
        total_rows, total_words, total_bites = 0,0,0
        for file in sys.argv[1:]:
            r,w,b = parse_file(file)
            total_bites += b
            total_rows += r
            total_words += w
            print(f"\t{r}\t{w}\t{b}")
        if len(sys.argv[1:]) > 1:
            print(f"Total rows: {total_rows}")
            print(f"Total words: {total_rows}")
            print(f"Total bites: {total_bites}")
    else:
        parse_stdint()