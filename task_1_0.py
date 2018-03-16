def _printer(message, count):
    for iteration in range(count):
        print(message)


message = input("Please enter message to echo: ")
count = input("Please enter repeat count: ")

if count:
    count = int(count)
else:
    count = 1
_printer(message,count)

