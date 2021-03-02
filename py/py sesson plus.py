def calculate(min, max):
    return ((min + max) * (max - min + 1)) / 2

total1 = calculate(1, 3)
total2 = calculate(4, 8)
print(total1)
print(total2)
