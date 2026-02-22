#
# @lc app=leetcode.cn id=290 lang=python3
# @lcpr version=30307
#
# [290] 单词规律
#
# https://leetcode.cn/problems/word-pattern/description/
#
# algorithms
# Easy (45.44%)
# Likes:    729
# Dislikes: 0
# Total Accepted:    261.5K
# Total Submissions: 575.4K
# Testcase Example:  '"abba"\n"dog cat cat dog"\n"abba"\n"dog cat cat fish"\n"aaaa"\n"dog cat cat dog"'
#
# 给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。
# 
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。具体来说：
# 
# 
# pattern 中的每个字母都 恰好 映射到 s 中的一个唯一单词。
# s 中的每个唯一单词都 恰好 映射到 pattern 中的一个字母。
# 没有两个字母映射到同一个单词，也没有两个单词映射到同一个字母。
# 
# 
# 
# 
# 示例1:
# 
# 输入: pattern = "abba", s = "dog cat cat dog"
# 输出: true
# 
# 示例 2:
# 
# 输入:pattern = "abba", s = "dog cat cat fish"
# 输出: false
# 
# 示例 3:
# 
# 输入: pattern = "aaaa", s = "dog cat cat dog"
# 输出: false
# 
# 
# 
# 提示:
# 
# 
# 1 <= pattern.length <= 300
# pattern 只包含小写英文字母
# 1 <= s.length <= 3000
# s 只包含小写英文字母和 ' '
# s 不包含 任何前导或尾随对空格
# s 中每个单词都被 单个空格 分隔
# 
# 
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # 边界处理：如果pattern数组与s长度不一致，返回false：
        words = s.split()
        if len(pattern) != len(words):
            return False
        # 初始化哈希表用于存储pattern到word的对应关系：
        pattern_to_word = {}
        # 初始化一个集合用于存储已经有模式对照关系的word：
        word_set = set()
        # 遍历pattern数组：
        for i, pattern in enumerate(pattern):
            # 查看当前的pattern模式是否已经被记录：
            # 如果还未被记录：
            if pattern not in pattern_to_word:
                # 如果当前word已经对应了其他的pattern，返回false：
                if words[i] in word_set:
                    return False
                # 添加当前模式对应关系并更新word_set：
                pattern_to_word[pattern] = words[i]
                word_set.add(words[i])
            # 如果当前模式已经被记录，查看是否一致即可：
            if pattern_to_word[pattern] != words[i]:
                return False
        # 返回：
        return True
# @lc code=end



#
# @lcpr case=start
# "abba"\n"dog cat cat dog"\n
# @lcpr case=end

# @lcpr case=start
# "abba"\n"dog cat cat fish"\n
# @lcpr case=end

# @lcpr case=start
# "aaaa"\n"dog cat cat dog"\n
# @lcpr case=end

#

