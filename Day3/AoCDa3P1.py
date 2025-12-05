import argparse
import sys

def processInput(lines):
    ans = 0
    for raw in lines:
        best = 0
        line = raw.strip()
        if not line:
            # skip blank lines
            continue
        input = [int(digit) for digit in line if digit.isdigit()]
        n = len(input)
        
        for i in range(n - 1):         # first digit index
            for j in range(i + 1, n):  # second digit index (must be after i)
                val = input[i] * 10 + input[j]
                if val > best:
                    best = val
        ans += best
        print("ans:", ans)

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