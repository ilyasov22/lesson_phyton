# There will be one line of input that contains between 1 and 255  characters.
#
# The output is determined by the following rules:
#
# If the input line does not contain any happy or sad emoticons, output none.
# Otherwise, if the input line contains an equal number of happy and sad emoticons, output unsure.
# Otherwise, if the input line contains more happy than sad emoticons, output happy.
# Otherwise, if the input line contains more sad than happy emoticons, output sad.

line = str(input())

if ':-)' > ':-(':
    print('happy')
elif ':-)' < ':-(':
    print('sad')
elif (not ':-)') and (not ':-('):
    print('none')
elif ':-)' == ':-(':
    print('unsure')