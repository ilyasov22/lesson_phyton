# ccc11s1, English or French?

# нужно написать программу распознающую текст Англиский язык или Французкий язык
# если колличество букв в тексте t and T больще чем s and S то это English
# если колличество букв в тексте s and S больще чем t and T то это French
# если колличество букв в тексте t and T одинаково s and S то это French

# вывод : English или French

num = int(input())

eng_t = 0
fre_s = 0

for i in range(num):
    text = input()
    fre_s = fre_s + text.count('s') + text.count('S')
    eng_t = eng_t + text.count('t') + text.count('T')
if eng_t > fre_s:
    print('English')
else:
    print('French')

