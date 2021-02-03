# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        cur = head
        index = 0
        stack = []
        res = []
        while cur:
            res.append(0)
            while stack and stack[-1][-1] < cur.val:
                temp = stack.pop()
                res[temp[0]] = cur.val
                
            stack.append([index, cur.val])
            index += 1
            cur = cur.next
            
        #print(stack)
        return res