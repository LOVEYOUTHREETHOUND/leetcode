#
# @lc app=leetcode.cn id=225 lang=python3
# @lcpr version=30307
#
# [225] 用队列实现栈
#
# https://leetcode.cn/problems/implement-stack-using-queues/description/
#
# algorithms
# Easy (65.68%)
# Likes:    981
# Dislikes: 0
# Total Accepted:    495.2K
# Total Submissions: 754K
# Testcase Example:  '["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# 请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。
# 
# 实现 MyStack 类：
# 
# 
# void push(int x) 将元素 x 压入栈顶。
# int pop() 移除并返回栈顶元素。
# int top() 返回栈顶元素。
# boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。
# 
# 
# 
# 
# 注意：
# 
# 
# 你只能使用队列的标准操作 —— 也就是 push to back、peek/pop from front、size 和 is empty
# 这些操作。
# 你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
# 
# 
# 
# 
# 示例：
# 
# 输入：
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# 输出：
# [null, null, null, 2, 2, false]
# 
# 解释：
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // 返回 2
# myStack.pop(); // 返回 2
# myStack.empty(); // 返回 False
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= x <= 9
# 最多调用100 次 push、pop、top 和 empty
# 每次调用 pop 和 top 都保证栈不为空
# 
# 
# 
# 
# 进阶：你能否仅用一个队列来实现栈。
# 
#

# @lc code=start
from collections import deque
class MyStack:

    def __init__(self):
        # 初始化,使用collections库的deque模拟双端队列:
        self.q = deque()
        # 因为要求使用队列的标准操作(peek from front),栈顶元素位于队列尾部,无法直接读取,所以需要一个变量进行记录:
        self.top_elem = 0


    def push(self, x: int) -> None:
        # 入栈,更新栈顶元素值:
        self.q.append(x)
        self.top_elem = x
        

    def pop(self) -> int:
        # 出栈,因为队列标准操作中不能尾部pop,所以将尾部元素之前的所有元素全部pop->append到尾部元素之后,再将尾部元素pop即可:
        # 需要注意栈顶元素值的更新:
        size = len(self.q)
        while size > 2:
            self.q.append(self.q.popleft())
            size -= 1
        self.top_elem = self.q[0]
        self.q.append(self.q.popleft())
        return self.q.popleft()
        

    def top(self) -> int:
        # 读取栈顶元素:
        return self.top_elem
        

    def empty(self) -> bool:
        # 判空:
        if not self.q:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end



#
# @lcpr case=start
# ["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]\n
# @lcpr case=end

#

