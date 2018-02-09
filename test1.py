# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1 # 初始化两个计数器a，b
#
#     def __iter__(self):
#         return self # 实例本身就是迭代对象，故返回自己
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b # 计算下一个值
#         if self.a > 1000000: # 退出循环的条件
#             raise StopIteration()
#         return self.a # 返回下一个值
# for i in Fib():
# 	print(i)

from queue import Queue
q = Queue()
for i in range(3):
    q.put(i)

while not q.empty():
    print(q.get())



from queue import LifoQueue
q = LifoQueue()
for i in range(3):
    q.put(i)

while not q.empty():
    print(q.get())