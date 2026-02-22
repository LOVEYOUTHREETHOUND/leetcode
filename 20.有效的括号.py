#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30307
#
# [20] 有效的括号
#
# https://leetcode.cn/problems/valid-parentheses/description/
#
# algorithms
# Easy (45.37%)
# Likes:    4888
# Dislikes: 0
# Total Accepted:    2.4M
# Total Submissions: 5.4M
# Testcase Example:  '"()"\n"()[]{}"\n"(]"\n"([])"\n"([)]"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "()"
# 
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：s = "()[]{}"
# 
# 输出：true
# 
# 
# 示例 3：
# 
# 
# 输入：s = "(]"
# 
# 输出：false
# 
# 
# 示例 4：
# 
# 
# 输入：s = "([])"
# 
# 输出：true
# 
# 
# 示例 5：
# 
# 
# 输入：s = "([)]"
# 
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^4
# s 仅由括号 '()[]{}' 组成
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        nums_left = 0
        # 使用栈(先入后出)存储所有的左括号:
        left = []
        # 遍历s,遇到左括号就入栈,遇到右括号就检查栈顶元素是否匹配:
        for char in s:
            # 是左括号:入栈:
            if char in '([{':
                left.append(char)
                nums_left += 1
            # 是右括号:检查栈顶元素是不是对应的左括号:
            else:
                if left and left[-1] == self.leftOf(char):
                    left.pop()
                    nums_left -= 1
                else:
                    return False
        # 返回:
        return nums_left == 0
        
    # 辅助函数:对于特定的右括号,返回对应的左括号类型:
    def leftOf(self, char:str) -> str:
        if char == ')':
            return '('
        if char == ']':
            return '['
        if char == '}':
            return '{'

        
# @lc code=end



#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

# @lcpr case=start
# "([)]"\n
# @lcpr case=end

#

