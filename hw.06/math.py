import math

for i in range(0, 91, 10):
    rad = math.radians(i)
    print(f"{i}도 → sin: {math.sin(rad):.2f}, cos: {math.cos(rad):.2f}")