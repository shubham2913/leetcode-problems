#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head) :
        if head==None or head.next==None :
            return head
        else :
            temp1=head
            temp2=head.next
            temp=temp1.val
            temp1.val=temp2.val
            temp2.val=temp
            head=temp1
            #print(temp2.val)
            print(head.val)
            temp1=temp2.next
            while temp1!=None :
                temp2=temp1.next
                if temp2==None :
                    break
                temp=temp1.val
                temp1.val=temp2.val
                temp2.val=temp
                temp1=temp2.next
            return head