from typing import List

def twoSum(nums: List[int], target: int):
  if len(nums) == 1:
    return []
  else:
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if nums[j] == target - nums[i]:
          print("couple: ", nums[i], nums[j])
          return [i, j]
    return []

input = [1, 3, 5, 7, 8]

result = twoSum(input, 9)
print('result: ', result)