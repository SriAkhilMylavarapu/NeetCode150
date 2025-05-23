# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        move1, move2 = headA, headB
        hsh = dict()

        while move1 is not None:
            hsh[move1] = 1
            move1 = move1.next
            if move1 is None:
                break

        while move2 is not None:
            if move2 in hsh:
                return move2
            move2 = move2.next
            if move2 is None:
                break

        return None