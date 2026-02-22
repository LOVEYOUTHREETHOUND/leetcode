#
# @lc app=leetcode.cn id=622 lang=python3
# @lcpr version=30307
#
# [622] 设计循环队列
#
# https://leetcode.cn/problems/design-circular-queue/description/
#
# algorithms
# Medium (47.10%)
# Likes:    585
# Dislikes: 0
# Total Accepted:    173.2K
# Total Submissions: 367.8K
# Testcase Example:  '["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]\n' +
  # '[[3],[1],[2],[3],[4],[],[],[],[4],[]]'
#
# 设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于
# FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。
# 
# 
# 循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。
# 
# 你的实现应该支持如下操作：
# 
# 
# MyCircularQueue(k): 构造器，设置队列长度为 k 。
# Front: 从队首获取元素。如果队列为空，返回 -1 。
# Rear: 获取队尾元素。如果队列为空，返回 -1 。
# enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
# deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
# isEmpty(): 检查循环队列是否为空。
# isFull(): 检查循环队列是否已满。
# 
# 
# 
# 
# 示例：
# 
# MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
# circularQueue.enQueue(1);  // 返回 true
# circularQueue.enQueue(2);  // 返回 true
# circularQueue.enQueue(3);  // 返回 true
# circularQueue.enQueue(4);  // 返回 false，队列已满
# circularQueue.Rear();  // 返回 3
# circularQueue.isFull();  // 返回 true
# circularQueue.deQueue();  // 返回 true
# circularQueue.enQueue(4);  // 返回 true
# circularQueue.Rear();  // 返回 4
# 
# 
# 
# 提示：
# 
# 
# 所有的值都在 0 至 1000 的范围内；
# 操作数将在 1 至 1000 的范围内；
# 请不要使用内置的队列库。
# 
# 
#

# @lc code=start
class MyCircularQueue:

    def __init__(self, k: int):
        # 设置队列容量为k+1:
        self.capacity = k + 1
        # 初始化队列:
        self.q = [0] * self.capacity
        # 初始化front,rear指针:
        self.front, self.rear = 0, 0

    def enQueue(self, value: int) -> bool:
      # 边界:队列已满,不能插入,返回false:
      if self.isFull():
        return False
      # 队尾插入元素:
      self.q[self.rear] = value
      self.rear = (self.rear + 1) % self.capacity
      return True
        

    def deQueue(self) -> bool:
      # 边界:队列已空,不能删除,返回false:
      if self.isEmpty():
        return False
      #队首删除元素:
      self.front = (self.front + 1) % self.capacity
      return True
        

    def Front(self) -> int:
      # 边界:队列为空返回-1:
      if self.isEmpty():
        return -1
      # 获取队首元素:
      return self.q[self.front]
        

    def Rear(self) -> int:
      # 边界:队列为空返回-1:
      if self.isEmpty():
        return -1
      # 获取队尾元素:
      return self.q[(self.rear - 1) % self.capacity]
        

    def isEmpty(self) -> bool:
      # 判空:front指针和rear指针重合时为空:
      if self.front == self.rear:
        return True
      return False
        

    def isFull(self) -> bool:
      # 判满:rear指针在front指针的前一位:
      if (self.rear + 1) % self.capacity == self.front:
        return True
      return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end



#
# @lcpr case=start
# ["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]\n[[3],[1],[2],[3],[4],[],[],[],[4],[]]\n
# @lcpr case=end

#

