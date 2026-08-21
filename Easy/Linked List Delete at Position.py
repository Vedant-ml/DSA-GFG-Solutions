# Given the head of a linked list and an integer x, delete the node at position x and return the updated head of the linked list.

# Note: Positions use 1-based indexing.

''' Structure of Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        #code here
        if x==1:
            return head.next
        
        count=1
        curr=head
        prev=None
        while curr:
            if count==x:
                prev.next=curr.next
                break

            count=count+1
            prev=curr
            curr=curr.next
        return head
