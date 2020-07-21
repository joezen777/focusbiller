# Python program to illustrate a stop watch 
# using Tkinter 
#importing the required libraries 
import math
from tkinter import *
from datetime import datetime 
import simpleaudio as sa
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
warning_threshold = 10
last_minute_threshold = 14
last_ten_seconds_threshold = 14.8333
revert_idle_threshold = 15


def counter_label1(label1): 
	def count1(): 
		global running1
		if running1: 
			global counter1, warning_threshold, revert_idle_threshold
			global running2 
			global running3
			global running4 
			global running5 
			label1.config(bg="white")
			running2=running3=running4=running5=False
			seconds = counter1 % 60
			minutes = math.floor((counter1 % 3600) / 60)
			hours = math.floor(counter1 / 3600) 
	
			# To manage the intial delay. 
			if counter1==0:			 
				display1="00:00:00"
			else: 
				string = " {hours:02}:{minutes:02}:{seconds:02}".format(hours=hours, minutes=minutes, seconds=seconds) 
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
		else:
			label1.config(fg="lime",bg="black")
	
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
			label2.config(bg="red4")
			running1=running3=running4=running5=False
			seconds = counter2 % 60
			minutes = math.floor((counter2 % 3600) / 60)
			hours = math.floor(counter2 / 3600) 
	
			# To manage the intial delay. 
			if counter2==0:			 
				display2="00:00:00"
			else: 
				string = " {hours:02}:{minutes:02}:{seconds:02}".format(hours=hours, minutes=minutes, seconds=seconds) 
				display2=string 
	
			label2['text']=display2 # Or label.config(text=display) 
	
			# label.after(arg1, arg2) delays by 
			# first argument given in milliseconds 
			# and then calls the function given as second argument. 
			# Generally like here we need to call the 
			# function in which it is present repeatedly. 
			# Delays by 1000ms=1 seconds and call count again. 
			

			counter2 += 1
			lastStart = lastStart2
			counter = counter2 
			label = label2
			if lastStart + 60*revert_idle_threshold <= counter:
				running2=False
				Start1(label1)
				PlayFailure()
				label.config(fg="lime",bg="black")
			elif lastStart + 60*warning_threshold <= counter:
				if counter % 2 == 1:
					if lastStart + 60*last_minute_threshold <= counter:
						PlayKlaxon()
					else:
						PlayBlip()
					label.config(fg="cyan",bg="red")
				else:
					if lastStart + 60*last_ten_seconds_threshold <= counter:
						PlayKlaxon()
					label.config(fg="lime",bg="red4")
			else:
				label.config(fg="lime",bg="red4")

			label.after(1000, count2) 
		else:
			label2.config(fg="lime",bg="black")
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
			label3.config(bg="gold4")
			running1=running2=running4=running5=False
			seconds = counter3 % 60
			minutes = math.floor((counter3 % 3600) / 60)
			hours = math.floor(counter3 / 3600) 
	
			# To manage the intial delay. 
			if counter3==0:			 
				display3="00:00:00"
			else: 
				string = " {hours:02}:{minutes:02}:{seconds:02}".format(hours=hours, minutes=minutes, seconds=seconds)
				display3=string 
	
			label3['text']=display3 # Or label.config(text=display) 
	
			# label.after(arg1, arg2) delays by 
			# first argument given in milliseconds 
			# and then calls the function given as second argument. 
			# Generally like here we need to call the 
			# function in which it is present repeatedly. 
			# Delays by 1000ms=1 seconds and call count again. 
			

			counter3 += 1
			lastStart = lastStart3
			counter = counter3 
			label = label3
			if lastStart + 60*revert_idle_threshold <= counter:
				running3=False
				Start1(label1)
				PlayFailure()
				label.config(fg="lime",bg="black")
			elif lastStart + 60*warning_threshold <= counter:
				if counter % 2 == 1:
					if lastStart + 60*last_minute_threshold <= counter:
						PlayKlaxon()
					else:
						PlayBlip()
					label.config(fg="cyan",bg="red")
				else:
					if lastStart + 60*last_ten_seconds_threshold <= counter:
						PlayKlaxon()
					label.config(fg="lime",bg="gold4")
			else:
				label.config(fg="lime",bg="gold4")

			label.after(1000, count3) 
		else:
			label3.config(fg="lime",bg="black")
	
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
			label4.config(bg="dark green")
			running1=running3=running2=running5=False
			seconds = counter4 % 60
			minutes = math.floor((counter4 % 3600) / 60)
			hours = math.floor(counter4 / 3600) 
	
			# To manage the intial delay. 
			if counter4==0:			 
				display4="00:00:00"
			else: 
				string = " {hours:02}:{minutes:02}:{seconds:02}".format(hours=hours, minutes=minutes, seconds=seconds)
				display4=string 
	
			label4['text']=display4 # Or label.config(text=display) 
	
			# label.after(arg1, arg2) delays by 
			# first argument given in milliseconds 
			# and then calls the function given as second argument. 
			# Generally like here we need to call the 
			# function in which it is present repeatedly. 
			# Delays by 1000ms=1 seconds and call count again. 
			
			
			counter4 += 1
			lastStart = lastStart4
			counter = counter4
			label = label4
			if lastStart + 60*revert_idle_threshold <= counter:
				running4=False
				Start1(label1)
				PlayFailure()
				label.config(fg="lime",bg="black")
			elif lastStart + 60*warning_threshold <= counter:
				if counter % 2 == 1:
					if lastStart + 60*last_minute_threshold <= counter:
						PlayKlaxon()
					else:
						PlayBlip()
					label.config(fg="cyan",bg="red")
				else:
					if lastStart + 60*last_ten_seconds_threshold <= counter:
						PlayKlaxon()
					label.config(fg="lime",bg="dark green")
			else:
				label.config(fg="lime",bg="dark green")

			label.after(1000, count4) 
		else:
			label4.config(fg="lime",bg="black")
	
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
			label5.config(bg="blue4")
			running1=running3=running4=running2=False
			seconds = counter5 % 60
			minutes = math.floor((counter5 % 3600) / 60)
			hours = math.floor(counter5 / 3600) 
	
			# To manage the intial delay. 
			if counter5==0:			 
				display5="00:00:00"
			else: 
				string = " {hours:02}:{minutes:02}:{seconds:02}".format(hours=hours, minutes=minutes, seconds=seconds)
				display5=string 
	
			label5['text']=display5 # Or label.config(text=display) 
	
			# label.after(arg1, arg2) delays by 
			# first argument given in milliseconds 
			# and then calls the function given as second argument. 
			# Generally like here we need to call the 
			# function in which it is present repeatedly. 
			# Delays by 1000ms=1 seconds and call count again. 
			
			
			counter5 += 1
			lastStart = lastStart5
			counter = counter5
			label = label5
			if lastStart + 60*revert_idle_threshold <= counter:
				running5=False
				Start1(label1)
				PlayFailure()
				label.config(fg="lime",bg="black")
			elif lastStart + 60*warning_threshold <= counter:
				if counter % 2 == 1:
					if lastStart + 60*last_minute_threshold <= counter:
						PlayKlaxon()
					else:
						PlayBlip()
					label.config(fg="cyan",bg="red")
				else:
					if lastStart + 60*last_ten_seconds_threshold <= counter:
						PlayKlaxon()
					label.config(fg="lime",bg="blue4")
			else:
				label.config(fg="lime",bg="blue4")

			label.after(1000, count5) 
		else:
			label5.config(fg="lime",bg="black")
	
	# Triggering the start of the counter. 
	count5()	 


