# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def linked_list_to_int(node: Optional[ListNode]):
            num_str = ''
            while node:
                num_str += str(node.val)
                node = node.next
            return int(num_str[::-1])
        
        num1=linked_list_to_int(l1)
        num2=linked_list_to_int(l2)
        num3=str(num1+num2)
        # num3=num3[::-1]
        head=None
        for digit in num3:
            node = ListNode(int(digit), head)
            head = node
        return head
        
        