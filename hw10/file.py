def text2list(text):
    nums = text.split()
    nums = [int(x) for x in nums]
    return nums


def average(nums):
    return sum(nums) / len(nums)


def median(nums):
    nums.sort()
    n = len(nums)

    if n % 2 == 1:
        return nums[n // 2]
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2


def main():
    with open("numbers1.txt") as f:
        text = f.readline().strip()

    nums = text2list(text)

    print("총 개수:", len(nums))
    print("평균:", average(nums))
    print("최댓값:", max(nums))
    print("최솟값:", min(nums))
    print("중앙값:", median(nums))


if __name__ == "__main__":
    main()