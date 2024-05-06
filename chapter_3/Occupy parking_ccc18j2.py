# парковочные места на парковке заняты и свободные
# Вывести колличество парковочный мест, которые были заняты на протяжении обоих дней
# С - занятое парковочное место
# . - свободное парковочное место

n = int(input())
yesterday = input()
today = input()

occupied = 0

for i in range(len(yesterday)):
    if yesterday[i] == 'C' and today[i] == 'C':
        occupied = occupied + 1
print(occupied)