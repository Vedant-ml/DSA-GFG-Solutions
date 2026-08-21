# Given a linked list with the head node and a key, the task is to check if the key is present in the linked list or not. 

'''Structure of Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        # Code here
        curr=head
        while curr:
            if curr.data==key:
                return True
                break
            else:
                curr=curr.next
        return False