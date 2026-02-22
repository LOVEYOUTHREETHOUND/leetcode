#
# @lc app=leetcode.cn id=23 lang=python3
# @lcpr version=30307
#
# [23] 合并 K 个升序链表
#
# https://leetcode.cn/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (63.29%)
# Likes:    3144
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 1.8M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]\n[]\n[[]]'
#
# 给你一个链表数组，每个链表都已经按升序排列。
# 
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
# 
# 
# 
# 示例 1：
# 
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
# 
# 
# 示例 2：
# 
# 输入：lists = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 输入：lists = [[]]
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 根据示例，需要处理特殊情况：lists为空时返回空：
        if not lists:
            return None        
        # 初始化结果链表以及对应指针：
        dummy = ListNode(-1)
        p = dummy
        # 初始化最小堆（优先队列）pq并将所有k个链表的头节点填入其中完成初始化，之后只需要移动对应链表的指针并对pq进行更新即可：
        pq = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(pq, (head.val, i, head))

        # 从优先队列中不断取出根节点并移动至结果链表，同时将对应的下一个节点push进优先队列中：
        while pq:
            val, i, node = heapq.heappop(pq)
            p.next = node
            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))
            p = p.next
        # 返回：
        return dummy.next
# @lc code=end



#
# @lcpr case=start
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [[]]\n
# @lcpr case=end

#

