# coci16c1p1, Tarifa
# monthly_mb - колличество мб в тарифном плане
# n - колличество месяцев использования тарифного плана
# excess - излишек мб трафика за месяц

monthly_mb = int(input())
n = int(input())

excess = 0

for i in range(n): # обработка данных за месяц
    used = int(input())
    excess = excess + monthly_mb - used
print(excess + monthly_mb)