print("변환 종류를 선택하세요")
print("1. 화씨 -> 섭씨")
print("2. 섭씨 -> 화씨")
print("3. 피트(ft) -> cm")
print("4. cm -> 피트(ft)")

choice = int(input("선택 (1~4): "))

value = float(input("값을 입력하세요: "))

if choice == 1:
    result = (value - 32) * 5 / 9
    print("섭씨 온도: {:.1f}".format(result))

elif choice == 2:
    result = value * 9 / 5 + 32
    print("화씨 온도: {:.1f}".format(result))

elif choice == 3:
    result = value * 30.48
    print("길이(cm): {:.1f}".format(result))

elif choice == 4:
    result = value / 30.48
    print("길이(ft): {:.1f}".format(result))

else:
    print("잘못된 선택입니다.")