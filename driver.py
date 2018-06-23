from server import * 

print("please enter an option")
option = raw_input()
modify = Modify()
while(option != "exit"):
	if option =='play' and modify.play:
		modify.play()
	elif option=='pause' and not modify.play:
		modify.pause() 	
	elif option=='seek':
		print("in current song, enter number (in seconds) of where you would like to go to")
		seconds = input()
		modify.seek(seconds * 1000)

	elif option=='volume':
		print("enter volume from 0 to 100")
		percent = input()
		modify.volume(percent)
	elif option=='next':
		modify.next()
	elif option=='prev':
		modify.prev()
	elif option=="shuffle":
		modify.shuffle()
	print("please enter an option")
	option = raw_input()

