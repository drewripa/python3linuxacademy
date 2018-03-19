import argparse

parser = argparse.ArgumentParser(description='Printing specific line from specific file. So simple.')
parser.add_argument('filename', help='File for open')
parser.add_argument('--line', '-l', help='Line number for print', type=int)

args = parser.parse_args()

try:
    with open(args.filename) as f:
        print(f.readlines()[args.line-1])
except FileNotFoundError:
    print("File you select not exists")
except IndexError:
    print("File is too short for your index")
