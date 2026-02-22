# @lcpr-before-debug-begin
from python3problem438 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30204
#
# [438] 找到字符串中所有字母异位词
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)

        if n < m:
            return []

        window = [0] * 26

        # 根据小写字母给出在windows数组中对应的索引：
        def idx(ch: str) -> int:
            return ord(ch) - ord('a')

        # 构建p对应的频次数组need：
        need = [0] * 26
        for ch in p:
            need[idx(ch)] += 1

        # 初始化结果数组：
        res = []

        # 初始化第一个窗口：
        for i in range(m):
            window[idx(s[i])] += 1

        # 先检查第一个窗口（起点为 0）
        if window == need:
            res.append(0)

        # 主循环：从窗口 [1..m] 开始滑动
        for i in range(0, n - m):
            window[idx(s[i])] -= 1
            window[idx(s[i + m])] += 1

            if window == need:
                res.append(i + 1)

        return res
        
# @lc code=end



#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#

