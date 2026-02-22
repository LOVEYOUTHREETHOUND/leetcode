#
# @lc app=leetcode.cn id=34 lang=python3
# @lcpr version=30204
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 实现函数lower_bound，功能：根据target进行红蓝染色，红：小于target；蓝：大于等于target；在这样的定义下，循环结束之后，L始终指向第一个大于等于target的数
        def lower_bound(x: int) -> int:
            L = 0
            R = len(nums) - 1# 在闭区间上进行讨论：[L, R]
            while L <= R:
                M = (L + R) // 2
                if nums[M] >= x:
                    R = M - 1
                else:
                    L = M + 1
            return L
        
        left = lower_bound(target)
        if left == len(nums) or nums[left] != target: # 对应四种需要返回[-1, -1]的特殊情况：1、所有数都小于target：循环结束之后L = len(nums);2、所有数都大于target：循环结束之后L = 0 且 nums[0] > target → nums[left] != target；3、中间缺失：nums[left] > target → nums[left] != target；4、空数组：len(nums)=0 → left==len(nums)；
            return [-1, -1]

        right = lower_bound(target + 1) - 1 # [left, right]
        return [left, right]

        



# @lc code=end



#
# @lcpr case=start
# [5,7,7,8,8,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,7,7,8,8,10]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#