# start function of the stopwatch 
def Start1(label1): 
	global running1, lastStart1 
	running1=running1==False
	lastStart1=counter1
	counter_label1(label1)

def Start2(label2, label1): 
	global running2, lastStart2 
	lastStart2=counter2
	if not running2:
		running2 = True
		counter_label2(label2, label1)
	else:
		PlayReset() 

def Start3(label3, label1): 
	global running3, lastStart3 
	lastStart3=counter3
	if not running3:
		running3 = True
		counter_label3(label3, label1)
	else:
		PlayReset()

def Start4(label4, label1): 
	global running4, lastStart4
	lastStart4=counter4
	if not running4:
		running4 = True
		counter_label4(label4, label1) 
	else:
		PlayReset()

def Start5(label5, label1): 
	global running5, lastStart5 
	
	lastStart5=counter5 
	if not running5:
		running5 = True
		counter_label5(label5, label1) 
	else:
		PlayReset()

def TotalTime(label6):
	def showtime():
		global counter1, counter2, counter3, counter4, counter5
		counter6 = counter1 + counter2 + counter3 + counter4 + counter5
		seconds = counter6 % 60
		minutes = math.floor((counter6 % 3600) / 60)
		hours = math.floor(counter6 / 3600)
		now = datetime.now()
		tstamp = now.strftime("%Y-%m-%d %H:%M:%S")
		string = "{hours:02}:{minutes:02}:{seconds:02}".format(hours=hours, minutes=minutes, seconds=seconds)
		display6=string 
		if counter6 % 300 == 0:
			print("{tstamp}	{display6}	{counter1}	{counter2}	{counter3}	{counter4}	{counter5}".format(tstamp=tstamp, display6=display6, counter1=counter1, counter2=counter2, counter3=counter3, counter4=counter4, counter5=counter5))
		
		label6['text']=display6 
		label6.after(1000,showtime)
	showtime()
	
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

