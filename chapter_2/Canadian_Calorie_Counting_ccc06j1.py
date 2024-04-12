
# Canadian Calorie Counting
# Here are the three burger choices:
# 1 – Cheeseburger (461 Calories)
# 2 – Fish Burger (431 Calories)
# 3 – Veggie Burger (420 Calories)
# 4 – no burger
# Here are the three side order choices:
# 1 – Fries (100 Calories)
# 2 – Baked Potato (57 Calories)
# 3 – Chef Salad (70 Calories)
# 4 – no side order
# Here are the three drink choices:
# 1 – Soft Drink (130 Calories)
# 2 – Orange Juice (160 Calories)
# 3 – Milk (118 Calories)
# 4 – no drink
# Here are the three dessert choices:
# 1 – Apple Pie (167 Calories)
# 2 – Sundae (266 Calories)
# 3 – Fruit Cup (75 Calories)
# 4 – no dessert


num_burger = int(input()) # Here are the three burger choices
num_side = int(input()) # Here are the three side order choices
num_drink = int(input()) # Here are the three drink choices
num_dessert = int(input()) # Here are the three dessert choices

if num_burger == 1:
   burger = 461
elif num_burger == 2:
   burger = 431
elif num_burger == 3:
   burger = 420
else:
   burger = 0

if num_side == 1:
   side = 100
elif num_side == 2:
   side = 57
elif num_side == 3:
   side = 70
else:
   side = 0

if num_drink == 1:
   drink = 130
elif num_drink == 2:
   drink = 160
elif num_drink == 3:
   drink = 118
else:
   drink = 0

if num_dessert == 1:
   dessert = 167
elif num_dessert == 2:
   dessert = 266
elif num_dessert == 3:
   dessert = 75
else:
   dessert = 0

total_calories = 'Your total Calorie count is ' + str(burger + side + drink + dessert) + '.'

print(total_calories)

