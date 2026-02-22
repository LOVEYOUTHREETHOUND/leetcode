#
# @lc app=leetcode.cn id=143 lang=python3
# @lcpr version=30204
#
# [143] 重排链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 如果链表有奇数个节点，寻找中间节点；如果有偶数个节点，寻找第二个中间节点；
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 翻转中间节点(slow)及其之后的所有节点；
        pre = slow
        cur = slow.next
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        slow.next = None

        # 重排两个链表；
        head2 = pre
        while head2.next:
            head_next = head.next
            head2_next = head2.next
            head.next = head2
            head2.next = head_next
            head = head_next
            head2 = head2_next
        

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#

