# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        cur = None
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        while list1 and list2:
            if head is None:
                if list1.val < list2.val:
                    head = list1
                    cur = list1
                    list1 = list1.next
                else:
                    head = list2
                    cur = list2
                    list2 = list2.next
            else:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                    cur = cur.next
                else:
                    cur.next = list2
                    list2 = list2.next
                    cur = cur.next
        while list1:
            cur.next = list1
            cur = cur.next
            list1 = list1.next
        while list2:
            cur.next = list2
            cur = cur.next
            list2 = list2.next
        return head