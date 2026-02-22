#
# @lc app=leetcode.cn id=876 lang=python3
# @lcpr version=30204
#
# [876] 链表的中间结点
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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 定义快慢指针都指向头节点：
        fast = slow = head
        # 开始循环：
        # 1、循环条件：还没走完（快指针不为空且其下一个节点也不是空）；
        # 2、跳出循环：走完了（快指针下一个节点为空或快指针为空）；
        # 3、循环内操作:快指针走两格，慢指针走一格。
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        return slow
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6]\n
# @lcpr case=end

#

