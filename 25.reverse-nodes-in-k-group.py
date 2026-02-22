#
# @lc app=leetcode.cn id=25 lang=python3
# @lcpr version=30204
#
# [25] K 个一组翻转链表
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 计算链表长度：
        n = 0 # 链表长度
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        # 设置哨兵节点与p0：
        dummy = ListNode(next = head)
        p0 = dummy

        # 初始化子组翻转需要的指针pre与cur：
        pre = None
        cur = p0.next

        # 主循环：只要剩余节点大于k就执行一组k个子节点的翻转：
        while n >= k:
            n -= k
            # 开始执行子组翻转：
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            
            # 翻转完成之后将子组与原链表进行衔接：
            nxt = p0.next # 暂时存储，用于3
            # 1、将原来子组的头节点（p0.next.next）指向下一组的开头（现在cur指向的节点）：
            p0.next.next = cur
            # 2、子组之前的上一个节点（p0.next）指向子组原末尾（现在pre指向的节点）：
            p0.next = pre
            # 3、更新p0：根据p0的含义（指针p0始终应该指向正在处理的子组的头节点的上一个节点，便于处理完成之后进行衔接），应将p0指向上一次处理的子组中的原头节点（现末尾节点）：
            p0 = nxt

        # 返回处理之后的链表的头节点：
        return dummy.next




# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#

