import os, time, random
from multiprocessing import Pool

def task(name):
	print('working name{}, ID：{}'.format(name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('working down name{}, ID:{}'.format(name,(end-start)))

if __name__ == '__main__':
	print('now is main process,ID:{}'.format(os.getpid()))
	print('------------------------------------')

	p = Pool(4)
	for i in range(1, 6):
		p.apple_async(task, args(i,))
	p.close()
	print('the son_process is start')
	p.join()
	print('-----------------------------------')
	print('all process was runned, now is main process,ID:{}'.format(os.getpid()))
	