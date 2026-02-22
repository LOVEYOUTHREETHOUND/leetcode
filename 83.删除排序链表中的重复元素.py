#
# @lc app=leetcode.cn id=83 lang=python
# @lcpr version=30307
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 边界处理：
        if not head:
            return None
        # 初始化快慢指针（读写指针）：
        fast = head
        slow = head
        # 重组链表（和26题一样）：
        while fast:
            # 对于每段值相同的链表，只串联第一个节点：
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        # 断开之后的节点：
        slow.next = None
        # 返回：
        return head
# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3,3]\n
# @lcpr case=end

#

