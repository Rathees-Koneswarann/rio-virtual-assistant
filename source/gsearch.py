
try:
	import pywhatkit as kit
	import webbrowser
except:
	pass
def search(word):
    kit.search(word)

def video(word):
	kit.playonyt(word)

def gaccount():
	webbrowser.open_new_tab('https://myaccount.google.com/?utm_source=chrome-profile-chooser&pli=1')

def youtube():
	webbrowser.open_new_tab("https://www.youtube.com/")

def google():
	webbrowser.open_new_tab("https://www.google.com/")

