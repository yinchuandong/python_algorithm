# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = rlist = ListNode(0)

        s = 0
        while l1 is not None or l2 is not None:
            s /= 10
            if l1 is not None:
                s += l1.val
                l1 = l1.next
            if l2 is not None:
                s += l2.val
                l2 = l2.next
            reminder = s % 10
            head.next = ListNode(reminder)
            head = head.next

        if s / 10 == 1:
            head.next = ListNode(1)
        return rlist.next


def printList(ln):
    arr = []
    while ln is not None:
        arr.append(ln.val)
        ln = ln.next
    print arr


if __name__ == '__main__':
    ln11 = ListNode(9)
    ln12 = ListNode(9)
    # ln13 = ListNode(3)
    ln11.next = ln12
    # ln12.next = ln13

    ln21 = ListNode(1)
    # ln22 = ListNode(6)
    # ln23 = ListNode(4)
    # ln21.next = ln22
    # ln22.next = ln23

    s = Solution()
    rlist = s.addTwoNumbers(ln11, ln21)
    printList(rlist)
