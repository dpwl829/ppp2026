import csv


def load_weather(filename):

    dates = []
    tmax = []
    tmin = []
    tavg = []

    with open(filename, encoding='cp949') as f:

        data = csv.reader(f)

        next(data)

        for row in data:

            try:
                date = row[0]

                avg_temp = float(row[2])

                max_temp = float(row[3])

                min_temp = float(row[4])

                dates.append(date)

                tavg.append(avg_temp)

                tmax.append(max_temp)

                tmin.append(min_temp)

            except:
                continue

    return dates, tmax, tmin, tavg



def yearly_max_gap(dates, tmax, tmin):

    result = {}

    for i in range(len(dates)):

        year = dates[i].split('-')[0]

        gap = tmax[i] - tmin[i]

        if year not in result:

            result[year] = [dates[i], gap]

        else:

            if gap > result[year][1]:

                result[year] = [dates[i], gap]

    return result



def yearly_gdd(dates, tavg):

    result = {}

    for i in range(len(dates)):

        parts = dates[i].split('-')

        year = parts[0]

        month = int(parts[1])


        if 5 <= month <= 9:

            gdd = tavg[i] - 5

            if gdd < 0:
                gdd = 0

            if year not in result:

                result[year] = 0

            result[year] += gdd

    return result


def main():

    filename = "weather(2001-2022).csv"

    dates, tmax, tmin, tavg = load_weather(filename)


    print("===== 연도별 최대 일교차 =====")

    max_gap = yearly_max_gap(dates, tmax, tmin)

    for year in sorted(max_gap):

        date = max_gap[year][0]

        gap = round(max_gap[year][1], 1)

        print(date, gap)

    print()


    print("===== 연도별 적산온도 =====")

    gdd_result = yearly_gdd(dates, tavg)

    for year in sorted(gdd_result):

        print(year, round(gdd_result[year], 1))


if __name__ == "__main__":
    main()