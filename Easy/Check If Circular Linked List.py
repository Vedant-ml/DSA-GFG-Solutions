# Given the head of a singly linked list, Returns true if the linked list is circular & false if it is not circular.

# A linked list is called circular if it is not NULL terminated and all nodes are connected in the form of a cycle. 

# Note: Linked list should not contain any inner loop. And a empty linked list is always a circular linked list.

#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


class Solution:
    def isCircular(self, head):
        # code here
        if head is None:
            return True
        fast=head
        
        while fast:
            fast=fast.next
        
            if fast==head:
                return True
        return False
        
        