def c2f(t_c):
    return t_c * 9 / 5 + 32

def main():
    print("섭씨 0도 -> 화씨:", c2f(0))
    print("섭씨 25도 -> 화씨:", c2f(25))

if __name__ == "__main__":
    main()