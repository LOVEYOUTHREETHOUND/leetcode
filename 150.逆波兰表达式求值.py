#
# @lc app=leetcode.cn id=150 lang=python3
# @lcpr version=30307
#
# [150] 逆波兰表达式求值
#
# https://leetcode.cn/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (57.17%)
# Likes:    1059
# Dislikes: 0
# Total Accepted:    538.8K
# Total Submissions: 942.3K
# Testcase Example:  '["2","1","+","3","*"]\n' +
  # '["4","13","5","/","+"]\n' +
  # '["10","6","9","3","+","-11","*","/","*","17","+","5","+"]'
#
# 给你一个字符串数组 tokens ，表示一个根据 逆波兰表示法 表示的算术表达式。
# 
# 请你计算该表达式。返回一个表示表达式值的整数。
# 
# 注意：
# 
# 
# 有效的算符为 '+'、'-'、'*' 和 '/' 。
# 每个操作数（运算对象）都可以是一个整数或者另一个表达式。
# 两个整数之间的除法总是 向零截断 。
# 表达式中不含除零运算。
# 输入是一个根据逆波兰表示法表示的算术表达式。
# 答案及所有中间计算结果可以用 32 位 整数表示。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：tokens = ["2","1","+","3","*"]
# 输出：9
# 解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
# 
# 
# 示例 2：
# 
# 输入：tokens = ["4","13","5","/","+"]
# 输出：6
# 解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
# 
# 
# 示例 3：
# 
# 输入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# 输出：22
# 解释：该算式转化为常见的中缀算术表达式为：
# ⁠ ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 
# 
# 
# 提示：
# 
# 
# 1 <= tokens.length <= 10^4
# tokens[i] 是一个算符（"+"、"-"、"*" 或 "/"），或是在范围 [-200, 200] 内的一个整数
# 
# 
# 
# 
# 逆波兰表达式：
# 
# 逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。
# 
# 
# 平常使用的算式则是一种中缀表达式，如 ( 1 + 2 ) * ( 3 + 4 ) 。
# 该算式的逆波兰表达式写法为 ( ( 1 2 + ) ( 3 4 + ) * ) 。
# 
# 
# 逆波兰表达式主要有以下两个优点：
# 
# 
# 去掉括号后表达式无歧义，上式即便写成 1 2 + 3 4 + * 也可以依据次序计算出正确结果。
# 适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中
# 
# 
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 初始化栈用于计算:
        stk = []
        # 计算:
        for token in tokens:
          if token in '+-*/':
            # 获取栈顶的两个数用于进行计算,first用于存储二元运算的第一个数,second用于存储第二个数:
            second = stk.pop()
            first = stk.pop()
            if token == '+':
              stk.append(first + second)
            if token == '-':
              stk.append(first - second)
            if token == '*':
              stk.append(first * second)
            if token == '/':
              stk.append(int(first / second))
          else:
            stk.append(int(token))             

        # 返回:
        return stk.pop()
# @lc code=end



#
# @lcpr case=start
# ["2","1","+","3","*"]\n
# @lcpr case=end

# @lcpr case=start
# ["4","13","5","/","+"]\n
# @lcpr case=end

# @lcpr case=start
# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]\n
# @lcpr case=end

#

