#
# @lc app=leetcode.cn id=151 lang=python3
# @lcpr version=30307
#
# [151] 反转字符串中的单词
#
# https://leetcode.cn/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (59.43%)
# Likes:    1383
# Dislikes: 0
# Total Accepted:    841.8K
# Total Submissions: 1.4M
# Testcase Example:  '"the sky is blue"\n"  hello world  "\n"a good   example"'
#
# 给你一个字符串 s ，请你反转字符串中 单词 的顺序。
# 
# 单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
# 
# 返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。
# 
# 注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "the sky is blue"
# 输出："blue is sky the"
# 
# 
# 示例 2：
# 
# 输入：s = "  hello world  "
# 输出："world hello"
# 解释：反转后的字符串中不能存在前导空格和尾随空格。
# 
# 
# 示例 3：
# 
# 输入：s = "a good   example"
# 输出："example good a"
# 解释：如果两个单词间有多余的空格，反转后的字符串需要将单词间的空格减少到仅有一个。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^4
# s 包含英文大小写字母、数字和空格 ' '
# s 中 至少存在一个 单词
# 
# 
# 
# 
# 
# 
# 
# 进阶：如果字符串在你使用的编程语言中是一种可变数据类型，请尝试使用 O(1) 额外空间复杂度的 原地 解法。
# 
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # 按照题给要求清除多余空格（双指针法）：
        chars = list(s)
        n = len(chars)
        slow = 0
        fast = 0
        while fast < n:
            # 读指针读到单词开头(不为空格)，开始准备处理：
            if chars[fast] != ' ':
                # 如果写指针不是为0（开头），需要写一个空格作为单词之间的分割：
                if slow != 0:
                    chars[slow] = ' '
                    slow += 1
                while fast < n and chars[fast] != ' ':
                    chars[slow] = chars[fast]
                    slow += 1
                    fast += 1
            
            # 读指针读到的是空格，则不需要做任何操作：
            else:
                fast += 1
        

            
            
        
        # 构建翻转函数（对于i和j索引之间的所有数组元素进行翻转操作）：
        def reverse(arr: List[str], i: int, j: int):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        # 将所有字母进行反转：
        chars = chars[: slow]
        n_new = len(chars)
        reverse(chars, 0, n_new - 1)

        # 以空格为分界，每一个单词内部进行翻转：
        char_start = 0
        for char_end in range(n_new + 1):
            # 找一个单词的结尾（遇到空格或者到达数组末尾，表示找到了一个单词的结尾）
            if char_end == n_new or chars[char_end] == ' ':
                reverse(chars, char_start, char_end - 1)
                char_start = char_end + 1
        # 返回： 
        return ''.join(chars)
# @lc code=end



#
# @lcpr case=start
# "the sky is blue"\n
# @lcpr case=end

# @lcpr case=start
# "  hello world  "\n
# @lcpr case=end

# @lcpr case=start
# "a good   example"\n
# @lcpr case=end

#

