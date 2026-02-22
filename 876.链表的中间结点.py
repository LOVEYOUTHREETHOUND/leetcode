#
# @lc app=leetcode.cn id=876 lang=python3
# @lcpr version=30307
#
# [876] 链表的中间结点
#
# https://leetcode.cn/problems/middle-of-the-linked-list/description/
#
# algorithms
# Easy (72.62%)
# Likes:    1107
# Dislikes: 0
# Total Accepted:    546K
# Total Submissions: 751.8K
# Testcase Example:  '[1,2,3,4,5]\n[1,2,3,4,5,6]'
#
# 给你单链表的头结点 head ，请你找出并返回链表的中间结点。
# 
# 如果有两个中间结点，则返回第二个中间结点。
# 
# 
# 
# 示例 1：
# 
# 输入：head = [1,2,3,4,5]
# 输出：[3,4,5]
# 解释：链表只有一个中间结点，值为 3 。
# 
# 
# 示例 2：
# 
# 输入：head = [1,2,3,4,5,6]
# 输出：[4,5,6]
# 解释：该链表有两个中间结点，值分别为 3 和 4 ，返回第二个结点。
# 
# 
# 
# 
# 提示：
# 
# 
# 链表的结点数范围是 [1, 100]
# 1 <= Node.val <= 100
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化快慢指针指向头节点：
        p1 = head
        p2 = head
        # 满足条件时快慢移动，停下来时p2正好指向中间节点：
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
        # 返回：
        return p2
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6]\n
# @lcpr case=end

#

