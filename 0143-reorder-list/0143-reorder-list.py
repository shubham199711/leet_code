class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow ,fast =  head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #reversing the second half of the list
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev #null intially
            prev = second
            second = temp

        #merge 2 halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next #storing the link between node
            first.next = second
            second.next = tmp1
            #shift pointers
            first ,second = tmp1,tmp2