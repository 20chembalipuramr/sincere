def pm():
	import os
	entering=True
	accessing=True

	passwords = [[], 
  	           [],
    	         []]

	while entering==True:
		os.system('clear')
		passwords[0].append(input("Please enter the account name\n"))
		passwords[1].append(input("Please enter the username\n"))
		passwords[2].append(input("Please enter the password\n"))
		os.system('clear')
		again=input("Would you like to enter anther account? (y/n)\n")
		os.system('clear')
		if again == "n":
			entering=False

	while accessing==True:
		account=input("What account would you like to look up the password for?\n")
		os.system('clear')
		try:
			index=passwords[0].index(account)
		except:
			print("That account is not on our database? Please try again\n")
		else:
			account=passwords[0][index]
			username=passwords[1][index]
			password=passwords[2][index]
			print(f"The account name is {account}\nThe username is {username}\nThe password is {password}")
			continueIndexing=input("Would you like to contine searching for passwords? (y/n)\n")
			os.stsem('clear')
			if continueIndexing == "n":
				continueIndexing=False