def firstMissingPositive(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if 0 < nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    # [1, 2, 3] -> 4
    return n + 1
