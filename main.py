# Python program to illustrate a stop watch 
# using Tkinter 
#importing the required libraries 
import tkinter as Tkinter 
import math
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

def counter_label1(label1): 
	def count1(): 
		if running1: 
			global counter1 
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
	
# start function of the stopwatch 
def Start1(label1): 
	global running1 
	running1=True
	counter_label1(label1) 
	start1['state']='disabled'
	stop1['state']='normal'
	reset1['state']='normal'
	
# Stop function of the stopwatch 
def Stop1(): 
	global running1 
	start1['state']='normal'
	stop1['state']='disabled'
	reset1['state']='normal'
	running1 = False
	
# Reset function of the stopwatch 
def Reset1(label1): 
	global counter1 
	counter1=0
	
	# If rest is pressed after pressing stop. 
	if running1==False:	 
		reset1['state']='disabled'
		label1['text']='Welcome!'
	
	# If reset is pressed while the stopwatch is running. 
	else:				 
		label1['text']='Starting...'
	
root = Tkinter.Tk() 
root.title("Focus Biller") 
	
# Fixing the window size. 
root.minsize(width=250, height=70) 
root.attributes('-fullscreen', True)
label1 = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold") 
label1.pack() 
f = Tkinter.Frame(root) 
start1 = Tkinter.Button(f, text='Start', width=6, command=lambda:Start1(label1)) 
stop1 = Tkinter.Button(f, text='Stop',width=6,state='disabled', command=Stop1) 
reset1 = Tkinter.Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset1(label1)) 
f.pack(anchor = 'center',pady=5) 
start1.pack(side="left") 
stop1.pack(side ="left") 
reset1.pack(side="left") 
root.mainloop() 

