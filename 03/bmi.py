height = float(input("키를 입력하세요=>"))
weight = float(input("몸무게를 입력하세요=>"))

height_m = height/100
#bmi = 55(kg) / 169(m)^2
bmi= weight/(height_m*height_m)

print(bmi)
