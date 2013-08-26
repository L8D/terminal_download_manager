import os,urllib
"""
The Ripper Download Manager v0.1
A vertasile little tool to manage your downloads but without a gui
Please contact me for any thing I can help with.
mail: la.yohda.stasella.1234@gmail.com
Skype: ripperhf1
Facebook: facebook.com/hasan.saad.980
github: github.com/ripperhf
"""


class Manager():
	def __init__(self):
		print """
The Ripper Download Manager v0.1
A vertasile little tool to manage your downloads but without a gui
Please contact me for any thing I can help with.
mail: la.yohda.stasella.1234@gmail.com
Skype: ripperhf1
Facebook: facebook.com/hasan.saad.980
github: github.com/ripperhf
"""
		self.manual="""	
			1-Command 1: single
			#Wait until asked for input
			#input format: url filename
			#example:  http://www.whatever.com/whatever.txt something.txt
			# Leaving filename empty will result in it being named according to original filename
			#example: http://www.whatever.com/whatever.txt 
			# ^ This would name the file something.txt
			#Warning: Do not use spaces in urls
			#Warning: Use www. or some other thing in urls. Don't put something like:
			# shit.com and put instead www.shit.com
			# And make sure to not forget the .com or .gov or whatever the hell you're using :P
			#After that input the location when asked for it

			2-Command 2:batch
			#Wait until asked for input
			#Enter download location
			#from now on on every line 
			#you use the same input format as that of single downloading
			#and you put 'done' without the quotes when you're done with adding downloads
			#example:
			www.shit.com/shit1.txt filename.shit
			www.shit.com/shit2.txt filename2.shit
			done
			"""
	def take_commands(self):
		while True:
			command=raw_input("Your wish is my command\n(type help for a manual on how to use this) : ")
			if command=="quit":
				break
			elif command=="help":
				print self.manual
			elif command=="single":
				self.add_download_single()
			elif command=="batch":
				self.batch_download()
			else:
				print "Command unknown.Sorry for the inconvenience."

	def add_download_single(self,user_input='',location=''):
		input_list=[]
		if user_input=='':
			user_input=raw_input("Enter required info: ")
		input_list=user_input.split(" ")
		if "http://" not in input_list[0] and "https://" not in input_list[0]:
			input_list[0]="http://"+input_list[0]
		if len(input_list)==1:
			something=input_list[0].split("/")
			input_list.append(something[len(something)-1])
		if location=='':
			location=raw_input("Enter download location: ")
		os.chdir(location)
		urllib.urlretrieve(input_list[0],input_list[1])
		print input_list[1]+" is downloaded."
	def batch_download(self):
		location=raw_input("Enter location of downloads: ")
		list_of_user_inputs=[]
		while True:
			x=raw_input('Input: ')
			if x=='done':
				break
			list_of_user_inputs.append(x)
		for x in list_of_user_inputs:
			self.add_download_single(user_input=x,location=location)
		print "Mischief managed"
manager1=Manager()
manager1.take_commands()
