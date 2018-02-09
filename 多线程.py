# 多任务可以由多进程完成，也可以由一个进程内的多线程完成。

# 我们前面提到了进程是由若干线程组成的，一个进程至少有一个线程。

# 由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。
import time,threading  #  多线程 cpu上的线程跟软件层面上线程没有直接关系！

def loop():
	print('thread %s is runing...' % threading.current_thread().name)
	n = 0
	while n < 5:
		n = n+1
		print('thread %s >>> %s' % (threading.current_thread().name,n))
		time.sleep(1)
	print('thread %s ended.' % threading.current_thread().name)

# print('thread %s is runing...' % threading.current_thread().name)
# t = threading.Thread(target=loop,name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended' % threading.current_thread().name)

balance = 0
lock = threading.Lock()

def change_it(n):
	global balance  #定义全局变量
	balance +=n
	balance -=n

def run_thread(n):
	for i in range(100000):
		lock.acquire()  #获取锁
		try:
			change_it(i)
		finally:
			lock.release()  #释放锁

t1 = threading.Thread(target=run_thread, args=(18,))
t2 = threading.Thread(target=run_thread, args=(18,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)