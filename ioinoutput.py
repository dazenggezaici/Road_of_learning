# try:
# 	f = open(r'C:\ProgramData\Anaconda3\Scripts\test\text.txt','r')
# 	print(f.read())

# except IOError as e:
# 	print("该文件不存在！")

# finally:
# 	if f:
#  		f.close()

#	上面方法等同于下，但下面的代码更加简洁且不会吧f.close()忘记！

try:
	with open(r'C:\ProgramData\Anaconda3\Scripts\test\text.txt', 'r') as f:
		print("readline:",f.readline())
		print("readlines:",f.readlines(),'\r\n')#  上面一行代码将“1”取出，所以改行代码只有“2-6”！
		print("read:",f.read())#  上面两行代码已经将全部内容取出，所以该行代码不会有内容！

except IOError as e:
	print("该文件不存在！")