import argparse

parser = argparse.ArgumentParser(description='Serch for words including partial word')
parser.add_argument('snippet', help='string search in words file')

args = parser.parse_args()
snippet = args.snippet.lower()

with open('/usr/share/dicts/words') as f:
    words = f.readlines()

matches = []

for word in words:
    if snippet in word.lower():
        matches.append(word)

print(matches)