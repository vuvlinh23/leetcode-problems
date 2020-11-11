'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''
# def singleNumber(nums: List[int]) -> int:
#     # Iterate over list, if item in list => remove, if item not in list => add to list
#     noDuplicateList = []
#     for i in nums:
#         if i not in noDuplicateList:
#             noDuplicateList.append(i)
#         else:
#             noDuplicateList.remove(i)
#     return noDuplicateList[0]
#     # Time complexity: O(n^2)
#     # Space complexity: O(n)
    
def singleNumber(nums) -> int:
    # Set up a hash map, return element apperared only one
    dict = {}
    for i in nums:
        if not dict.get(i):
            dict[i] = 0
            dict[i] +=1
        else:
            dict[i] += 1

    for k in dict:
        if dict[k] == 1:
            return k
    # Time complexity: O(n)
    # Space complexity: O(n)


input = [2, 2, 1]
output = singleNumber(input)
print(output)