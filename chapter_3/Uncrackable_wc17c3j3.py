# wc17c3j3, Uncrackable

# пароль должен быть между 8 и 12 символов
# не менее 3х нижний регистр
# не менее 2х верхний регистр
# не менее 1 цыфры
# вывод : Valid или Invalid

passw = input()

lower = 0
upper = 0
digit = 0

if 8 <= len(passw) <= 12:
    for login in passw:
        if login.islower():
            lower = lower + 1
        elif login.isupper():
            upper = upper + 1
        elif login.isdigit():
            digit = digit + 1

if upper >= 2 and lower >= 3 and digit >= 1:
   print("Valid")
else:
   print("Invalid")