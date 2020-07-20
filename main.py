# Python program to illustrate a stop watch 
# using Tkinter 
#importing the required libraries 
import math
from tkinter import *
from datetime import datetime 
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
running1 = False
running2 = False
running3 = False
running4 = False
running5 = False
lastStart1 = 0
lastStart2 = 0
lastStart3 = 0
lastStart4 = 0
lastStart5 = 0
warning_threshold = 1
revert_idle_threshold = 2

def counter_label1(label1): 
	def count1(): 
		global running1
		if running1: 
			global counter1, warning_threshold, revert_idle_threshold
			global running2 
			global running3
			global running4 
			global running5 
			running2=running3=running4=running5=False
			seconds = counter1 % 60
			minutes = math.floor(counter1 / 60)
			hours = math.floor(counter1 / 3600) 
	
			# To manage the intial delay. 
			if counter1==0:			 
				display1="Starting..."
			else: 
				string = f'{hours:02}:{minutes:02}:{seconds:02}' 
				display1=string 
	
			label1['text']=display1 # Or label.config(text=display) 
	
			# label.after(arg1, arg2) delays by 
			# first argument given in milliseconds 
			# and then calls the function given as second argument. 
			# Generally like here we need to call the 
			# function in which it is present repeatedly. 
			# Delays by 1000ms=1 seconds and call count again. 
			label1.after(1000, count1) 
			counter1 += 1
	
	# Triggering the start of the counter. 
	count1()	 
	
def counter_label2(label2, label1): 
	def count2(): 
		global running2
		if running2: 
			global counter2, warning_threshold, revert_idle_threshold
			global running1 
			global running3
			global running4 
			global running5 
			running1=running3=running4=running5=False
			seconds = counter2 % 60
			minutes = math.floor(counter2 / 60)
			hours = math.floor(counter2 / 3600) 
	
			# To manage the intial delay. 
			if counter2==0:			 
				display2="Starting..."
			else: 
				string = f'{hours:02}:{minutes:02}:{seconds:02}' 
				display2=string 
	
			label2['text']=display2 # Or label.config(text=display) 
	
			# label.after(arg1, arg2) delays by 
			# first argument given in milliseconds 
			# and then calls the function given as second argument. 
			# Generally like here we need to call the 
			# function in which it is present repeatedly. 
			# Delays by 1000ms=1 seconds and call count again. 
			

			counter2 += 1
			if lastStart2 + 60*revert_idle_threshold <= counter2:
				running2=False
				Start1(label1)
				label2.config(fg="lime",bg="black")
			elif lastStart2 + 60*warning_threshold <= counter2:
				if counter2 % 2 == 1:
					label2.config(fg="cyan",bg="red")
				else:
					label2.config(fg="lime",bg="black")
			else:
				label2.config(fg="lime",bg="black")

			label2.after(1000, count2) 
	
	# Triggering the start of the counter. 
	count2()	 

def counter_label3(label3, label1): 
	def count3(): 
		global running3
		if running3: 
			global counter3, warning_threshold, revert_idle_threshold
			global running1 
			global running2
			global running4 
			global running5 
			running1=running2=running4=running5=False
			seconds = counter3 % 60
			minutes = math.floor(counter3 / 60)
			hours = math.floor(counter3 / 3600) 
	
			# To manage the intial delay. 
			if counter3==0:			 
				display3="Starting..."
			else: 
				string = f'{hours:02}:{minutes:02}:{seconds:02}' 
				display3=string 
	
			label3['text']=display3 # Or label.config(text=display) 
	
			# label.after(arg1, arg2) delays by 
			# first argument given in milliseconds 
			# and then calls the function given as second argument. 
			# Generally like here we need to call the 
			# function in which it is present repeatedly. 
			# Delays by 1000ms=1 seconds and call count again. 
			

			counter3 += 1
			if lastStart3 + 60*revert_idle_threshold <= counter3:
				running3=False
				Start1(label1)
				label3.config(fg="lime",bg="black")
			elif lastStart3 + 60*warning_threshold <= counter3:
				if counter3 % 2 == 1:
					label3.config(fg="cyan",bg="red")
				else:
					label3.config(fg="lime",bg="black")
			else:
				label3.config(fg="lime",bg="black")

			label3.after(1000, count3) 
	
	# Triggering the start of the counter. 
	count3()	 

