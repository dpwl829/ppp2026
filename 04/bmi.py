bmi = float(input("bmi 값을 입력하세요"))

if 23 <= bmi < 25:
    print("비만 전단계입니다.")
elif 25 <= bmi < 30:
    print("1단계 비만입니다.")
elif 30 <= bmi < 35:
    print("2단계 비만입니다.")
elif bmi >= 35:
    print("3단계 비만입니다.")
else:
    print("정상 또는 저체중입니다.")