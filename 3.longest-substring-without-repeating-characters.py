#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30204
#
# [3] 无重复字符的最长子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = Counter()
        left = 0
        ans = 0

        # 主循环：
        for right, ch in enumerate(s):
            cnt[ch] += 1
            # 重复性只来自最右边新加入的元素：
            while cnt[ch] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
            


# @lc code=end



#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

