"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

class Solution:

    # convert number to string, reverse
    def reverseUsingString(self, x: int) -> int:
      isNegative = x < 0
      
      # get input string and remove the negative sign
      strInput = str(abs(x))

      # reverse string
      strOutput = strInput[::-1]

      # convert back to string
      numOutput = int(strOutput)

      if isNegative:
        numOutput = -numOutput

      if numOutput > -2**31 and numOutput < 2**31 - 1:
        return numOutput

      return 0



s = Solution()
input = -123

result = s.reverseUsingString(input)

print(result)