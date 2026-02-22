#
# @lc app=leetcode.cn id=83 lang=python3
# @lcpr version=30204
#
# [83] 删除排序链表中的重复元素
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
        # 处理特殊情况：列表为空
        if head is None:
            return head
        
        # 初始化cur指针指向头节点：
        cur = head
        # 主循环：
        # 1、循环条件：cur指向节点还有下一个节点；
        # 2、执行逻辑：如果cur指向的节点与其下一个节点相等，就删除下一个节点；如果不相等，就将cur指针指向下一个节点；
        while cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3,3]\n
# @lcpr case=end

#

