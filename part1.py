import retro 

env = retro.make ('SuperMarioWorld-Snes', 'Start')

env.reset()

done = False



#CONTROL RAM DUMPS for BUTTON action
#RIGHT = [0, 0, 1, 0, 1, 0, 0, 1, 0]
#LEFT  = [0, 0, 1, 0, 1, 1, 1, 0, 0]
#JUMP  = [1, 0, 0, 1, 0, 0, 0, 1, 1]

while not done:
	
	env.render()								#frame render 
	action = [0, 0, 1, 0, 1, 0, 0, 1, 0]
	#REWARDS = EVERY FRAME HOW FAR MARIO MOVIES GIVES HIM REWARD FOR EVERY FRAME
	ob, rew, done, info = env.step(action)		#action dump [input of emulator for every frame]
	print("Action ", action, "Reward ", rew)
	#print("Image ", ob.shape, "Reward ",rew, "Done? ", done)
	#print("Info ", info)


