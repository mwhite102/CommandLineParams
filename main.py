# Usage: python main.py one two three

import sys

def main(argv):
    
    # the first argument is the module name and
    print(f"Module Name: {argv[0]}")

    # print any remaining arguments
    for i, arg in enumerate(argv[1:]):
        print(f"Arg {i}: {arg}")

if __name__ == "__main__":
    main(sys.argv)