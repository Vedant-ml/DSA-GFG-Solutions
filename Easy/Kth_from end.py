""" Structure of Linked List Node
class Node:
    def __init__(self, x):
        self.data = x
    ata    self.next = None
"""

class Solution:
    def getKthFromLast(self, head, k):
        fast=head
        slow=head
        
        for i in range(k):
            if fast is None:
                return -1
            fast=fast.next
        
        while fast:
            slow=slow.next
            fast=fast.next
        
        return slow.data