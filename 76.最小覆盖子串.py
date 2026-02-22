#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30307
#
# [76] 最小覆盖子串
#
# https://leetcode.cn/problems/minimum-window-substring/description/
#
# algorithms
# Hard (48.79%)
# Likes:    3491
# Dislikes: 0
# Total Accepted:    990.9K
# Total Submissions: 2M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"\n"a"\n"a"\n"a"\n"aa"'
#
# 给定两个字符串 s 和 t，长度分别是 m 和 n，返回 s 中的 最短窗口 子串，使得该子串包含 t
# 中的每一个字符（包括重复字符）。如果没有这样的子串，返回空字符串 ""。
# 
# 测试用例保证答案唯一。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
# 
# 
# 示例 2：
# 
# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串 s 是最小覆盖子串。
# 
# 
# 示例 3:
# 
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。
# 
# 
# 
# 提示：
# 
# 
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s 和 t 由英文字母组成
# 
# 
# 
# 进阶：你能设计一个在 O(m + n) 时间内解决此问题的算法吗？
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 初始化滑动窗口（左闭右开）：
        left = 0
        right = 0
        need = {}
        window = {}
        # 根据目标t填充need哈希表：
        for c in t:
            need[c] = need.get(c, 0) + 1

        valid = 0
        length = float('inf')
        start = 0

        # 滑动窗口开始向右扩张直到即将越界（右指针遍历）：
        while right <= len(s) - 1:
            # 扩张进来的元素是s[right - 1]，根据这个元素更新window、valid：
            right += 1
            c = s[right - 1]
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            # 满足条件时开始收缩左侧窗口：
            while valid == len(need):
                # 收缩排除的元素是s[left],根据这个元素更新window、length、start、valid:
                c = s[left]
                # 现在位置当前滑动窗口对应的子串还是合法的，需要看看要不要更新start以及length：
                if right - left < length:
                    start = left
                    length = right - left
                # 更新window、valid：
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
                # 执行左窗口收缩：
                left += 1
        # 返回：
        return '' if length == float('inf') else s[start: start + length]
# @lc code=end



#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#

