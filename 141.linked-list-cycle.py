#
# @lc app=leetcode.cn id=141 lang=python3
# @lcpr version=30204
#
# [141] 环形链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 定义快慢指针指向头节点：
        slow = fast = head

        # 主循环：
        # 1、循环条件：两个指针都还在走（fast指针不为空且其指向的下一个节点不为空）；
        # 2、什么时候跳出循环：快指着追上慢指针；
        # 循环体执行什么逻辑：“追”
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # “追上”，也可以写成slow is fast
                return True
        return False
# @lc code=end



#
# @lcpr case=start
# [3,2,0,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1]\n-1\n
# @lcpr case=end

#

