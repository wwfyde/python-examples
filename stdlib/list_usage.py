def main():
    nums = [1, 2, 3, 4]
    doubled_nums = list(map(lambda x: x * 2, nums))
    pythonic_doubled_nums = [x * 2 for x in nums]
    pass

    # filter
    filtered = filter(lambda x: x % 2 == 0, nums)
    print(list(filtered))
    filtered_ = [x for x in nums if x % 2 == 0]
    print(filtered_)


if __name__ == "__main__":
    main()
