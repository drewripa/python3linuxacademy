def _readliner():
    flag = False
    text = []
    print("Please enter some text. Empty line for finish.\n")
    while not flag:
        line = input()
        if line:
            text.append(f"{line}\n")
        else:
            flag = True
    return text

def _filewriter(filename, content):
    with open(filename, 'w') as f:
        f.writelines(content)

file_name = input('Please  enter name of our awesome file: ')
_filewriter(file_name, _readliner())

