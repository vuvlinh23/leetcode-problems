'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Use recursion to calculate the maximum height:
# 1. recursively calculate the height of the tree to the left of the root
# 2. recursively calculate the height of the tree to the right of the root
# 3. pick the larger height from the two answers and add one to it (plus the root node)

def maxDepth(root: TreeNode) -> int:
  # null node has 0 depth.
  if root == None:
    return 0
  
  # get the depth of the left and the right subtree
  # using recursion.
  leftDepth = maxDepth(root.left)
  rightDepth = maxDepth(root.right)

  # choose the larger one and add the root to it
  if leftDepth > rightDepth:
    return leftDepth + 1
  else:
    return rightDepth + 1


# input
rootNode = TreeNode(1)
rootNode.left = TreeNode(2)
rootNode.right = TreeNode(3)
rootNode.left.left = TreeNode(4)
rootNode.left.right = TreeNode(5)
rootNode.left.left.left = TreeNode(6)

# output
result = maxDepth(rootNode)

print(result)