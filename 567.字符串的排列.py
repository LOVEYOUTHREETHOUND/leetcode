#
# @lc app=leetcode.cn id=567 lang=python3
# @lcpr version=30307
#
# [567] 字符串的排列
#
# https://leetcode.cn/problems/permutation-in-string/description/
#
# algorithms
# Medium (46.35%)
# Likes:    1083
# Dislikes: 0
# Total Accepted:    341K
# Total Submissions: 735.4K
# Testcase Example:  '"ab"\n"eidbaooo"\n"ab"\n"eidboaoo"'
#
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的 排列。如果是，返回 true ；否则，返回 false 。
# 
# 换句话说，s1 的排列之一是 s2 的 子串 。
# 
# 
# 
# 示例 1：
# 
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
# 
# 
# 示例 2：
# 
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s1.length, s2.length <= 10^4
# s1 和 s2 仅包含小写字母
# 
# 
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 维护滑动窗口状态：
        window = {}
        need = {}
        for c in s1:
            need[c] = need.get(c, 0) + 1
        valid = 0
        
        # 初始化滑动窗口：
        left = 0
        right = 0
        # 右扩张滑动窗口：
        while right <= len(s2) - 1:
            c = s2[right]
            right += 1
            # 更新窗口状态：
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            # 满足条件时左收缩滑动窗口：
            if right - left == len(s1):
                d = s2[left]
                left += 1
                # 判断是否是合法子串：
                if valid == len(need):
                    return True
                # 更新窗口状态：
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        # 返回：
        return False
# @lc code=end



#
# @lcpr case=start
# "ab"\n"eidbaooo"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"eidboaoo"\n
# @lcpr case=end

#

