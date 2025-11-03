#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30204
#
# [15] 三数之和
#
 

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 解法一：暴力循环求解（时间复杂度太高）
        # 解法二：哈希表法：
        # nums.sort()
        # n = len(nums)
        # triplets = set()
        # for i in range(n):
        #     if nums[i] > 0:
        #         break
        #     else:
        #         if i > 0 and nums[i] == nums[i-1]:
        #             continue
        #         candidates = set()
        #         for j in range(i+1,n):
        #             target = -(nums[i] + nums[j])
        #             if target in candidates:
        #                 triplet = sorted([nums[i],nums[j],target])
        #                 triplets.add(tuple(triplet))
        #             candidates.add(nums[j])
        # return [list(triplet) for triplet in triplets]
        # 解法三：双指针法
        nums.sort()
        n = len(nums)
        results = set()
        for i in range(n):
            left = i + 1
            right = n - 1
            target = -nums[i]
            #在条件判断之前需要做剪枝操作，避免最后超时：
            #剪枝1：没有上升趋势就代表已经找过，直接跳过continue即可：
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            #剪枝2：如果三元组中第一个元素已经大于0，就表示三元组已经找完了，直接break
            if nums[i] > 0:
                break
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    #找到一个三元组：
                    result = ([nums[i],nums[left],nums[right]])
                    results.add(result)
                    #在步进之前最好是对左指针和右指针都进行剪枝去重：
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    #左右同时步进：
                    left += 1
                    right -= 1
        return [list(result) for result in results]      



# @lc code=end



#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#

