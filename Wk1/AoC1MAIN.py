import argparse
import sys

def process_lines(lines):
    
    position = 50
    zero_count = 0
    N = 100

    for raw in lines:
        line = raw.strip()
        if not line:
            # skip blank lines
            continue

        direction = line[0]
        steps = int(line[1:])

        if direction == 'R':
            total = position + steps
            zero_count += total // N
            position = total % N

        elif direction == 'L':
            # Count how many clicks pass through 0 going left
            if position == 0:
                first = 100
            else:
                first = position

            if steps >= first:
                zero_count += 1 + (steps - first) // 100

            # Update final position
            position = (position - steps) % 100


    return zero_count


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(description='Count how many times the dial lands on 0')
    parser.add_argument('file', nargs='?', default='input',
                        help="path to input file (default: './input')")
    args = parser.parse_args(argv)

    try:
        with open(args.file, 'r', encoding='utf-8') as fh:
            result = process_lines(fh)
    except FileNotFoundError:
        # If the file doesn't exist, try reading from stdin as a fallback
        if args.file == 'input':
            # no default file; read from stdin
            result = process_lines(sys.stdin)
        else:
            raise

    print(result)


if __name__ == '__main__':
    main()