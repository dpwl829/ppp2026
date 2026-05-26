import csv
import os
import csv


filename = "weather_146_2023.csv"


if not os.path.exists(filename):

    url = "https://api.taegon.kr/stations/146/?sy=2023&ey=2023&format=csv"

    response = requests.get(url)
    response.encoding = "utf-8"

    with open(filename, "w", encoding="utf-8-sig") as f:
        f.write(response.text)


temp_sum = 0
temp_count = 0

rain_days = 0
rain_sum = 0


with open(filename, encoding="utf-8-sig") as f:

    data = csv.reader(f)
    next(data)

    for row in data:

        temp = row[4]
        rain = row[7]


        if temp != "":
            temp = float(temp)

            temp_sum += temp
            temp_count += 1


        if rain != "":
            rain = float(rain)

            rain_sum += rain


            if rain >= 5:
                rain_days += 1


avg_temp = temp_sum / temp_count


with open("result.txt", "w", encoding="utf-8") as out:

    out.write(f"1. 연 평균 기온 : {avg_temp:.2f}℃\n")
    out.write(f"2. 5mm 이상 강우일수 : {rain_days}일\n")
    out.write(f"3. 총 강우량 : {rain_sum:.1f}mm\n")

print("result.txt 파일 저장 완료")

