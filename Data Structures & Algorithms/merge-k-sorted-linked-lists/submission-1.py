# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sortedList = ListNode()
        curr = sortedList

        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        mid = len(lists)//2

        list1 = self.mergeKLists(lists[:mid])
        list2 = self.mergeKLists(lists[mid:])

        i, j = list1, list2

        while i is not None and j is not None:
            if i.val <= j.val:
                curr.next = ListNode(i.val)
                curr, i = curr.next, i.next
            else:
                curr.next = ListNode(j.val)
                curr, j = curr.next, j.next

        while i is not None:
            curr.next = ListNode(i.val)
            curr, i = curr.next, i.next

        while j is not None:
            curr.next = ListNode(j.val)
            curr, j = curr.next, j.next


        return sortedList.next