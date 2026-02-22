#
# @lc app=leetcode.cn id=142 lang=python3
# @lcpr version=30204
#
# [142] 环形链表 II
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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 定义快慢指针指向头节点：
        slow = head
        fast = head
        # 主循环：
        # 1、循环条件： 两个指针还在走（fast指针不指向空节点且其指向节点的下一个节点不是空节点）；
        # 2、跳出循环：走完了（快指针指向空节点或快指针指向节点的下一节点是空节点），意味着可以走到头=没有环
        # 3、循环体执行什么内容：快指针“追”慢指针直到在环内追到，之后执行内层循环：slow指针和head指针相向而行知道相遇在入口节点。
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow: # 追上
                while slow is not head: # 开始执行相遇问题
                    head = head.next
                    slow = slow.next
                return slow


        return None

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

