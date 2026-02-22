#
# @lc app=leetcode.cn id=82 lang=python3
# @lcpr version=30204
#
# [82] 删除排序链表中的重复元素 II
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 因为有可能删除头节点，所以需要初始化dummy node：
        dummy = ListNode(next = head)

        # 初始化cur节点指向dummy node：
        cur = dummy

        # 比较cur指向的节点的下一个节点与下下个节点：
        # 1、如果相等：需要将连续重复的所有节点都删除：不断删除第一个节点：
        # 2、如果不相等：说明cur的下一个节点以及下下个节点不再重复，所以就应该将cur后移一位；
        while cur.next and cur.next.next:
            val = cur.next.val
            if cur.next.next.val == val:
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        # 返回头节点：
        return dummy.next

# @lc code=end



#
# @lcpr case=start
# [1,2,3,3,4,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,2,3]\n
# @lcpr case=end

#

