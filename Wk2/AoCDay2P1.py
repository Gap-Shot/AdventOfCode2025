import argparse
import sys

def processInput(input):
    ans = 0
    line = input.readline().strip()
    for part in line.split(","):
        x, y = part.split("-")
        x = int(x)
        y = int(y)

        while x <= y:
            chars = list(str(x))
            char1 = ""
            char2 = ""
            size = len(chars)
            if(size%2 == 0):
                for i in range(0, size//2):
                    char1 += chars[i]
                    char2 += chars[i + size//2]
                if(int(char1) == int(char2)):
                    print(char1+char2)
                    ans += int(char1+char2)
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