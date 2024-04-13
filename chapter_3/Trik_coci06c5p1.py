# coci06c5p1, Trik

# The first and only line contains a string of at most 50 characters, Borko's moves.
#
# Each of the characters is A, B or C.
#
# Output the index of the cup under which the ball is:
#  1 if it is under the left cup,
#  2 if it is under the middle cup or
#  3 if it is under the right cup.

swaps = input()

ball_location = 1

for swap_type in swaps:
    if swap_type == 'A' and ball_location == 1:
       ball_location = 2
    elif swap_type == 'A' and ball_location == 2:
       ball_location = 1
    elif swap_type == 'B' and ball_location == 2:
       ball_location = 3
    elif swap_type == 'B' and ball_location == 3:
       ball_location = 2
    elif swap_type == 'C' and ball_location == 1:
       ball_location = 3
    elif swap_type == 'C' and ball_location == 3:
       ball_location = 1
print(ball_location)
