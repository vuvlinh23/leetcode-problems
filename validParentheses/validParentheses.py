'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''

# use stack
def isValid(s: str) -> bool:
  if len(s) % 2 != 0:
    return False
  
  #stack to keep track of opening brackets
  stack = []

  # hash map for keeping track of mappings
  mapping = {
    '(': ')',
    '{': '}',
    '[': ']',
  }

  # set is faster when in comes to determining if an object
  # is in the set (as x in y), but are slower than lists when it comes to iterating over their contents
  openPar = set(['(', '{', '['])

  for char in s:
    # if char is open -> push to stack
    if char in openPar:
      stack.append(char)

    # if char is close -> check if the previos is the open with same type
    elif stack and char == mapping[stack[-1]]:
      stack.pop()
    else:
      return False
  return stack == []


test = '((()(())))'

result = isValid(test)

print(result)