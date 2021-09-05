import speech_recognition as sr
import pyttsx3
import os
import time
import datetime
import gsearch
import myapps
import keyboard
import offline
import requests
import pyautogui
from tkinter import *
def place(win):
 
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y-200))
    win.deiconify()


engine = pyttsx3.init()
engine.setProperty('rate', 200)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

global internet
internet=0
def say(a):
		engine.say(a)
		engine.runAndWait()

r=sr.Recognizer()
r.energy_threshold = 6000
def phrase():

        with sr.Microphone() as source:
                audio = r.listen(source)

        try:
                return r.recognize_google(audio)

        except sr.UnknownValueError:
        	phrase()


        return ""
def phrase1():
	try:
		return offline.offline_rec()
	except:
		pass
		
	return ""


def checkInternetRequests(url='http://www.google.com/', timeout=5):
    try:
        
        r = requests.head(url, timeout=timeout)
        global internet
        internet=0
        
        return phrase()
    except:
    	if internet<1:
	    	print("No internet conetivity right now..")
	    	say('No internet conetivity right now sir, I am using offline recognition.')
	    	internet=internet+1
    	return phrase1()
    return ""

#localtime = time.asctime(time.localtime(time.time()))
now = datetime.datetime.now()
hr=now.hour
os.system('cls')
if hr < 12:
    print("Good moring.... Have a nice day")
    say("good moring sir. Have a nice day")
elif hr >= 12 and hr < 15:
    print("Good afternoon...")
    say("good afternoon sir")
elif hr >= 15 and hr <= 19:
    print("Good Evening")
    say("good evening sir")
elif hr >=19 and hr<=24:
    print("hi sir")
    say("hi sir")

sltime=0

