#
# @lc app=leetcode.cn id=303 lang=python3
# @lcpr version=30307
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        # 输入为nums数组，需要利用nums数组构建前缀和数组：
        n = len(nums)
        # 初始化前缀和数组preSum(前缀和数组定义：对应位置之前，不包括该位置的前缀和)：
        self.preSum = [0] * (n + 1)
        # 根据nums数组的值对前缀和数组赋值：
        for i in range(n):
            self.preSum[i + 1] = self.preSum[i] + nums[i]



    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right + 1] - self.preSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end



#
# @lcpr case=start
# ["NumArray","sumRange","sumRange","sumRange"]\n[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]\n
# @lcpr case=end

#

