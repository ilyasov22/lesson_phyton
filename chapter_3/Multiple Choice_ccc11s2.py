# ccc11s2, Multiple Choice
# ввод (N) число - число вопросов студенту
# ввод после вводим букву правильные ответы (A,B,C,D or E)
# ввод после вводим букву какие ответы выбрал студент (A,B,C,D or E)
#
# вывод (C) чило сколько совпало вопросов с правильными ответами студента в вводе

N = int()
Line = int(input())

ask = 0
ans = 0
for i in range(Line,N):
    line = 2*N
    if ask == ans:
        total = total + 1
print(total)

