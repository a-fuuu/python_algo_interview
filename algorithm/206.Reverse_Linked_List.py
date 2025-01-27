'''
연결리스트를 뒤집어라
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def reverseLinkedList(self, head: ListNode):
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)
    
solution = Solution()
lst1 = ListNode(1)
lst1.next = ListNode(1)
lst1.next.next = ListNode(1)
lst1.next.next.next = ListNode(2)
lst1.next.next.next.next = ListNode(3)
lst1.next.next.next.next.next = ListNode(1500)

result = solution.reverseLinkedList(lst1)

current_node = result

while current_node:
    print(current_node.val)
    current_node = current_node.next