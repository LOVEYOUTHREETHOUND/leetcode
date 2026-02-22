#
# @lc app=leetcode.cn id=19 lang=python3
# @lcpr version=30307
#
# [19] 删除链表的倒数第 N 个结点
#
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (52.67%)
# Likes:    3244
# Dislikes: 0
# Total Accepted:    2M
# Total Submissions: 3.8M
# Testcase Example:  '[1,2,3,4,5]\n2\n[1]\n1\n[1,2]\n1'
#
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
# 
# 
# 
# 示例 1：
# 
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
# 
# 
# 示例 2：
# 
# 输入：head = [1], n = 1
# 输出：[]
# 
# 
# 示例 3：
# 
# 输入：head = [1,2], n = 1
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中结点的数目为 sz
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
# 
# 
# 
# 
# 进阶：你能尝试使用一趟扫描实现吗？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 初始化虚拟头节点指向head节点：
        dummy = ListNode(-1)
        dummy.next = head
        # 初始化两个指针指向虚拟头节点：
        p1 = dummy
        p2 = dummy
        # p1指针先走（n）步：
        for _ in range(n - 1):
            p1 = p1.next
        # p1指针和p2指针同时走到p1指向尾节点的上一个节点，此时p2指针指向的是倒数第n个节点的前驱节点：
        while p1.next.next:
            p1 = p1.next
            p2 = p2.next
        # 删除倒数第n个节点：
        p2.next = p2.next.next
        # 返回：
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

