# winning score

apple_3 = int(input())
apple_2 = int(input())
apple_1 = int(input())

banana_3 = int(input())
banana_2 = int(input())
banana_1 = int(input())

apple_total = apple_3 * 3 + apple_2 * 2 + apple_1
banana_total = banana_3 * 3 + banana_2 * 2 + banana_1

if apple_total > banana_total:
   print('A')
elif apple_total < banana_total:
   print('B')
else:
   print('T')