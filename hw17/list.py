def main():
    numbers = []

    while True:
        x = input("X=? ")

        if x == "-1":
            break

        try:
            num = int(x)

            if num > 0:
                numbers.append(num)

        except ValueError:
            pass

    print(f"입력된 값은 {numbers} 입니다.")

    count = len(numbers)

    if count > 0:
        avg = sum(numbers) / count
    else:
        avg = 0

    print(f"총 {count}개의 자연수가 입력되었고, 평균은 {avg}입니다.")


if __name__ == "__main__":
    main()