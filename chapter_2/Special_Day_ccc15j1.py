# If the date occurs before February 18, output the word .
# If the date occurs after February 18, output the word After.
# If the date is February 18, output the word Special.
#
# The first line will contain the month, which will be an integer in the range from
# 1 (indicating January) to
# 12 (indicating December).
#
# The second line will contain the day of the month, which will be an integer in the range from
# 1 to 31
# You can assume that the day of the month will be valid for the given month.

month = int(input())
day = int(input())

if month == 2 and day == 18:
    print('Special')
elif month < 2 or (month == 2 and day < 18):
    print('Before')
elif month > 2 or (month == 2 and day > 18):
    print('After')



