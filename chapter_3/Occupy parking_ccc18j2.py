# ccc18j2, Occupy parking
# парковочные места на парковке заняты и свободные
# Вывести колличество парковочный мест, которые были заняты на протяжении обоих дней
# С - занятое парковочное место
# . - свободное парковочное место

# n - число мест парковки
# yesterday - вчера занятые и свободные места порковки
# today - сегодня занятые и свободные места парковки
# occupied - число когда в оба дня парковочное место было занято

n = int(input())
yesterday = input()
today = input()

occupied = 0

for i in range(len(yesterday)):
    if yesterday[i] == 'C' and today[i] == 'C':
        occupied = occupied + 1
print(occupied)