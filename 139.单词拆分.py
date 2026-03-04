#
# @lc app=leetcode.cn id=139 lang=python3
# @lcpr version=30400
#
# [139] 单词拆分
#
# https://leetcode.cn/problems/word-break/description/
#
# algorithms
# Medium (59.69%)
# Likes:    2913
# Dislikes: 0
# Total Accepted:    976.9K
# Total Submissions: 1.6M
# Testcase Example:  '"leetcode"\n' +
  # '["leet","code"]\n' +
  # '"applepenapple"\n' +
  # '["apple","pen"]\n' +
  # '"catsandog"\n' +
  # '["cats","dog","sand","and","cat"]'
#
# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。
# 
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
# 
# 
# 
# 示例 1：
# 
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
# 
# 
# 示例 2：
# 
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
# 注意，你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s 和 wordDict[i] 仅由小写英文字母组成
# wordDict 中的所有字符串 互不相同
# 
# 
#

# @lc code=start
"""
分析：本题属于一维动态规划问题，使用dp table进行求解；
1、dp[i]的含义：表示前i个字符能否被拼出；
2、如何初始化基础值：dp[0] = True
3、如何进行状态转移：对于dp[i]是true还是false（前i位是否可以被拼出）：需要遍历前面所有值，进行判断；
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 初始化dp table：
        n = len(s)
        dp = [False] * (n + 1)

        word_set = set(wordDict)

        # 初始化基础值：
        dp[0] = True
        # 根据状态转移公式填充dp table:
        for i in range(1, n + 1):
          for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
        # 返回：
        return dp[n]
# @lc code=end



#
# @lcpr case=start
# "leetcode"\n["leet","code"]\n
# @lcpr case=end

# @lcpr case=start
# "applepenapple"\n["apple","pen"]\n
# @lcpr case=end

# @lcpr case=start
# "catsandog"\n["cats","dog","sand","and","cat"]\n
# @lcpr case=end

#

