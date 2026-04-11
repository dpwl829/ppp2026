
def is_leap_year(y):
    if y % 4 == 0 and y % 100 != 0:
        return True
    return False

def main():
    print(is_leap_year(2024))

if __name__ == "__main__":
    main()