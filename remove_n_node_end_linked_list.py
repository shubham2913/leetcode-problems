#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        nodes=[]
        length=0
        temp=head
        while temp.next!=None :
            nodes.append(temp)
            temp=temp.next
        nodes.append(temp)
        if len(nodes)==1 :
            return None
        if n==len(nodes) :
            head=nodes[1]
            return head
        if n==1 :
            nodes[-2].next=None
            return head
        nodes[-n-1].next=nodes[-n+1]
        return head