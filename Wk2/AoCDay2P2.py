import argparse
import sys


def is_invalid_id(n: int) -> bool:
    s = str(n)
    L = len(s)

    for p in range(1, L // 2 + 1):
        if L % p != 0:
            continue  # pattern must tile the full length

        repeats = L // p
        if repeats < 2:
            continue  # must repeat at least twice

        pattern = s[:p]
        if pattern * repeats == s:
            return True

    return False



def processInput(input):
    ans = 0
    line = input.readline().strip()
    for part in line.split(","):
        x_str, y_str = part.split("-")
        x = int(x_str)
        y = int(y_str)

        while x <= y:
            if is_invalid_id(x):
                ans += x
            x += 1

    return ans



def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(description='Add up invalid values')
    parser.add_argument('file', nargs='?', default='input',
                        help="path to input file (default: './input')")
    args = parser.parse_args(argv)

    try:
        with open(args.file, 'r', encoding='utf-8') as fh:
            result = processInput(fh)
    except FileNotFoundError:
        # If the file doesn't exist, try reading from stdin as a fallback
        if args.file == 'input':
            # no default file; read from stdin
            result = processInput(sys.stdin)
        else:
            raise
    print("result:",result)

if __name__ == '__main__':
    main()