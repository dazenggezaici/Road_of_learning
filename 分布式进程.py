# _*_ coding:utf-8 _*_
#__Author__=="Todd"
import random,time,queue
from multiprocessing.managers import BaseManager

#创建发送任务队列实例
task_queue = queue.Queue()
#创建接收结果队列实例
result_queue = queue.Queue()

#为了兼容windows10系统，用函数返回值
def get_task():
    global task_queue
    return task_queue
def get_result():
    global result_queue
    return result_queue
#从BaseManager继承QueueManager
class QueueManager(BaseManager):
    pass
#注册Queue到网络,callable参数关联Queue对象
def start_server():
    QueueManager.register('get_task_queue',callable=get_task)
    QueueManager.register('get_result_queue',callable=get_result)
    #绑定端口为5000,验证码为'abc'
    manager = QueueManager(address=('127.0.0.1',5000),authkey=b'abc')
    #启动Queue
    manager.start()
    #通过网络获取Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    #创建新任务
    for i in range(10):
        n = random.randint(0,10000)
        print('Put task %d...' %n)
        task.put(n)
    #获取结果
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=100)
        print('Result:%s' %r)

    #close
    manager.shutdown()
    print('master exit.')

if __name__=='__main__':
    start_server()