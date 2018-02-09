#windows平台多进程
# import os
# import time
# from multiprocessing import Process

# def run_proc(name):
# 	print('Run child process %s (%s)...' % (name,os.getpid()))

# if __name__=='__main__':
# 	s=time.time()
# 	print('Parent process %s' % os.getpid())
# 	p = Process(target=run_proc,args=('test',))
# 	print('Child process will start.')
# 	p.start()
# 	p.join()
# 	print('Child process end.')
# 	e=time.time()
# 	print(e-s)

#Pool如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
# from multiprocessing import Pool
# import os,time,random  #  random随机数生成模块

# def long_time_task(name):
# 	print('Run task %s (%s)...' % (name,os.getpid()))
# 	start = time.time()
# 	time.sleep(random.random()*3) 
# 	end = time.time()
# 	print('Task %s runs %0.2f seconds.' % (name,(end-start)))

# if __name__=='__main__':
# 	s = time.time()
# 	print('Parent process %s' %os.getpid())
# 	p = Pool(5)
# 	for i in range(5):
# 		p.apply_async(long_time_task,args=(i,))
# 	print('Waiting for all subprocesses done...')
# 	p.close()
# 	p.join()
# 	print('All subprocesses done.')
# 	e = time.time()
# 	print(e-s)

# # 子进程
# import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# print('Exit code:',r)

# import subprocess

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('GBK'))
# print('Exit code:', p.returncode)

#下面是实例############################################
from multiprocessing import Process,Queue  #  导入相关库
import os,time,random

#写数据进程执行的代码:
def write(q):
	print('Process to write %s' % os.getpid())
	for value in ['A','B','C']:
		print('Put %s to queue..' % value)
		q.put(value)
		time.sleep(random.random())

#读数据进程执行的代码:
def read(q):
	print('Process to read %s' % os.getpid())
	while True:
		value=q.get(True)
		print('Get %s from queue.' % value)

if __name__ == '__main__':
	#父进程创建Queue,并传给各个子程序
	s=time.time()
	q = Queue()
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))
	#启动子程序
	pr.start()
	pw.start()
	pw.join()
	pr.terminate()
	e=time.time()
	print('time=%s'%(e-s))