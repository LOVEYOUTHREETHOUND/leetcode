#
# @lc app=leetcode.cn id=19 lang=python3
# @lcpr version=30204
#
# [19] 删除链表的倒数第 N 个结点
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 因为有可能删除头节点，所以初始化一个dummy node：
        dummy = ListNode(next = head)

        # 初始化左右指针指向dummy：
        left = dummy
        right = dummy

        # 右指针走n步：
        for _ in range(n):
            right = right.next

        # 左右指针开始同时走（间距始终为n），直到右指针指向倒数第一个节点，这是左指针正好指向倒数（n+1）个节点：
        while right.next:
            left = left.next
            right = right.next

        # 删除倒数第n个节点：
        left.next = left.next.next

        # 返回头节点：
        return dummy.next


# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n
# @lcpr case=end

#

