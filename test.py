# def pair_with_targetsum(arr, target_sum):
#   nums = {}  # to store numbers and their indices
#   for i, num in enumerate(arr):
#     if target_sum - num in nums:
#       return [nums[target_sum - num], i]
#     else:
#       nums[arr[i]] = i
#   return [-1, -1]

arr = [2, 5, 8]
for i, num in enumerate(arr):
  print(i, num)
