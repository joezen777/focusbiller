# focusbiller

Update revert_idle_threshold and warning_threshold for your preferences, units is minutes.

This is a handy program you can run that helps you self-track how much time you're actually spending on a billable activity.

Your left-most timer is your default timer. AFM or Away From Monitor or Another Flipping Meeting or Amazon.com Fixates Me. This timer has no penalty or pay-off, it's the default. The other timers will expire after 15 minutes unless you hit their button again. This way you get a neat little reminder every so many minutes to stay on task. And at the end of the day, you can tell yourself, yes I actually did work enough time, I should give myself permission to take a break and not feel guilty. 

Currently the time intervals for the other timers are set to give you a warning at ten minutes.  It slowly progresses. 
1. 10 minutes = blip every other second
2. 14 minutes = klaxon every other second
3. 14 minutes 50 seconds = klaxon every second
4. 15 minutes = system failure -> stop current timer and revert to AFM/Idle timer

[Here's a commit of me changing the time intervals and labels](https://github.com/joezen777/focusbiller/commit/100c770a6f26de2e73617089061288b1801aa257)

Again set your own labels. The goal is to minimize your reactive time and maximize your proactive time. Also, make sure you're spending the most time and what's important.

* AFM - Awesomely Focused Mindnumbing - Away Facebooking Mom (Reactive, low priority)
* MAJ - My Actual Job - Proactive, High Priority
* MOJ - My Other Job - Proactive, Low Priority
* PTB - PT Barnum - Political Talking Business - Please Try Buying - Proactive/Reactive, Mixed Priority
* SEP - Somebody Else's Problem - Reactive, High Priority
* Break - Stops all timers, even your default timer. Click on a timer to resume.
* Sleep - Reset, there's no prompt, go back to zero
* End - It ends things

Feel free to adjust as you like and hope this helps. 

Failing to type in the correct sequence of numbers does not cause a magnetic anomaly. 

# install

Make sure you have Python3 installed. Also you'll need to run this pip command
```shell
sudo pip install simpleaudio
```

I tested this on a Mac and on a Raspberry Pi with a 7" touchscreen.  Could not get the simpleaudio pip to install on my Android phone. 

When you're ready to start
```shell
python3 main.py
```

# logs

The program does a console out every 5 minutes with your time so if there's an unexplainable crash, hopefully you don't lose your time.

# demo

[![Demonstrating how to stay on task using the app](http://img.youtube.com/vi/jxrBUJRwbJ8/0.jpg)](http://www.youtube.com/watch?v=jxrBUJRwbJ8)