def toggle_text(text: str) -> str:
    result = ""

    for ch in text:
        code = ord(ch)

        if 65 <= code <= 90:      # 대문자
            result += chr(code + 32)
        elif 97 <= code <= 122:   # 소문자
            result += chr(code - 32)
        else:
            result += ch

    return result


text = input("문자열 입력: ")
print(toggle_text(text))