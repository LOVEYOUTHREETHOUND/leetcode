#
# @lc app=leetcode.cn id=21 lang=python3
# @lcpr version=30307
#
# [21] 合并两个有序链表
#
# https://leetcode.cn/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (68.12%)
# Likes:    3963
# Dislikes: 0
# Total Accepted:    2.3M
# Total Submissions: 3.4M
# Testcase Example:  '[1,2,4]\n[1,3,4]\n[]\n[]\n[]\n[0]'
#
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 
# 
# 示例 1：
# 
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 
# 
# 示例 2：
# 
# 输入：l1 = [], l2 = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 输入：l1 = [], l2 = [0]
# 输出：[0]
# 
# 
# 
# 
# 提示：
# 
# 
# 两个链表的节点数目范围是 [0, 50]
# -100 <= Node.val <= 100
# l1 和 l2 均按 非递减顺序 排列
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建新链表（合并链表）的虚拟头节点：
        dummy = ListNode(-1)
        # 创建三个指针分别指向对应链表（的头节点）：
        p = dummy
        p1 = list1
        p2 = list2
        # 两个原始链表都未遍历完时，进行比较并将小的节点加入合并链表：
        while p1 is not None and p2 is not None:
            if p1.val >= p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next
        # 有一个原始链表遍历完时，直接将剩下的那个原始链表的剩下部分接到合并链表之后即可：
        if p1 is not None:
            p.next = p1
        if p2 is not None:
            p.next = p2
        # 返回：
        return dummy.next

# @lc code=end



#
# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#

