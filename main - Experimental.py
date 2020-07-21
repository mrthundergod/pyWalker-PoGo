import os, time, random

def autowalker():
	t1=time.time()
	print('Time to walk. Time: ', time.time())
	c=0
	mover=["adb shell input tap 736 1744", "adb shell input tap 976 1976", "adb shell input tap 734 2219", "adb shell input tap 496 1983"]
	
	stop_time=time.time()+3600*10
	while time.time() < stop_time:
		direction = random.choice(mover)
		time.sleep(random.randrange(5, 10))
		for i in range(random.randrange(5)):
			c+=1
			print('Step: ', c)
			os.system(direction)
			time.sleep(3)
	t2=time.time()
	print('Done walking for ', t2-t1)

def buddyfeeder():
	print('Buddy Feeding Time!')
	time.sleep(2)
	os.system('adb shell input tap 266 2196')		#Click Buddy
	time.sleep(3)
	os.system('adb shell input tap 555 1001')		#Click PLAY
	time.sleep(5)
	os.system('adb shell input tap 539 2136')		#Click Quick Treat
	time.sleep(5)
	os.system('adb shell input tap 508 2111')		#Click Berry
	time.sleep(5)
	os.system('adb shell input swipe 560 1536 549 617') #Throw Berry
	time.sleep(7)
	os.system('adb shell input tap 508 2111')		#Click Berry
	time.sleep(3)
	os.system('adb shell input swipe 560 1536 549 617') #Throw Berry
	time.sleep(7)
	os.system('adb shell input tap 508 2111')		#Click Berry
	time.sleep(3)
	os.system('adb shell input swipe 560 1536 549 617') #Throw Berry	
	time.sleep(10)
	print('Done, You buddy has joined you!')

def main():
	#buddyfeeder()
	autowalker()	

if __name__ == '__main__':
	main()





