def caesar_encode(text: str, shift: int = 3) -> str:
    result = ""

    for ch in text:
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += ch

    return result


def caesar_decode(text: str, shift: int = 3) -> str:
    result = ""

    for ch in text:
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += ch

    return result


text = input("문자열 입력: ")

encoded = caesar_encode(text)
print("암호화:", encoded)

decoded = caesar_decode(encoded)
print("복호화:", decoded)