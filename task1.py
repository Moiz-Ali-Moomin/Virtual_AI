import os
import pyttsx3 as pys
import speech_recognition as sr

print('''
Commands Available:
1. Open Notepad
2. Open Windows Media player
3. Open MS Excel
4. Open Chrome Browser
5. Open Vscode
6. Open Firefox
7. Open Microsoft word
	''')

# you can add more options 

while True:

	r = sr.Recognizer()

	with sr.Microphone() as source:
		print("Speak anything : ")
		audio = r.listen(source)

		try:
			text = r.recognize_google()
			print("You said  {}".format(text))

			print("Which application would you like to open:", end=' ')
			p=text
			if("run " in p) or ("open "in p):
				if("not " in p) or ("do not " in p) or ("dont " in p):
					exit()
				else:
					if ("notepad "in p) or ("text edittor"in p):
						pys.speak("opening notepad") 
						os.system("notepad")

					elif("wmplayer"in p) or ("Windows Media player" in p):
						pys.speak("opening Windows Media Player") 
						os.system("wmplayer")

					elif("Excel"in p) or ("excel"in p):
						pys.speak("opening Microsoft Excel") 
						os.system("EXCEL")	

					elif("chrome"in p) or ("browser" in p):
						pys.speak("opening Google Chrome: Your internet browser") 
						os.system("chrome")

					elif("code"in p) or ("vscode"in p) or ("visual studio code"in p):
						pys.speak("opening Code Blocks: Your C compiler") 
						os.system("code")
	

					elif("Word"in p) or ("word"in p):
						pys.speak("opening Microsoft Word") 
						os.system("WINWORD")	

					elif("Mozilla Firefox"in p) or ("mozilla firefox"in p) or ("firefox"in p):
						pys.speak("opening Mozilla Firefox: Your internet browser") 
						os.system("Mozilla Firefox")															

					else:
						print("Command not available")
						pys.speak("Please Try Something else")

			elif("close"in p) or ("stop"in p) or ("exit"in p):
						pys.speak("Bye Have a Great Day")
						exit()

			elif("hi "in p) or ("hello"in p) or ("hey"in p):
						pys.speak("Hello Everyone AI at your service How can I help you")

			else:
				pys.speak("Unable to run your command please try again")
		except:

			pys.speak("Sorry Unable to recognize your voice")





























# 