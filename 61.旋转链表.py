#
# @lc app=leetcode.cn id=61 lang=python3
# @lcpr version=30307
#
# [61] 旋转链表
#
# https://leetcode.cn/problems/rotate-list/description/
#
# algorithms
# Medium (41.45%)
# Likes:    1176
# Dislikes: 0
# Total Accepted:    495.6K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4,5]\n2\n[0,1,2]\n4'
#
# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
# 
# 
# 
# 示例 1：
# 
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
# 
# 
# 示例 2：
# 
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目在范围 [0, 500] 内
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 10^9
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 统计链表长度并遍历至尾部：
        if not head or not head.next:
            return head
        p = head
        n = 1
        while p.next:
            n += 1
            p = p.next
        # 循环结束之后,n为链表长度,p指针指向的是链表尾节点


        # 处理k可能大于链表长度的情况:
        if k > n:
            k = k % n
        # 闭合成环:
        p.next = head

        # 寻找新链表的尾节点(从原始尾节点移动n-k次即到达新链表的尾节点),断开成为新链表:
        for _ in range(n - k):
            p = p.next
        
        new_head = p.next
        p.next = None
        
        # 返回:
        return new_head
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2]\n4\n
# @lcpr case=end

#

