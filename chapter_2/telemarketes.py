
# ccc18j1, Telemarketes

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

# номер телемаркетолога: первое число - 8 или 9,
# четвертое - 8 или 9, второе и третье числа индентичны

if ((num1 == 8 or num1 == 9) and
    (num4 == 8 or num4 == 9) and
    (num2 == num3)):
  print('ignore')
else:
  print('answer') 
