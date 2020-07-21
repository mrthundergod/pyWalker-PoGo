import os, time, random

def autowalker():
	c=0
	mover=["adb shell input tap 325 194", "adb shell input tap 583 410", "adb shell input tap 351 655", "adb shell input tap 130 407"]
	
	stop_time=time.time()+3600*10
	while time.time() < stop_time:
		direction = random.choice(mover)
		for i in range(random.randrange(4)):
			c+=1
			print('Step: ', c)
			os.system(direction)
			time.sleep(10)

if __name__ == '__main__':
	t1=time.time()
	print('Time to walk. Time: ', time.time())
	autowalker()
	t2=time.time()
	print('Done walking for ', t2-t1)

#TEST

# mrthundergod
# 528.5Km walked

#shadowpriestess
# 7km



