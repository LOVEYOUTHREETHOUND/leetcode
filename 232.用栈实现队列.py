#
# @lc app=leetcode.cn id=232 lang=python3
# @lcpr version=30307
#
# [232] 用栈实现队列
#
# https://leetcode.cn/problems/implement-queue-using-stacks/description/
#
# algorithms
# Easy (68.15%)
# Likes:    1266
# Dislikes: 0
# Total Accepted:    596.7K
# Total Submissions: 875.6K
# Testcase Example:  '["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
# 
# 实现 MyQueue 类：
# 
# 
# void push(int x) 将元素 x 推到队列的末尾
# int pop() 从队列的开头移除并返回元素
# int peek() 返回队列开头的元素
# boolean empty() 如果队列为空，返回 true ；否则，返回 false
# 
# 
# 说明：
# 
# 
# 你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty
# 操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# 输出：
# [null, null, null, 1, 1, false]
# 
# 解释：
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false
# 
# 
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= x <= 9
# 最多调用 100 次 push、pop、peek 和 empty
# 假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）
# 
# 
# 
# 
# 进阶：
# 
# 
# 你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。
# 
# 
#

# @lc code=start
class MyQueue:

    def __init__(self):
        # 初始化:使用两个栈底背靠背的栈来模拟实现FIFO队列:
        self.s1 = []
        self.s2 = []


    def push(self, x: int) -> None:
        # 向队列中添加元素:使用s2 append:
        self.s2.append(x)
        

    def pop(self) -> int:
        # 从FIFO队列中弹出元素:使用s1 pop:
        # 需要先调用peek保证s1不为空:
        self.peek()
        return self.s1.pop()
        

    def peek(self) -> int:
        # 查看最开始的元素(位于s1的最左端):
        # 需要处理特殊情况:如果队列中元素全部都在s2中,那么第一个元素处于s2的栈底,无法取出,所以应该先将s2的元素依次push入s1,这样操作队列本身并不会改变:
        if not self.s1:
            while self.s2:
                self.s1.append(self.s2.pop())
        return self.s1[-1]
        

    def empty(self) -> bool:
        # 判空:两个栈中都没有元素时队列为空:
        if not self.s1 and not self.s2:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end



#
# @lcpr case=start
# ["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]\n
# @lcpr case=end

#

