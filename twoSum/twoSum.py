"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

from typing import List

class Solution:

  # Brute force:
  def twoSumBruteForce(sefl, nums: List[int], target: int):
    if len(nums) == 1:
      return []
    else:
      for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
          if nums[j] == target - nums[i]:
            return [i, j]
      return []
  
  # Use hash map
  def twoSumHash(self, nums: List[int], target: int):
    map = {}
    for i in range(len(nums)):
      map[nums[i]] = i
    
    for j in range(len(nums)):
      complement = target - nums[j]
      if complement in map and map[complement] != j:
        return [j, map.get(complement)]
    
    return []
  
  # Use hash map with one loop
  def twoSumHash2(self, nums: List[int], target: int):
    map = {}
    for i in range(len(nums)):
      complement = target - nums[i]
      
      if complement in map:
        return [ map.get(complement), i]
      
      map[nums[i]] = i

    return []



# Test area
input = [1, 3, 5, 8, 9]
target = 9

s = Solution()

#resultBruteForce = s.twoSumBruteForce(input, target) # this solution is slow, faster than 5% of Python 3 for Two Sum
#resultHashMap = s.twoSumHash(input, target) #this solution is much faster than brute force one
resultHashMap2 = s.twoSumHash2(input, target) #this solution is much faster than brute force one

print(resultHashMap2)