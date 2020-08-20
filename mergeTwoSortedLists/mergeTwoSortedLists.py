'''
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## solution 1: use recursive
def mergeTwoLists1(l1: ListNode, l2: ListNode) -> ListNode:
    def merge(left, right):
        if not right:
            return left
        if not left:
            return right

        if left.val < right.val:
            left.next = merge(left.next, right)
            return left
        right.next = merge(left, right.next)
        return right

    return merge(l1, l2)

## solution 2: use dummy head
def mergeTwoLists2(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    head = dummy

    while l1 != None and l2 != None:
        if l1.val < l2.val:
            dummy.next = l1
            l1 = l1.next
        else:
            dummy.next = l2
            l2 = l2.next

        dummy = dummy.next
    
    if l1 != None:
        dummy.next = l1
    else:
        dummy.next = l2
    
    # Because we dont need first dummy node, we will return next node(real start node)
    return head.next