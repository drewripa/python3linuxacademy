my_file = open('textfile.txt', 'r')

print(my_file.read())

#my_file.close()

my_new_file = open('my_new_file.txt', 'w')
my_file.seek(0)
my_new_file.write(my_file.read())
my_new_file.close()
my_new_file = open('my_new_file.txt', 'r+')
print(my_new_file.read())

with open('my_new_file.txt', 'a') as f:
    f.write('\nHello my text')