while True:
		if hr>=22 and sltime==0:
			print('You have to sleep')
			say('you have to sleep sir')
			say('I thing it is better to do your works tommorow')
			sltime=sltime+1
		com0=checkInternetRequests()
		print(com0)
		com=com0.lower()

		if com=='enter' or com =='in to' or com=='send' or com=='search' or com=='find':
			pyautogui.press('enter')

		if com!='':
			if com.split()[0]=='type':
				ty=com.split()
				for wordty0 in range(1,len(com.split())):
					pyautogui.press('space')
					for wordty1 in ty[wordty0]:
						pyautogui.press(wordty1)
 
		if com=='hi rio' or com=='hai rio' or com=='hi' or com=='hai' or ('hello' in com) or com=='rio':
			print('hello sir, how can I help you?')
			say('hello sir, how can I help you?')

		elif ('can you hear me' in com) or ('are you hearing me' in com):
			print('yes sir')
			say('yes sir')
 
		elif ('bye' in com) or ('bhai' in com):
			print("bye sir, have a good time")
			say('ok bye sir, have a good time')
			exit()

		elif (("close" in com) or ("exit" in com)) and ('assistant' in com):
			print("bye sir, have a good time")
			say('ok bye sir, have a good time')
			exit()

		elif com=='thanks' or com=='thank you' or com=='thank you so much' or com=='ok thanks'  or com=='ok thank you':
			print("it's my pleasure..")
			say("it's my pleasure..")

		elif 'good night' in com:
			print('good night sir.. sweet dreams')
			say('good night sir.. sweet dreams')
			exit()

		elif 'what' in com and 'time' in com:
			print(now.hour+""+now.minute)

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ("calculator" in com) :
			say('starting calculater sir')
			myapps.calculator()
			

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ("notepad" in com) :
			say('starting notepad sir')
			myapps.notepad()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ("word" in com) :
			say('starting microsoft word sir')
			myapps.msword()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ("excel" in com) :
			say('starting microsoft excel sir')
			myapps.msexcel()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ("access" in com) :
			say('starting microsoft access sir')
			myapps.msaccess()
			say('done sir')
						
		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and (("power point" in com) or ("powerpoint" in com)) :
			say('starting microsoft power point sir')
			myapps.msppt()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ("paint" in com) :
			say('starting paint tool sir')
			myapps.mspaint()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and (("cmd" in com) or ("command line" in com) or ("terminal" in com)) :
			say('starting command prompt sir')
			myapps.cmd()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ("bluetooth" in com) :
			say('starting bluetooth sir')
			myapps.bluetooth()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and (("taskmanager" in com) or ("task manager" in com)) :
			myapps.taskmanager()
			say('done sir')

		elif (('logoff' in com ) or ('log off' in com) or ('signoff' in  com) or ('sign off' in  com) or ('sign out' in  com) or ('log out' in  com)) and ('rio' in  com):
			myapps.logoff()
			print('preparing to logoff')
			say('logging off the computer sir.')
			exit()

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('magnifier' in com) :
			say('starting magnifier sir')
			myapps.magnify()
			say('done sir')	

		elif  (("zoom" in com) or ("magnify" in com)) and (('screen' in com) or ('dekstop' in com)) :
			say('starting magnifier sir')
			myapps.magnify()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('narrator' in com) :
			say('starting narrator sir')
			myapps.narrator()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('screen keyboard' in com) :
			say('starting screen keyboard sir')
			myapps.keyboard()
			say('done sir')	

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('step recorder' in com) :
			say('starting step recorder sir')
			myapps.step_recorder()
			say('done sir')	

		elif (('pc' in com) or ("computer" in com) or ('system' in com) or ('laptop' in com)) and (("status" in com) or ("performance" in com) or ('info' in com)):
			say('searching system info sir')
			myapps.performance1()
			myapps.systeminfo()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('volume mixer' in com) :
			myapps.vol_mix()
			say('done sir')	

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('snipping tool' in com) :
			say('starting snipping tool sir')
			myapps.snipping_tool()
			say('done sir')

		elif (('system' in com) or ("computer" in com) or ('pc' in com)) and (('properties' in com) or ('property' in com) or ('info' in com)):
			say('searching systeminfo sir')
			myapps.system_properties()
			myapps.systeminfo()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('explorer' in com) :
			say('starting file explorer sir')
			myapps.explorer()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and (("adobe reader" in com) or ("pdf" in com)) :
			say('starting adope pdf reader sir')
			myapps.adope_reader()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and (("wave editor" in com) or ("audio editor" in com) or ("song editor" in com)) :
			myapps.wave_editor()
			say('done sir')	

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and (("notepad 2 plus" in com) or ("notepad plus plus" in com)) :
			myapps.notepad_1()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and (('windows media player' in com) or ('window media player' in com)):
			myapps.windows_media_player()
			say('done sir')	

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('photoshop' in com) :
			myapps.photoshop()
			say('done sir')	

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('touchpad' in com) :
			myapps.touch_pad()
			say('done sir')	

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and (('sublime text' in com) or ('text editor' in com)) :
			myapps.sublime_text()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('control panel' in com) :
			myapps.control_panel()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('chrome' in com) :
			myapps.chrome()
			say('done sir')

		elif (('program' in com) or ('sofwtware' in com) or ('application' in com) or ("go to" in com))	and ('uninstall' in com):
			myapps.uninstall()
			say('done sir')	

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('display setting' in com) :
			myapps.display_settings()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('sound setting' in com) :
			myapps.sound_settings()
			say('done sir')

		elif (('version' in com) or ('about' in com)) and ("windows" in com):
			myapps.about_windows()
			say('done sir')

		elif ('rio' in com) and (('shutdown' in com) or ('shut down' in com)):
			myapps.shutdown()
			print('preparing to shutdown')
			say('wait sir, shutting down')
			exit()															

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('desktop' in com) :
			myapps.desktop()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('document' in com) :
			myapps.documents()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('download' in com) :
			myapps.downloads()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and (('picture' in com) or ('image' in com)) :
			myapps.pictures()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and (('music' in com) or ('song' in com)) :
			myapps.music()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('video' in com) :
			myapps.videos()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('disk c' in com):
			myapps.disk_c()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('disk e' in com):
			myapps.disk_e()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com) or ("search" in com)) and ('google account' in com):
			try:
				gsearch.gaccount()
				say('done sir')
			except:
				print('here is a  problem right now')
				say('here is a  problem right now sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com) or ("search" in com)) and ('google' in com):
			try:
				say('opening google search sir')
				gsearch.google()
				say('done sir')
			except:
				print('here is a  problem right now ')
				say('here is a  problem right now sir')


		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com) or ("search" in com)) and (('youtube' in com) or ('you tube' in com)):
			try:
				say('opening youtube sir')
				gsearch.youtube()
				say('done sir')
			except:
				print('here is a  problem right now')
				say('here is a  problem right now sir')				

		elif (('play' in com) or ('listen' in com)  or ('watch' in com) ) and (('music' in com) or ('song' in com) or ('bgm' in com) or ('video' in com) or ('movie' in com) or ('film' in com)):
			y=com.split()
			x=''
			for i in range(len(y)):
				if (y[i]=='play') or (y[i]=='listen') or (y[i]=='watch'):
						for j in range(i+1,len(y)):
							if (y[j]=='song') or (y[j]=='music') or (y[j]=='bgm') or (y[j]=='video') or (y[j]=='movie') or (y[j]=='film'):
								for k in range(i+1,j+1):
									x=x+ y[k]+" "
								try:							
									gsearch.video(x)
									print('playing... '+x)
									say('playing'+x)
								except:
									print('here is a problem right now sir')
									say('here is a problem right now sir')									

		elif ('what is' in com) or ('what are' in com)  or ('wich is' in com) or ('wich are' in com) or ('who is' in com) or ('who are' in com) or ('search about' in com) or ('how to' in com) or ('where is' in com) or ('when is' in com):
			y=com.split()
			x=''
			for i in range(len(y)):
				if (y[i]=='is') or (y[i]=='are') or (y[i]=='about') or (y[i]=='to'):
					for j in range(i+1,len(y)):
						x=x+ y[j]+" "
					print(x)
					try:
						say('searching results for'+x)		
						gsearch.search(x)
					except:
						print('here is a  problem right now sir')
						say('here is a  problem right now sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('telegram' in com):
			myapps.telegram()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and (('whatsapp' in com) or ('whats app' in com)):
			myapps.whatsapp()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and (('arduino' in com) or ('ardino' in com)):
			myapps.arduino()
			say('done sir')
		
		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com) or ("send" in com)) and (('email' in com) or ('gmail' in com) or ('mail' in com)):
			myapps.mail()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com) or ("see" in com) or ("watch" in com) or ("check" in com) or ('need' in com) or ('want' in com)) and  ('calendar' in com):
			myapps.calendar()
			say('done sir')
						
		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com) or ('need' in com) or ('want' in com)) and (('alarm' in com) or ('clock' in com) or ('timer' in com) or ('stop watch' in com)):
			myapps.alarm_and_clock()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com) or ("play" in com) or ("listen" in com)) and (('music' in com) or ('song' in com)):
			myapps.music_player()
			say('done sir')
		
		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com) or ("find" in com) or ("search" in com)) and (('map' in com) or ('location' in com)):
			myapps.telegram()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('game' in com):
			myapps.game()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('sticky note' in com):
			myapps.sticky_note()
			say('done sir')

		elif  'note this' in com or 'note that' in com :
			myapps.sticky_note()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com) or ('record')) and (('voice recorder' in com) or ('mic' in com)):
			myapps.voice_recorder()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('zoom' in com):
			myapps.zoom()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and (('power director' in com) or ('video editor' in com)):
			myapps.power_director()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('settings' in com):
			myapps.settings()
			say('done sir')

		elif  (("open" in com) or ("run" in com) or ("start" in com) or ("go to" in com)) and ('math' in com):
			myapps.math_input_panel()
			say('done sir')

		elif (('on' in com) or ('off' in com) or ('go to' in com)  or ('turn' in com)  or ('enable' in com) or ('disable' in com)) and ('flight' in com):
			say('done sir')
			myapps.flight_mode()

		elif (('stop' in com) or ('pause' in com)) and (('music' in com) or ('song' in com) or ('bgm' in com) or ('video' in com) or ('movie' in com) or ('film' in com)):
			pyautogui.press('space')

		elif ('type' in com) and (('word' in com) or ('sentence' in com) or ('letter' in com) or ('miss it' in com) or ('speed' in com)   ):
			say('ok I am ready sir.')
			while True:
				typelet=checkInternetRequests()
				print(typelet)
				if 'stop' in typelet and 'typ' in typelet:
					print('typing exited')
					say('ok done sir')
					break
				if typelet=="":
					continue
				if typelet=='enter' or typelet=='Enter' or typelet=='press enter' or typelet=='hit enter':
					pyautogui.press('enter')
					continue
				if typelet=='full stop':
					pyautogui.press('.')
					continue
				if typelet=='question mark':
					pyautogui.press('?')
					continue
				for let in typelet:
					pyautogui.press(let)
				pyautogui.press('space')
		elif (('volume' in com) or ('sound' in com)) and (('increase' in com) or ('up' in com)):
			pass

