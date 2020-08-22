import os
import pyttsx3 as pys
import speech_recognition as sr
import webbrowser
from selenium import webdriver
import smtplib
import wikipedia
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

print('''
Commands Available:
1. Open Notepad
2. Open Windows Media player
3. Open MS Excel
4. Open Chrome Browser
5. Open Vscode
6. Open Firefox
7. Open Microsoft word
8. Play Music
9. Send Email
10. Open website like (Wikipedia, linkedin)
	''')

# you can add more options

while True:

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(" AI at your Service what can i do for You :", end=" ")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="en-in")
            print("You said  {}".format(text))

            p = text.lower()
            if("run " in p) or ("open " in p):
                if("not " in p) or ("do not " in p) or ("dont " in p):
                    exit()
                else:
                    if ("notepad " in p) or ("text edittor" in p):
                        pys.speak("opening notepad")
                        os.system("notepad")

                    elif("wmplayer" in p) or ("Windows Media player" in p):
                        pys.speak("opening Windows Media Player")
                        os.system("wmplayer")

                    elif("Excel" in p) or ("excel" in p):
                        pys.speak("opening Microsoft Excel")
                        os.system("EXCEL")

                    elif("chrome" in p) or ("browser" in p):
                        pys.speak(
                            "opening Google Chrome: Your internet browser")
                        os.system("chrome")

                    elif("code" in p) or ("vscode" in p) or ("visual studio code" in p):
                        pys.speak("opening Code Blocks: Your C compiler")
                        os.system("code")

                    elif("Word" in p) or ("word" in p):
                        pys.speak("opening Microsoft Word")
                        os.system("WINWORD")

                    elif("Mozilla Firefox" in p) or ("mozilla firefox" in p) or ("firefox" in p):
                        pys.speak(
                            "opening Mozilla Firefox: Your internet browser")
                        os.system("Mozilla Firefox")

                    elif("music" in p) or ("Play Music" in p) or ("play music" in p):
                        pys.speak("Playing Music")
                        music_dir = os.path.join(
                            os.environ['USERPROFILE'], "Music")
                        songs = os.listdir(music_dir)
                        print(songs)
                        os.startfile(os.path.join(music_dir, songs[0]))

                    elif("send email" in p) or ("Send Email" in p) or ("Email" in p):
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.ehlo()
                        server.starttls()
                        server.login('youremail@gmail.com', 'your-password')
                        server.sendmail('youremail@gmail.com', to, content)
                        server.close()

                    # elif("youtube" in p):
					# 	assistant_speaks("Opening in youtube")
					# 	indx = p.lower().split().index('youtube')
					# 	p = p.split()[indx + 1:]
					# 	driver.get(
					# 		"http://www.youtube.com/results?search_query =" + '+'.join(p))

                    # elif ("wikipedia" in p):
					# 	assistant_speaks("Opening Wikipedia")
					# 	indx = p.lower().split().index('wikipedia')
					# 	query = p.split()[indx + 1:]
					# 	driver.get(
					# 		"https://en.wikipedia.org/wiki/" + '_'.join(p))

                    elif ("wikipedia") in p:
                        pys.speak('Searching Wikipedia...')
                        query = p.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=2)
                        pys.speak("According to Wikipedia")
                        print(results)
                        pys.speak(results)

                    elif ("youtube search" in p):
                        pys.speak("Opening youtube")
                        indx = p.lower().split().index('youtube search')
                        query = p.split()[indx + 1:]
                        webbrowser.open(
                            "http://www.youtube.com/results?search_query =" + "+".join(query))

                    elif ("google search" in p):
                        pys.speak("Opening google")
                        indx = p.lower().split().index('google search')
                        query = p.split()[indx + 1:]
                        webbrowser.open(
                            "google.com/?q=" + "+".join(query))

                    elif ("open stackoverflow" in query):
                        webbrowser.open("stackoverflow.com")



            elif("close" in p) or ("stop" in p) or ("exit"in p):
                pys.speak("Bye Have a Great Day")
                exit()

            elif("hi " in p) or ("hello" in p) or ("hey"in p):
                pys.speak("Hello Everyone AI at your service How can I help you")

            else:
                pys.speak("Unable to run your command please try again")
        except:

            pys.speak("Sorry Unable to recognize your voice")


#
