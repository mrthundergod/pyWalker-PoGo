import os, time, random



def autowalker():
	c=0
	mover=["adb shell input tap 325 194", "adb shell input tap 583 410", "adb shell input tap 351 655", "adb shell input tap 130 407"]
	
	stop_time=time.time()+60*1
	while time.time() < stop_time:
		direction = random.choice(mover)
		for i in range(random.randrage(4)):
			c+=1
			print('Step: ', c)
			os.system(direction)
			time.sleep(10)

if __name__ == '__main__':
	print('Time to walk. Time: ', time.time())
	autowalker()
	print('Done')
