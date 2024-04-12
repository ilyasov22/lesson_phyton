# dmopc16c1p0, C.C. and Cheese-kun

# C.C. will be absolutely satisfied if the pizza she gets has a width of 3
#  units and an extra-cheesiness of at least 95%
# C.C. will be fairly satisfied if the pizza she gets has a width of 1
#  unit and an extra-cheesiness of at most 50 %
# C.C. will be very satisfied with any other pizza she receives.

# W : (1 <= W <= 3)
# C : (0 <= C <= 100)
# M : C.C. is M satisfied with her pizza.

# w = 3 c >= 95 absolutely
# w = 1 c <= 50 fairly
# (w != 3 and (not c > 95) or (w != 1 and (not c <= 50))   very

w = int(input())
c = int(input())

if w == 3 and c >= 95:
   M = 'absolutely'
elif w == 1 and c <= 50:
   M = 'fairly'
else:
   M = 'very'

print('C.C. is ' + str(M) + ' satisfied with her pizza.')