def PlayBlip():
	PlaySound("HatchBlip32.wav")

def PlayKlaxon():
	PlaySound("HatchKlaxon32.wav")

def PlayReset():
	PlaySound("HatchReset32.wav")

def PlayFailure():
	PlaySound("HatchErupt32.wav")


def PlaySound(soundFile):
	wave_obj = sa.WaveObject.from_wave_file(soundFile)
	#play_obj = 
	wave_obj.play()
	# play_obj.wait_done()  # Wait until sound has finished playing

def Exit(root):
	global counter1, counter2, counter3, counter4, counter5 
	
	print("{counter1:n}-{counter2:n}-{counter3:n}-{counter4:n}-{counter5:n}".format(counter1=counter1,counter2=counter2,counter3=counter3,counter4=counter4,counter5=counter5))
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
label1 = Label(f, text="00:00:00", fg="lime", bg="black", font="Verdana 24 bold") 
label1.grid(column=0, row=0, sticky=N+S+E+W)
#label1.pack(side="left")
label2 = Label(f, text="00:00:00", fg="lime", bg="black", font="Verdana 24 bold") 
label2.grid(column=1, row=0, sticky=N+S+E+W)
#label2.pack(side="left")
label3 = Label(f, text="00:00:00", fg="lime", bg="black", font="Verdana 24 bold") 
label3.grid(column=2, row=0, sticky=N+S+E+W)
#label3.pack(side="left")
label4 = Label(f, text="00:00:00", fg="lime", bg="black", font="Verdana 24 bold") 
label4.grid(column=3, row=0, sticky=N+S+E+W)
#label4.pack(side="left")
label5 = Label(f, text="00:00:00", fg="lime", bg="black", font="Verdana 24 bold") 
label5.grid(column=4, row=0, sticky=N+S+E+W)
#label5.pack(side="left") 

label6 = Label(f, text="Total Time", fg="black", font="Courier 12 bold")
label6.grid(column=0, row=2, sticky=E+N+S+W)


start1 = Button(f, text='AFM', width=6, command=lambda:Start1(label1), font="Courier 24 bold") 
start1.grid(column=0, row=1, sticky=N+S+E+W)

stop = Button(f, text='Break',width=6, command=Stop, font="Courier 24 bold") 
stop.grid(column=2, row=2, sticky=E+N+S)
reset = Button(f, text='Sleep',width=6, command=Reset, font="Courier 24 bold") 
reset.grid(column=3, row=2, sticky=E+N+S)
start2 = Button(f, text='MAJ', width=6, command=lambda:Start2(label2, label1), font="Courier 24 bold") 
start2.grid(column=1, row=1, sticky=N+S+E+W)
start3 = Button(f, text='MOJ', width=6, command=lambda:Start3(label3, label1), font="Courier 24 bold") 
start3.grid(column=2, row=1, sticky=N+S+E+W)
start4 = Button(f, text='PTB', width=6, command=lambda:Start4(label4, label1), font="Courier 24 bold") 
start4.grid(column=3, row=1, sticky=N+S+E+W)
start5 = Button(f, text='SEP', width=6, command=lambda:Start5(label5, label1), font="Courier 24 bold") 
start5.grid(column=4, row=1, sticky=N+S+E+W)
exitbutton = Button(f, text='End', width=4, command=lambda:Exit(root), font="Courier 24 bold")
exitbutton.grid(column=4, row=2, sticky=E+N+S)

label6.after(1000,lambda:TotalTime(label6))


root.mainloop() 