def counter_label4(label4, label1):
	def count4(): 
		global running4
		if running4: 
			global counter4, warning_threshold, revert_idle_threshold
			global running1 
			global running3
			global running2 
			global running5 
			running1=running3=running2=running5=False
			seconds = counter4 % 60
			minutes = math.floor(counter4 / 60)
			hours = math.floor(counter4 / 3600) 
	
			# To manage the intial delay. 
			if counter4==0:			 
				display4="Starting..."
			else: 
				string = f'{hours:02}:{minutes:02}:{seconds:02}' 
				display4=string 
	
			label4['text']=display4 # Or label.config(text=display) 
	
			# label.after(arg1, arg2) delays by 
			# first argument given in milliseconds 
			# and then calls the function given as second argument. 
			# Generally like here we need to call the 
			# function in which it is present repeatedly. 
			# Delays by 1000ms=1 seconds and call count again. 
			
			
			counter4 += 1
			if lastStart4 + 60*revert_idle_threshold <= counter4:
				running4=False
				Start1(label1)
				label4.config(fg="lime",bg="black")
			elif lastStart4 + 60*warning_threshold <= counter4:
				if counter4 % 2 == 1:
					label4.config(fg="cyan",bg="red")
				else:
					label4.config(fg="lime",bg="black")
			else:
				label4.config(fg="lime",bg="black")

			label4.after(1000, count4) 
	
	# Triggering the start of the counter. 
	count4()	 

def counter_label5(label5, label1): 
	def count5(): 
		global running5
		if running5: 
			global counter5, warning_threshold, revert_idle_threshold
			global running1 
			global running3
			global running4 
			global running2 
			running1=running3=running4=running2=False
			seconds = counter5 % 60
			minutes = math.floor(counter5 / 60)
			hours = math.floor(counter5 / 3600) 
	
			# To manage the intial delay. 
			if counter5==0:			 
				display5="Starting..."
			else: 
				string = f'{hours:02}:{minutes:02}:{seconds:02}' 
				display5=string 
	
			label5['text']=display5 # Or label.config(text=display) 
	
			# label.after(arg1, arg2) delays by 
			# first argument given in milliseconds 
			# and then calls the function given as second argument. 
			# Generally like here we need to call the 
			# function in which it is present repeatedly. 
			# Delays by 1000ms=1 seconds and call count again. 
			
			
			counter5 += 1
			if lastStart5 + 60*revert_idle_threshold <= counter5:
				running5=False
				Start1(label1)
				label5.config(fg="lime",bg="black")
			elif lastStart5 + 60*warning_threshold <= counter5:
				if counter5 % 2 == 1:
					label5.config(fg="cyan",bg="red")
				else:
					label5.config(fg="lime",bg="black")
			else:
				label5.config(fg="lime",bg="black")

			label5.after(1000, count5) 
	
	# Triggering the start of the counter. 
	count5()	 


# start function of the stopwatch 
def Start1(label1): 
	global running1, lastStart1 
	running1=running1==False
	lastStart1=counter1
	if running1:
		counter_label1(label1)

def Start2(label2, label1): 
	global running2, lastStart2 
	lastStart2=counter2
	if not running2:
		running2 = True
		counter_label2(label2, label1) 

def Start3(label3, label1): 
	global running3, lastStart3 
	lastStart3=counter3
	if not running3:
		running3 = True
		counter_label3(label3, label1)

def Start4(label4, label1): 
	global running4, lastStart4
	lastStart4=counter4
	if not running4:
		running4 = True
		counter_label4(label4, label1) 

def Start5(label5, label1): 
	global running5, lastStart5 
	
	lastStart5=counter5 
	if not running5:
		running5 = True
		counter_label5(label5, label1) 
	
