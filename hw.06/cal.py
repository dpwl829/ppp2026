calories = {
    "한라봉": 50,
    "딸기": 34,
    "바나나": 77
}

total = 0

for fruit in calories:
    gram = int(input(f"{fruit} 섭취량(g): "))
    total += (calories[fruit] * gram / 100)

print(f"총 칼로리: {total} kcal")