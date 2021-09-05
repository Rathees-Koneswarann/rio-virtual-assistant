import os
import keyboard
import pyautogui
import time
def appclick(x):
	pyautogui.click(80, 885)
	time.sleep(2)
	for i in x:
		pyautogui.press(i)
	pyautogui.press('enter')


def calculator():
    os.startfile("C:/Windows/System32/calc.exe")

def notepad():
    os.startfile("C:/Windows/System32/notepad.exe")

def msword():
    os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office 2013/Word 2013")

def msexcel():
    os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office 2013/Excel 2013")

def msppt():
    os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office 2013/PowerPoint 2013")

def msaccess():
    os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office 2013/Access 2013")

def mspaint():
    os.startfile("C:/Windows/System32/mspaint.exe")

def cmd():
	appclick('cmd')

def bluetooth():
	os.startfile("C:/Windows/System32/fsquirt.exe")

def taskmanager():
	os.startfile("C:/Windows/System32/LaunchTM.exe")

def logoff():
	os.startfile("C:/Windows/System32/logoff.exe")

def magnify():
	os.startfile("C:/Windows/System32/Magnify.exe")

def narrator():
	os.startfile("C:/Windows/System32/Narrator.exe")

def keyboard():
	os.startfile("C:/Windows/System32/osk.exe")

def performance():
	os.startfile("C:/Windows/System32/perfmon.exe")

def step_recorder():
	os.startfile("C:/Windows/System32/psr.exe")

def performance1():
	os.startfile("C:/Windows/System32/resmon.exe")

def vol_mix():
	os.startfile("C:/Windows/System32/SndVol.exe")

def snipping_tool():
	os.startfile("C:/Windows/System32/SnippingTool.exe")

def system_properties():
	os.startfile("C:/Windows/System32/SystemPropertiesComputerName.exe")

def explorer():
	os.startfile("C:/Windows/explorer.exe")

def adope_reader():
	os.startfile("C:/Program Files (x86)/Adobe/Reader 11.0/Reader/AcroRd32.exe")

def wave_editor():
	os.startfile("C:/Program Files (x86)/Cyberlink/WaveEditor/WaveEditor.exe")

def notepad_1():
	os.startfile("C:/Program Files (x86)/Notepad++/notepad++.exe")
	
def windows_media_player():
	os.startfile("C:/Program Files (x86)/Windows Media Player/wmplayer.exe")

def photoshop():
	os.startfile("C:/Program Files/Adobe/Adobe Photoshop 2020/Photoshop.exe")

def touch_pad():
	os.startfile("C:/Program Files/DellTPad/DellTouchpad.exe")

def sublime_text():
	os.startfile("C:/Program Files/Sublime Text 3/sublime_text.exe")

def chrome():
	os.system('start chrome')

def control_panel():
	os.system('control')

def uninstall():
	os.system("APPWIZ.CPL ")

def display_settings():
	os.system('DESK.CPL')

def sound_settings():
	os.system("MMSYS.CPL")

def about_windows():
	os.system("winver")

def shutdown():
	os.system('shutdown /s')

def desktop():
	os.startfile('C:/Users/user/Desktop')

def documents():
	os.startfile('C:/Users/user/Documents')

def downloads():
	os.startfile('C:/Users/user/Downloads')

def music():
	os.startfile('C:/Users/user/Music')

def pictures():
	os.startfile('C:/Users/user/Pictures')

def videos():
	os.startfile('C:/Users/user/Videos')

def disk_c():
	os.system('start c:')

def disk_e():
	os.system('start e:')

def systeminfo():
	os.system('  systeminfo')

def telegram():
	appclick('  telegram')

def whatsapp():
	appclick('  whatsapp')

def arduino():
	appclick('  arduino')

def mail():
	appclick('  mail')

def webots():
	appclick('  webots')

def calendar():
	appclick('  calendar')

def alarm_and_clock():
	appclick('  alarm')

def music_player():
	appclick('  groove music')

def map():
	appclick('  map')

def game():
	appclick('  solitaire')	

def sticky_note():
	appclick('  sticky note')

def voice_recorder():
	appclick('  voice recorder')

def zoom():
	appclick("  zoom")

def power_director():
	appclick('  power director')

def settings():
	appclick('  settings')
	
def math_input_panel():
	appclick('  math input panel')

def flight_mode():
	pyautogui.click(1414, 875)
	time.sleep(2)
	pyautogui.click(1395,819)
	pyautogui.click(1414, 875)

