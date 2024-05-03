# coci18c3p1, Magnus
# в строке надо найти блок со словом HONI и вывести сколько раз это блок попадается в строке

world = input()

block = 0
total = 0

for honi in world:
    if block == 0:
        match = 'H'
    elif block == 1:
        match = 'O'
    elif block == 2:
        match = 'N'
    else:
        match = 'I'
    if match == honi:
        block = block + 1
        if block == 4:
            block = 0
            total = total + 1
print(total)