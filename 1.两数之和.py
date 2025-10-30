#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    # method1:
    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     n = len(nums)
    #     for i in range(n):
    #         for j in range(i+1,n):
    #             if nums[i] + nums[j] == target:
    #                 return [i,j]
    #     return []
                

    # method2:
    def twoSum(self,nums, target):
        hashtable = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashtable:
                return [i,hashtable[complement]]
            else:
                hashtable[nums[i]] = i
        return []

            
        






        
# @lc code=end

