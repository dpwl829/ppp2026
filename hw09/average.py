def average(nums):
    if not nums:
        return 0
    return sum(nums)/len(nums)

def main():
    print(average([1,2,3,4,5,]))

if __name__=="__main__":
    main()