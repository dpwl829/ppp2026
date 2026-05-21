

def main():
    with open("weather(146)_2022-2022.csv", encoding="cp949") as f:
        lines = f.readlines()
        print(lines)


if __name__ == "__main__":
    main()

import csv

with open("weather(146)_2022-2022.csv", encoding="cp949") as f:
    data = csv.reader(f)

    header = next(data)

    print(header)

    for row in data:
        print(row)