#
# @lc app=leetcode.cn id=92 lang=python3
# @lcpr version=30307
#
# [92] 反转链表 II
#
# https://leetcode.cn/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (58.05%)
# Likes:    2053
# Dislikes: 0
# Total Accepted:    716K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4,5]\n2\n4\n[5]\n1\n1'
#
# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right
# 的链表节点，返回 反转后的链表 。
# 
# 
# 示例 1：
# 
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
# 
# 
# 示例 2：
# 
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点数目为 n
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
# 
# 
# 
# 
# 进阶： 你可以使用一趟扫描完成反转吗？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n1\n1\n
# @lcpr case=end

#

