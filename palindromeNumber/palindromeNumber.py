'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?

'''

import math

class Solution:
    # Turn to string and compare with old one
    def isPalindromeUsingString(self, x: int) -> bool:
      if x < 0: return False
      return str(x) == str(x)[::-1]

    def isPalindromeNotUsingString(self, x: int) -> bool:
      if x < 0 or (x % 10 == 0 and x != 0):
        return False
      
      rev = 0
      while x > rev:
        rev = rev * 10 + x % 10
        x = math.floor(x / 10)
      
      # When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
      # For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
      # since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
      return x == rev or x == math.floor(rev/10)


input = 1231321

s = Solution()

# result = s.isPalindromeUsingString(input)
result = s.isPalindromeNotUsingString(input)

print(result)
