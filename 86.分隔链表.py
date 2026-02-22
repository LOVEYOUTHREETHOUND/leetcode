#
# @lc app=leetcode.cn id=86 lang=python3
# @lcpr version=30307
#
# [86] 分隔链表
#
# https://leetcode.cn/problems/partition-list/description/
#
# algorithms
# Medium (65.86%)
# Likes:    961
# Dislikes: 0
# Total Accepted:    388.1K
# Total Submissions: 589.3K
# Testcase Example:  '[1,4,3,2,5,2]\n3\n[2,1]\n2'
#
# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
# 
# 你应当 保留 两个分区中每个节点的初始相对位置。
# 
# 
# 
# 示例 1：
# 
# 输入：head = [1,4,3,2,5,2], x = 3
# 输出：[1,2,2,4,3,5]
# 
# 
# 示例 2：
# 
# 输入：head = [2,1], x = 2
# 输出：[1,2]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目在范围 [0, 200] 内
# -100 <= Node.val <= 100
# -200 <= x <= 200
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 初始化两个新链表（一个链表放小于x的节点，一个链表放大于x的节点）的虚拟头节点：
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        # 初始化所需要的三个指针指向已有的三个链表的头节点：
        p = head
        p1 = dummy1
        p2 = dummy2
        # 遍历原始链表，并按照比较结果分配每个节点到对应的链表：
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            
            # 因为本题中“分割”的操作实质上是将原始链表的节点移动到两个新链表中，所以需要断开原始链表中的next关系：
            next = p.next
            p.next = None
            p = next

        # 连接两个新链表：
        p1.next = dummy2.next
        # 返回：
        return dummy1.next
# @lc code=end



#
# @lcpr case=start
# [1,4,3,2,5,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n
# @lcpr case=end

#

