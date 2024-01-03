# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    #Solution 1 - Time Complexity: O(n), Space Complexity: O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        set = []
        while head != None:
            if head in set:
                return True
            set.append(head)
            head = head.next
        return False
    
    #Solution 2 - Time Complexity: O(n), Space Complexity: O(1)
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        slowPointer = fastPointer = head
        while fastPointer != None and fastPointer.next != None:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            if slowPointer == fastPointer:
                return True
        return False