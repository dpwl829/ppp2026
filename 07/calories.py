calories = {
    "한라봉": 50,
    "딸기": 34,
    "바나나": 77
}

total_calories = 0

while True:
    fruit = input("먹은 과일 이름을 입력하세요 (종료하려면 '끝'): ")

    if fruit == "끝":
        break

    if fruit in calories:
        amount = int(input(f"{fruit}을 몇 g 먹었나요?: "))
        total_calories += calories[fruit] * amount / 100
    else:
        print("해당 과일은 목록에 없습니다.")

print("총 섭취 칼로리:", total_calories, "kcal")