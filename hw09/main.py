from average import average

def main():
    nums = list(map(int, input("숫자 입력(공백 구분): ").splist()))
    print("평균:", average(nums))

if __name__ == "__main__":
    main()