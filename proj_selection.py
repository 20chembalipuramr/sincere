def ps():
	from password_manager import pm
	from snap import sp
	import os
	proj_selection=input("What project would you like to run?\n1---Snap\n2---Password Manager\n")
	os.system('clear')
	if proj_selection=="1":
		sp()
	elif proj_selection=="2":
		pm()
	else:
		print("Invalid selection, please try again")			
		ps()