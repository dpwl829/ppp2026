import csv

def main():
    file = open('weather(146).csv', 'r', encoding='utf-8')
    data = csv.reader(file)

    next(data)

    temp_sum = 0
    temp_count = 0

    rain_sum = 0
    rain_days = 0

    for row in data:
        try:
            temp = float(row[1])
            rain = float(row[2])

            temp_sum += temp
            temp_count += 1

            rain_sum += rain

            if rain >= 5:
                rain_days += 1

        except:
            continue
    file.close()

    avg_temp = temp_sum / temp_count

    print("연 평균 기온:", avg_temp)
    print("5mm 이상 강우일수:", rain_days)
    print("총 강우량:", rain_sum)


if __name__ == "__main__":
    main()