# Stop function of the stopwatch 
def Stop(): 
	global running1, lastStart1, counter1 
	global running2, lastStart2, counter2
	global running3, lastStart3, counter3
	global running4, lastStart4, counter4
	global running5, lastStart5, counter5
	running1 = False
	running2 = False 
	running3 = False 
	running4 = False 
	running5 = False
	lastStart1=counter1 
	lastStart2=counter2 
	lastStart3=counter3 
	lastStart4=counter4 
	lastStart5=counter5
	
# Reset function of the stopwatch 
def Reset(): 
	global counter1, lastStart1
	global counter2, lastStart2
	global counter3, lastStart3
	global counter4, lastStart4
	global counter5, lastStart5
	counter1=lastStart1=0
	counter2=lastStart2=0
	counter3=lastStart3=0
	counter4=lastStart4=0
	counter5=lastStart5=0

def Exit(root):
	global counter1, counter2, counter3, counter4, counter5 
	print(f'{counter1:n}-{counter2:n}-{counter3:n}-{counter4:n}-{counter5:n}')
	root.destroy()
	
root = Tk() 
root.title("Focus Biller") 
	
# Fixing the window size. 
root.minsize(width=250, height=70) 
#root.attributes('-fullscreen', True)
Grid.columnconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 0, weight=1)
f = Frame(root) 
f.grid(row=0, column=0, sticky=N+E+S+W)


Grid.columnconfigure(f, 0, weight=1)
Grid.columnconfigure(f, 1, weight=1)
Grid.columnconfigure(f, 2, weight=1)
Grid.columnconfigure(f, 3, weight=1)
Grid.columnconfigure(f, 4, weight=1)

Grid.rowconfigure(f, 0, weight=5)
Grid.rowconfigure(f, 1, weight=5)
Grid.rowconfigure(f, 2, weight=1)

#f.pack(anchor = 'center', pady=5)
label1 = Label(f, text="Task Idle", fg="lime", bg="black", font="Verdana 30 bold") 
label1.grid(column=0, row=0, sticky=N+S+E+W)
#label1.pack(side="left")
label2 = Label(f, text="Task #1", fg="lime", bg="black", font="Verdana 30 bold") 
label2.grid(column=1, row=0, sticky=N+S+E+W)
#label2.pack(side="left")
label3 = Label(f, text="Task #2", fg="lime", bg="black", font="Verdana 30 bold") 
label3.grid(column=2, row=0, sticky=N+S+E+W)
#label3.pack(side="left")
label4 = Label(f, text="Task #3", fg="lime", bg="black", font="Verdana 30 bold") 
label4.grid(column=3, row=0, sticky=N+S+E+W)
#label4.pack(side="left")
label5 = Label(f, text="Task #4", fg="lime", bg="black", font="Verdana 30 bold") 
label5.grid(column=4, row=0, sticky=N+S+E+W)
#label5.pack(side="left") 

start1 = Button(f, text='Task Idle', width=6, command=lambda:Start1(label1)) 
start1.grid(column=0, row=1, sticky=N+S+E+W)

stop = Button(f, text='Stop',width=6, command=Stop) 
stop.grid(column=2, row=2, sticky=E+N+S)
reset = Button(f, text='Reset',width=6, command=Reset) 
reset.grid(column=3, row=2, sticky=E+N+S)
start2 = Button(f, text='Task #1', width=6, command=lambda:Start2(label2, label1)) 
start2.grid(column=1, row=1, sticky=N+S+E+W)
start3 = Button(f, text='Task #2', width=6, command=lambda:Start3(label3, label1)) 
start3.grid(column=2, row=1, sticky=N+S+E+W)
start4 = Button(f, text='Task #3', width=6, command=lambda:Start4(label4, label1)) 
start4.grid(column=3, row=1, sticky=N+S+E+W)
start5 = Button(f, text='Task #4', width=6, command=lambda:Start5(label5, label1)) 
start5.grid(column=4, row=1, sticky=N+S+E+W)
exitbutton = Button(f, text='End', width=4, command=lambda:Exit(root))
exitbutton.grid(column=4, row=2, sticky=E+N+S)



root.mainloop() 

