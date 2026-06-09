import random

CHOSUNG_LIST = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ',
    'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
    'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ',
    'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]


def get_chosung(word):
    result = ""

    for ch in word:
        code = ord(ch) - ord('가')
        cho = code // (21 * 28)
        result += CHOSUNG_LIST[cho]

    return result


def main():
    words = [
        "사과",
        "강아지",
        "컴퓨터",
        "자동차",
        "바나나",
        "프로그래밍"
    ]

    answer = random.choice(words)

    print("초성 :", get_chosung(answer))

    user = input("정답 입력 : ")

    if user == answer:
        print("정답!")
    else:
        print("오답!")
        print("정답은", answer, "입니다.")


if __name__ == "__main__":
    main()