#
# @lc app=leetcode.cn id=641 lang=python3
# @lcpr version=30307
#
# [641] 设计循环双端队列
#
# https://leetcode.cn/problems/design-circular-deque/description/
#
# algorithms
# Medium (56.46%)
# Likes:    257
# Dislikes: 0
# Total Accepted:    79.9K
# Total Submissions: 141.6K
# Testcase Example:  '["MyCircularDeque","insertLast","insertLast","insertFront","insertFront","getRear","isFull","deleteLast","insertFront","getFront"]\n' +
  # '[[3],[1],[2],[3],[4],[],[],[],[4],[]]'
#
# 设计实现双端队列。
# 
# 实现 MyCircularDeque 类:
# 
# 
# MyCircularDeque(int k) ：构造函数,双端队列最大为 k 。
# boolean insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true ，否则返回 false 。
# boolean insertLast() ：将一个元素添加到双端队列尾部。如果操作成功返回 true ，否则返回 false 。
# boolean deleteFront() ：从双端队列头部删除一个元素。 如果操作成功返回 true ，否则返回 false 。
# boolean deleteLast() ：从双端队列尾部删除一个元素。如果操作成功返回 true ，否则返回 false 。
# int getFront() )：从双端队列头部获得一个元素。如果双端队列为空，返回 -1 。
# int getRear() ：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1 。
# boolean isEmpty() ：若双端队列为空，则返回 true ，否则返回 false  。
# boolean isFull() ：若双端队列满了，则返回 true ，否则返回 false 。
# 
# 
# 
# 
# 示例 1：
# 
# 输入
# ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront",
# "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# 输出
# [null, true, true, true, false, 2, true, true, true, 4]
# 
# 解释
# MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
# circularDeque.insertLast(1);                    // 返回 true
# circularDeque.insertLast(2);                    // 返回 true
# circularDeque.insertFront(3);                    // 返回 true
# circularDeque.insertFront(4);                    // 已经满了，返回 false
# circularDeque.getRear();                  // 返回 2
# circularDeque.isFull();                        // 返回 true
# circularDeque.deleteLast();                    // 返回 true
# circularDeque.insertFront(4);                    // 返回 true
# circularDeque.getFront();                // 返回 4
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= k <= 1000
# 0 <= value <= 1000
# insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty,
# isFull  调用次数不大于 2000 次
# 
# 
#

# @lc code=start
class MyCircularDeque:

    def __init__(self, k: int):
      # 队列容量:
      self.capacity = k + 1
      # 初始化队列:
      self.q = [0] * self.capacity
      # 初始化front和rear指针:
      self.front = 0
      self.rear = 0


    def insertFront(self, value: int) -> bool:
      # 边界:队列已经满时不能插入:
      if self.isFull():
        return False
      # 在队列前面插入:将front指针先左移,再对新的front指针所指的位置进行赋值:
      self.front = (self.front - 1) % self.capacity
      self.q[self.front] = value
      return True
        

    def insertLast(self, value: int) -> bool:
      # 边界:队列已经满时不能插入:
      if self.isFull():
        return False
      # 在队列后面插入:因为是左闭右开,所以先对rear指针所指的位置进行赋值,再将rear指针右移:
      self.q[self.rear] = value
      self.rear = (self.rear + 1) % self.capacity
      return True
        

    def deleteFront(self) -> bool:
      # 边界:队列已经为空时不能删除:
      if self.isEmpty():
        return False
      # 删除队列头元素:直接将front指针右移:
      self.front = (self.front + 1) % self.capacity
      return True
        

    def deleteLast(self) -> bool:
      # 边界:队列已经为空时不能删除:
      if self.isEmpty():
        return False
      # 删除队列尾元素:直接将rear指针左移:
      self.rear = (self.rear - 1) % self.capacity
      return True
        

    def getFront(self) -> int:
      # 边界:队列为空时返回-1:
      if self.isEmpty():
        return -1
      return self.q[self.front]
        

    def getRear(self) -> int:
      # 边界:队列为空时返回-1:
      if self.isEmpty():
        return -1
      return self.q[(self.rear - 1) % self.capacity]

    def isEmpty(self) -> bool:
      # 判空:front指针和rear指针重合:
      if self.front == self.rear:
        return True
      return False
        

    def isFull(self) -> bool:
      # 判满:rear指针和front指针相邻(也就是说k+1的环形数组容量里面有一个位置不处于[front, rear)范围之间):
      if (self.rear + 1) % self.capacity == self.front:
        return True
      return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end



#
# @lcpr case=start
# ["MyCircularDeque","insertLast","insertLast","insertFront","insertFront","getRear","isFull","deleteLast","insertFront","getFront"]\n[[3],[1],[2],[3],[4],[],[],[],[4],[]]\n
# @lcpr case=end

#

