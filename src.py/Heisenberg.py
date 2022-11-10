import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon
import datetime
import getpass
import os
import random
import sqlite3
import string
import subprocess
import threading
import tkinter as tk
import webbrowser
import winsound
from functools import partial
from tkinter import END, RIGHT, LEFT
from tkinter.ttk import Entry

import PIL
import psutil
import pyautogui
import pyjokes
import pywhatkit
import requests
import wikipedia
import wolframalpha
from PIL import ImageTk, Image
from ttkthemes import themed_tk
import pystray
import Annex
import MyAlarm

try:
    app = wolframalpha.Client("JPK4EE-L7KR3XWP9A")  # API key for wolframalpha
except Exception as e:
    pass

# setting chrome path
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"


def there_exists(terms, query):
    for term in terms:
        if term in query:
            return True


def CommandsList():
    os.startfile('Commands List.txt')


def clearScreen():
    SR.scrollable_text_clearing()


def greet():
    conn = sqlite3.connect('Heisenberg.db')
    mycursor = conn.cursor()
    hour = int(datetime.datetime.now().hour)
    if 4 <= hour < 12:
        mycursor.execute('select sentences from goodmorning')
        result = mycursor.fetchall()
        SR.speak(random.choice(result)[0])
    elif 12 <= hour < 18:
        mycursor.execute('select sentences from goodafternoon')
        result = mycursor.fetchall()
        SR.speak(random.choice(result)[0])
    elif 18 <= hour < 21:
        mycursor.execute('select sentences from goodevening')
        result = mycursor.fetchall()
        SR.speak(random.choice(result)[0])
    else:
        mycursor.execute('select sentences from night')
        result = mycursor.fetchall()
        SR.speak(random.choice(result)[0])
    conn.commit()
    conn.close()
    SR.speak("\nI'm Alex ,How can i help you sir!")


def mainframe():
    SR.scrollable_text_clearing()
    greet()

    TIME_NOW = datetime.datetime.now()
    TIME_REST = datetime.timedelta(minutes=4)  # i put it only 4 minutes for recording purpose
    new = TIME_NOW + TIME_REST
    new1 = new.strftime("%H:%M:%S %p")
    print(new1)

    try:
        while True:
            Ta = datetime.timedelta(hours=12)
            t = datetime.datetime.now()
            t1 = t.strftime("%H:%M:%S %p")
            print(Ta)

            print(t1)
            if (t1 >= new1):
                SR.speak("Warning,sir! you are using pc more then 4 minutes !")
                pass

            delta = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
            uptimeWeeks = divmod(delta.days, 7)[0]
            uptimeHours, remainder = divmod(delta.seconds, 3600)
            uptimeMins = divmod(remainder, 60)[0]
            uptime = f'the computer wake up for {uptimeWeeks:2}week ,{delta.days:2}day, {uptimeHours:2}hour and {uptimeMins:2}minute'

            query = SR.takeCommand().lower()
            if there_exists(['search wikipedia for', 'wikipedia', 'from wikipedia', 'what is meant by',
                             'who the heck is'], query):

                SR.speak(query)
                results = wikipedia.summary(query, sentences=2)
                SR.speak("According to wikipedia:\n")
                SR.speak(results)
                pass


            elif there_exists(['tell me joke', 'tell me a joke', 'tell me some jokes', 'i would like to hear some jokes'
                                  , "i'd like to hear some jokes", 'can you please tell me some jokes',
                               'i want to hear a joke'
                                  , 'i want to hear some jokes', 'please tell me some jokes',
                               'would like to hear some jokes', 'tell me more jokes'], query):
                answer_chioce = ["ok boss,i will tell some jokes listen to this one:",
                                 "This is a funny joke. Listen:",
                                 "oh, my brother,i have to tell jokes? ok, Hear this joke. It is really funny:"]
                greeting = random.choice(answer_chioce)
                SR.speak(greeting)
                if 'tell me joke' in query:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = query

                    pass

                elif 'tell me a joke' in query:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = query
                    pass

                elif 'tell me some jokes' in query:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = query
                    pass
                elif 'i would like to hear some jokes' in query:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = query
                    pass

                elif 'id like to hear some jokes' in query:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = query
                    pass

                elif 'can you please tell me some jokes' in query:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = query
                    pass

                elif 'i want to hear a joke' in query:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = query
                    pass

                elif 'i want to hear some jokes' in query:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = query
                    pass
                elif 'would like to hear some jokes' in query:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = query
                    pass
                elif 'tell me more jokes' in query:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = query
                    pass



            elif there_exists(["what is your name",
                               "tell me your name", 'who are you', "your name", "who the hell are you",
                               "name please"], query):
                if 'what is your name' in query:
                    answer_chioce = ["My name is Alex and I'm here to serve you.",
                                     "My name is Alex!  Did you forget me sir?",
                                     "I'm sad because you don't remember me.  I'm Alex your personal assistant!"]
                    greeting = random.choice(answer_chioce)
                    SR.speak(greeting)
                    query_for_name = query
                    pass
                elif 'tell me your name' in query:
                    answer_chioce = ["My name is Alex and I'm here to serve you.",
                                     "My name is Alex!  Did you forget me sir?",
                                     "I'm sad because you don't remember me.  I'm Alex your personal assistant!"]
                    greeting = random.choice(answer_chioce)
                    SR.speak(greeting)
                    query_for_name = query
                    pass
                elif 'who are you' in query:
                    answer_chioce = ["My name is Alex and I'm here to serve you.",
                                     "My name is Alex!  Did you forget me sir?",
                                     "I'm sad because you don't remember me.  I'm Alex your personal assistant!"]
                    greeting = random.choice(answer_chioce)
                    SR.speak(greeting)
                    query_for_name = query
                    pass

                elif 'your name' in query:
                    answer_chioce = ["My name is Alex and I'm here to serve you.",
                                     "My name is Alex!  Did you forget me sir?",
                                     "I'm sad because you don't remember me.  I'm Alex your personal assistant!"]
                    greeting = random.choice(answer_chioce)
                    SR.speak(greeting)
                    query_for_name = query
                    pass

                elif 'who the hell are you' in query:
                    answer_chioce = ["My name is Alex and I'm here to serve you.",
                                     "My name is Alex!  Did you forget me sir?",
                                     "I'm sad because you don't remember me.  I'm Alex your personal assistant!"]
                    greeting = random.choice(answer_chioce)
                    SR.speak(greeting)
                    query_for_name = query
                    pass

                elif 'who the hell are you' in query:
                    answer_chioce = ["My name is Alex and I'm here to serve you.",
                                     "My name is Alex!  Did you forget me sir?",
                                     "I'm sad because you don't remember me.  I'm Alex your personal assistant!"]
                    greeting = random.choice(answer_chioce)
                    SR.speak(greeting)
                    query_for_name = query
                    pass





                elif 'name please' in query:
                    answer_chioce = ["My name is Alex and I'm here to serve you.",
                                     "My name is Alex!  Did you forget me sir?",
                                     "I'm sad because you don't remember me.  I'm Alex your personal assistant!"]
                    greeting = random.choice(answer_chioce)
                    SR.speak(greeting)
                    query_for_name = query
                    pass





            elif there_exists(['how are you', 'how are you doing', 'are you ok', 'how do you feel'], query):
                conn = sqlite3.connect('Heisenberg.db')
                mycursor = conn.cursor()
                mycursor.execute('select sentences from howareyou')
                result = mycursor.fetchall()
                temporary_data = random.choice(result)[0]
                SR.updating_ST_No_newline(temporary_data + '😃\n')
                SR.nonPrintSpeak(temporary_data)
                conn.close()
                pass



            elif there_exists(['what is my name', 'tell me my name', "i don't remember my name", " I want my name",
                               "do you know my name", "my name is"], query):
                SR.speak("Your name is " + str(getpass.getuser()))
                query_for_username = query
                pass



            elif there_exists(['open youtube', 'show youtube',
                               'access youtube'], query):
                if 'open youtube' in query:
                    SR.speak("Opening youtube")
                    webbrowser.open("https://www.youtube.com")
                    pass

                elif 'show youtube' in query:
                    SR.speak("Opening youtube")
                    webbrowser.open("https://www.youtube.com")
                    pass

                elif 'access youtube' in query:
                    SR.speak("Opening youtube")
                    webbrowser.open("https://www.youtube.com")
                    pass

            elif there_exists(['play on youtube', 'music in youtube', 'youtube music', 'play song', 'music youtube'],
                              query):
                if 'play on youtube' in query:
                    song = query.replace('play on youtube', '')
                    SR.speak('playing' + song)
                    pywhatkit.playonyt(song)
                    pass
                elif 'music in youtube' in query:
                    song = query.replace('music in youtube', '')
                    SR.speak('playing' + song)
                    pywhatkit.playonyt(song)
                    pass

                elif 'youtube music' in query:
                    song = query.replace('youtube music', '')
                    SR.speak('playing' + song)
                    pywhatkit.playonyt(song)
                    pass

                elif 'play song' in query:
                    song = query.replace('play song', '')
                    SR.speak('playing' + song)
                    pywhatkit.playonyt(song)
                    pass

                elif 'music youtube' in query:
                    song = query.replace('music youtube', '')
                    SR.speak('playing' + song)
                    pywhatkit.playonyt(song)
                    pass

            elif there_exists(['open google', 'show google',
                               'access google'], query):
                if 'open google' in query:
                    SR.speak("Opening Google")
                    webbrowser.open("https://www.google.com")
                    pass

                elif 'show google' in query:
                    SR.speak("Opening Google")
                    webbrowser.open("https://www.google.com")
                    pass

                elif 'access google' in query:
                    SR.speak("Opening Google")
                    webbrowser.open("https://www.google.com")
                    pass

            elif there_exists(['open facebook', 'show facebook',
                               'access facebook'], query):
                if 'open facebook' in query:
                    SR.speak("Opening Facebook")
                    webbrowser.open("https://www.facebook.com")
                    pass

                elif 'show facebook' in query:
                    SR.speak("Opening Facebook")
                    webbrowser.open("https://www.facebook.com")
                    pass

                elif 'access facebook' in query:
                    SR.speak("Opening Facebook")
                    webbrowser.open("https://www.facebook.com")
                    pass

            elif there_exists(['google and search'
                                  , 'search on google', 'find in google'], query):
                if 'google and search' in query:
                    google = query.replace("google and search", "")
                    webbrowser.open("https://www.google.com/search?q={}".format(google))
                    pass

                elif 'search on google' in query:
                    google = query.replace("search on google", "")
                    webbrowser.open("https://www.google.com/search?q={}".format(google))
                    pass

                elif 'find in google' in query:
                    google = query.replace("find in google", "")
                    webbrowser.open("https://www.google.com/search?q={}".format(google))
                    pass
            elif there_exists(['open microsoft edge', 'show microsoft edge',
                               'access microsoft edge', 'microsoft edge'], query):
                if 'open microsoft edge' in query:
                    opening = query.replace('open microsoft edge', 'microsoft edge')
                    SR.speak("Opening Microsoft Edge")
                    pyautogui.hotkey('win', 'd')
                    pyautogui.press('win')
                    pyautogui.write(opening)
                    pyautogui.press("enter")
                    pass

                elif 'show microsoft edge' in query:
                    opening = query.replace('show microsoft edge', 'microsoft edge')
                    SR.speak("Opening Microsoft Edge")
                    pyautogui.hotkey('win', 'd')
                    pyautogui.press('win')
                    pyautogui.write(opening)
                    pyautogui.press("enter")
                    pass

                elif 'access microsoft edge' in query:
                    opening = query.replace('access microsoft edge', 'microsoft edge')
                    SR.speak("Opening Microsoft Edge")
                    pyautogui.hotkey('win', 'd')
                    pyautogui.press('win')
                    pyautogui.write(opening)
                    pyautogui.press("enter")
                    pass


                elif 'microsoft edge' in query:
                    opening = query.replace('microsoft edge', 'microsoft edge')
                    SR.speak("Opening Microsoft Edge")
                    pyautogui.hotkey('win', 'd')
                    pyautogui.press('win')
                    pyautogui.write(opening)
                    pyautogui.press("enter")
                    pass


            elif there_exists(['open gmail', 'show gmail',
                               'access gmail', 'gmail'], query):
                if 'open gmail' in query:
                    webbrowser.open('https://mail.google.com/mail/')
                    SR.speak("Opening gmail")
                    pass


                elif 'show gmail' in query:
                    webbrowser.open('https://mail.google.com/mail/')
                    SR.speak("Opening gmail")
                    pass

                elif 'access gmail' in query:
                    webbrowser.open('https://mail.google.com/mail/')
                    SR.speak("Opening gmail")
                    pass

                elif 'gmail' in query:
                    webbrowser.open('https://mail.google.com/mail/')
                    SR.speak("Opening gmail")
                    pass

            elif there_exists(['open maps', 'show maps',
                               'access maps', 'maps'], query):
                if 'open maps' in query:
                    webbrowser.open('https://www.google.co.in/maps/')
                    SR.speak("Opening Google Maps")
                    pass


                elif 'show maps' in query:
                    webbrowser.open('https://www.google.co.in/maps/')
                    SR.speak("Opening Google Maps")
                    pass

                elif 'access maps' in query:
                    webbrowser.open('https://www.google.co.in/maps/')
                    SR.speak("Opening Google Maps")
                    pass

                elif 'maps' in query:
                    webbrowser.open('https://www.google.co.in/maps/')
                    SR.speak("Opening Google Maps")
                    pass

            elif there_exists(['open calculator', 'show calculator',
                               'access calculator'], query):
                if 'open calculator' in query:
                    SR.speak('Opening calculator')
                    os.startfile('C:\\Windows\\System32\\calc.exe')
                    pass
                elif 'show calculator' in query:
                    SR.speak('Opening calculator')
                    os.startfile('C:\\Windows\\System32\\calc.exe')
                    pass
                elif 'access calculator' in query:
                    SR.speak('Opening calculator')
                    os.startfile('C:\\Windows\\System32\\calc.exe')
                    pass


            elif there_exists(['open notepad', 'show notepad',
                               'access notepad'], query):
                if 'open notepad' in query:
                    SR.speak('Opening notepad')
                    os.startfile('c:\\Windows\\System32\\notepad.exe')
                    pass
                elif 'show notepad' in query:
                    SR.speak('Opening notepad')
                    os.startfile('c:\\Windows\\System32\\notepad.exe')
                    pass
                elif 'access notepad' in query:
                    SR.speak('Opening notepad')
                    os.startfile('c:\\Windows\\System32\\notepad.exe')
                    pass


            elif there_exists(['close notepad', 'deny notepad'
                               ], query):
                if 'close notepad' in query:
                    SR.speak(" Closing notepad")
                    os.system("taskkill /f /im notepad.exe")
                    pass
                elif 'deny notepad' in query:
                    SR.speak(" Closing notepad")
                    os.system("taskkill /f /im notepad.exe")
                    pass

            elif there_exists(['close calculator', 'deny calculator'
                               ], query):
                if 'close calculator' in query:
                    SR.speak(" Closing calculator")
                    os.system("taskkill /f /im calc.exe'")
                    pass
                elif 'deny calculator' in query:
                    SR.speak(" Closing calculator")
                    os.system("taskkill /f /im calc.exe'")
                    pass

            elif there_exists(['shut down', 'shut down my pc', 'shut this pc down', 'shut down the pc'
                               ], query):
                if 'shut down' in query:
                    m5 = Annex.shutdown()
                    m5.shut(textarea)
                    del m5
                    pass

                elif 'shut this pc down' in query:
                    m5 = Annex.shutdown()
                    m5.shut(textarea)
                    del m5
                    pass

                elif 'shut down my pc' in query:
                    m5 = Annex.shutdown()
                    m5.shut(textarea)
                    del m5
                    pass

                elif 'shut down the pc' in query:
                    m5 = Annex.shutdown()
                    m5.shut(textarea)
                    del m5
                    pass

            elif there_exists(['restart', 'restart my pc', 'restart this pc down', 'restart the pc'
                               ], query):
                if 'restart' in query:
                    m5 = Annex.restart()
                    m5.rest(textarea)
                    del m5
                    pass



                elif 'restart this pc down' in query:
                    m5 = Annex.restart()
                    m5.rest(textarea)
                    del m5
                    pass

                elif 'restart my pc' in query:
                    m5 = Annex.restart()
                    m5.rest(textarea)
                    del m5
                    pass

                elif 'restart the pc' in query:
                    m5 = Annex.restart()
                    m5.rest(textarea)
                    del m5
                    pass

            elif there_exists(['log out my pc', 'log out this pc down', 'log out the pc', 'logout', 'log out'
                               ], query):
                if 'log out my pc' in query:
                    m5 = Annex.logout()
                    m5.log(textarea)
                    del m5
                    pass


                elif 'log out this pc down' in query:
                    m5 = Annex.logout()
                    m5.log(textarea)
                    del m5
                    pass


                elif 'log out the pc' in query:
                    m5 = Annex.logout()
                    m5.log(textarea)
                    del m5
                    pass



                elif 'logout' in query:
                    m5 = Annex.logout()
                    m5.log(textarea)
                    del m5
                    pass



                elif 'log out' in query:
                    m5 = Annex.logout()
                    m5.log(textarea)
                    del m5
                    pass


            elif there_exists(['mute my pc', 'mute this pc ', 'mute the pc'
                               ], query):
                if 'mute my pc' in query:
                    SR.speak("Muting Sound")
                    pyautogui.hotkey('volumemute')
                    pass
                elif 'mute this pc' in query:
                    SR.speak("Muting Sound")
                    pyautogui.hotkey('volumemute')
                    pass
                elif 'mute the pc' in query:
                    SR.speak("Muting Sound")
                    pyautogui.hotkey('volumemute')
                    pass

            elif there_exists(
                    ['minimize my screen', 'minimize my window ', 'minimize', 'small screen', 'small my screen'
                     ], query):
                if 'minimize my screen' in query:
                    SR.speak("Minimizing Screen")
                    pyautogui.keyDown('winleft')
                    pyautogui.keyDown('down')
                    pyautogui.keyUp('winleft')
                    pyautogui.keyUp('down')
                    pass
                elif 'minimize my window' in query:
                    SR.speak("Minimizing Screen")
                    pyautogui.keyDown('winleft')
                    pyautogui.keyDown('down')
                    pyautogui.keyUp('winleft')
                    pyautogui.keyUp('down')
                    pass
                elif 'minimize' in query:
                    SR.speak("Minimizing Screen")
                    pyautogui.keyDown('winleft')
                    pyautogui.keyDown('down')
                    pyautogui.keyUp('winleft')
                    pyautogui.keyUp('down')
                    pass
                elif 'small screen' in query:
                    SR.speak("Minimizing Screen")
                    pyautogui.keyDown('winleft')
                    pyautogui.keyDown('down')
                    pyautogui.keyUp('winleft')
                    pyautogui.keyUp('down')
                    pass
                elif 'small my screen' in query:
                    SR.speak("Minimizing Screen")
                    pyautogui.keyDown('winleft')
                    pyautogui.keyDown('down')
                    pyautogui.keyUp('winleft')
                    pyautogui.keyUp('down')
                    pass

            elif there_exists(
                    ['maximize my screen', 'maximize my window ', 'maximize', 'big screen', 'big my screen'
                     ], query):
                if 'maximize my screen' in query:
                    SR.speak("Maximizing Screen")
                    pyautogui.keyDown('winleft')
                    pyautogui.keyDown('up')
                    pyautogui.keyUp('winleft')
                    pyautogui.keyUp('up')
                    pass
                elif 'maximize my window' in query:
                    SR.speak("Maximizing Screen")
                    pyautogui.keyDown('winleft')
                    pyautogui.keyDown('up')
                    pyautogui.keyUp('winleft')
                    pyautogui.keyUp('up')
                    pass
                elif 'maximize' in query:
                    SR.speak("Maximizing Screen")
                    pyautogui.keyDown('winleft')
                    pyautogui.keyDown('up')
                    pyautogui.keyUp('winleft')
                    pyautogui.keyUp('up')
                    pass
                elif 'big screen' in query:
                    SR.speak("Maximizing Screen")
                    pyautogui.keyDown('winleft')
                    pyautogui.keyDown('up')
                    pyautogui.keyUp('winleft')
                    pyautogui.keyUp('up')
                    pass
                elif 'big my screen' in query:
                    SR.speak("Maximizing Screen")
                    pyautogui.keyDown('winleft')
                    pyautogui.keyDown('up')
                    pyautogui.keyUp('winleft')
                    pyautogui.keyUp('up')
                    pass

            elif there_exists(
                    ['exit my screen', 'exit my window ', 'exit', 'exit screen', 'exit my screen'
                     ], query):
                if 'exit my screen' in query:
                    SR.speak("EXIT")
                    pyautogui.keyDown('altleft')
                    pyautogui.keyDown('f4')
                    pyautogui.keyUp('altleft')
                    pyautogui.keyUp('f4')
                    pass
                elif 'exit my window' in query:
                    SR.speak("EXIT")
                    pyautogui.keyDown('altleft')
                    pyautogui.keyDown('f4')
                    pyautogui.keyUp('altleft')
                    pyautogui.keyUp('f4')
                    pass
                elif 'exit' in query:
                    SR.speak("EXIT")
                    pyautogui.keyDown('altleft')
                    pyautogui.keyDown('f4')
                    pyautogui.keyUp('altleft')
                    pyautogui.keyUp('f4')
                    pass
                elif 'exit screen' in query:
                    SR.speak("EXIT")
                    pyautogui.keyDown('altleft')
                    pyautogui.keyDown('f4')
                    pyautogui.keyUp('altleft')
                    pyautogui.keyUp('f4')
                    pass
                elif 'exit my screen' in query:
                    SR.speak("EXIT")
                    pyautogui.keyDown('altleft')
                    pyautogui.keyDown('f4')
                    pyautogui.keyUp('altleft')
                    pyautogui.keyUp('f4')
                    pass

            elif there_exists(
                    ['back', 'go back', 'move back', 'moveback'
                     ], query):
                if 'back' in query:
                    SR.speak("Back")
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('left')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('left')
                    pass
                elif 'go back' in query:
                    SR.speak("Back")
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('left')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('left')
                    pass
                elif 'move back' in query:
                    SR.speak("Back")
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('left')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('left')
                    pass
                elif 'moveback' in query:
                    SR.speak("Back")
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('left')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('left')
                    pass

            elif there_exists(
                    ['forward', 'go forward', 'move forward', 'moveforward'
                     ], query):
                if 'forward' in query:
                    SR.speak("Forward")
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('right')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('right')
                    pass
                elif 'go forward' in query:
                    SR.speak("Forward")
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('right')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('right')
                    pass
                elif 'move forward' in query:
                    SR.speak("Forward")
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('right')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('right')
                    pass
                elif 'moveforward' in query:
                    SR.speak("Forward")
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('right')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('right')
                    pass

            elif there_exists(
                    ['search and open'
                     ], query):
                if 'search and open' in query:
                    query = query.replace("search and open", "")
                    SR.speak("Opening" + query)
                    pyautogui.hotkey('win', 'd')
                    pyautogui.press('win')
                    pyautogui.write(query)
                    pyautogui.press("enter")
                    pass







            elif there_exists(
                    ['go up', 'up'
                     ], query):
                if 'go up' in query:
                    SR.speak("Up")
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('up')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('up')
                    pass
                elif 'up' in query:
                    SR.speak("Up")
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('up')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('up')
                    pass
            elif there_exists(['find location of', 'show location of', 'find location for', 'show location for'],
                              query):
                if 'of' in query:
                    url = 'https://google.nl/maps/place/' + query[query.find('of') + 3:] + '/&amp'
                    webbrowser.get(chrome_path).open(url)
                    pass
                elif 'for' in query:
                    url = 'https://google.nl/maps/place/' + query[query.find('for') + 4:] + '/&amp'
                    webbrowser.get(chrome_path).open(url)
                    pass

            elif there_exists(["show my location", "what is my location", "tell me my location",
                               "tell me my current location", "what is my current location"], query):
                if "show my location" in query:
                    SR.speak("Showing your location on google maps...")
                    url = "https://www.google.com/maps/search/Where+am+I+?/"
                    webbrowser.get().open(url)
                    pass

                elif "what is my location" in query:
                    SR.speak("Showing your location on google maps...")
                    url = "https://www.google.com/maps/search/Where+am+I+?/"
                    webbrowser.get().open(url)
                    pass

                elif "tell me my location" in query:
                    SR.speak("Showing your location on google maps...")
                    url = "https://www.google.com/maps/search/Where+am+I+?/"
                    webbrowser.get().open(url)
                    pass

                elif "tell me my current location" in query:
                    SR.speak("Showing your location on google maps...")
                    url = "https://www.google.com/maps/search/Where+am+I+?/"
                    webbrowser.get().open(url)
                    pass

                elif "what is my current location" in query:
                    SR.speak("Showing your location on google maps...")
                    url = "https://www.google.com/maps/search/Where+am+I+?/"
                    webbrowser.get().open(url)
                    pass
            elif there_exists(["where am i", "where do i live", "where i live", 'tell me where am i'], query):
                if "where am i" in query:
                    Ip_info = requests.get(
                        'https://api.ipdata.co?api-key=aa4b921dc121bf96c60cb33e7e9dc05eef7e191206228b9e09c0bbc6').json()
                    region = Ip_info['region']
                    country = Ip_info['country_name']
                    latitude = Ip_info['latitude']
                    longitude = Ip_info['longitude']
                    postal = Ip_info['postal']
                    SR.speak(f"You must be somewhere in {region} in {country} with {latitude}"
                             f" as latitude and {longitude} as longitude and you postal code is {postal} ")
                    pass

                elif "where do i live" in query:
                    Ip_info = requests.get(
                        'https://api.ipdata.co?api-key=aa4b921dc121bf96c60cb33e7e9dc05eef7e191206228b9e09c0bbc6').json()
                    region = Ip_info['region']
                    country = Ip_info['country_name']
                    latitude = Ip_info['latitude']
                    longitude = Ip_info['longitude']
                    postal = Ip_info['postal']
                    SR.speak(f"You must be somewhere in {region} in {country} with {latitude}"
                             f" as latitude and {longitude} as longitude and you postal code is {postal} ")
                    pass

                elif "where i live" in query:
                    Ip_info = requests.get(
                        'https://api.ipdata.co?api-key=aa4b921dc121bf96c60cb33e7e9dc05eef7e191206228b9e09c0bbc6').json()
                    region = Ip_info['region']
                    country = Ip_info['country_name']
                    latitude = Ip_info['latitude']
                    longitude = Ip_info['longitude']
                    postal = Ip_info['postal']
                    SR.speak(f"You must be somewhere in {region} in {country} with {latitude}"
                             f" as latitude and {longitude} as longitude and you postal code is {postal} ")
                    pass

                elif "tell me where am i" in query:
                    Ip_info = requests.get(
                        'https://api.ipdata.co?api-key=aa4b921dc121bf96c60cb33e7e9dc05eef7e191206228b9e09c0bbc6').json()
                    region = Ip_info['region']
                    country = Ip_info['country_name']
                    latitude = Ip_info['latitude']
                    longitude = Ip_info['longitude']
                    postal = Ip_info['postal']
                    SR.speak(f"You must be somewhere in {region} in {country} with {latitude}"
                             f" as latitude and {longitude} as longitude and you postal code is {postal} ")
                    pass


            elif there_exists(["tell me about my system", "tell me about my system condition", "system condition",
                               "tell me about my system situation", "system situation", "check the system condition",
                               "check my system condition", "check the system situation", "check my system condition"],
                              query):
                if 'tell me about my system' in query:
                    freq = str(psutil.cpu_freq())
                    times = str(psutil.cpu_times())
                    usage = str(psutil.cpu_percent())
                    disk = str(psutil.disk_usage('/'))
                    memory = str(psutil.virtual_memory())
                    delta = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
                    uptimeWeeks = divmod(delta.days, 7)[0]
                    uptimeHours, remainder = divmod(delta.seconds, 3600)
                    uptimeMins = divmod(remainder, 60)[0]
                    uptime = f'the computer wake up for {uptimeWeeks:2}week ,{delta.days:2}day, {uptimeHours:2}hour and {uptimeMins:2}minute'

                    SR.speak("CPU is at" + usage + " percentage \n" + freq +
                             "\n" + times + "\n" + disk + "\n" + memory + "\n" + uptime)
                    mem = psutil.virtual_memory()
                    THRESHOLD = 100 * 1024 * 1024  # 100MB
                    if mem.available <= THRESHOLD:
                        SR.speak("Virtual memory is more then 100MB , warning , warning, warning")
                    else:
                        SR.speak("Virtual memory is less then 100MB , it is normal")
                    percentage_usage = psutil.cpu_percent()
                    if 1 <= percentage_usage <= 10:
                        SR.speak(f"Boss CPU usage is too normal")
                    elif 11 <= percentage_usage <= 20:
                        SR.speak(f"Boss CPU usage is  normal")
                    elif 21 <= percentage_usage <= 50:
                        SR.speak(f"Boss CPU usage is high ")
                    else:
                        SR.speak(f"Boss CPU usage is too high ")
                    battray = psutil.sensors_battery()
                    percentage = battray.percent
                    SR.speak(f"our system have {percentage} percentage Battery")
                    if percentage >= 75:
                        SR.speak(f"we could have enough charging to continue our work")
                    elif percentage >= 40 and percentage <= 75:
                        SR.speak(f" we should connect out system to charging point to charge our battery")
                    elif percentage >= 15 and percentage <= 30:
                        SR.speak(f" we don't have enough power to work, please connect to charging")
                    else:
                        SR.speak(
                            f" we have very low power, please connect to charging"
                            f" otherwise the system will shutdown very soon")
                        pass



                elif 'tell me about my system condition' in query:
                    freq = str(psutil.cpu_freq())
                    times = str(psutil.cpu_times())
                    usage = str(psutil.cpu_percent())
                    disk = str(psutil.disk_usage('/'))
                    memory = str(psutil.virtual_memory())
                    SR.speak("CPU is at" + usage + " percentage \n" + freq +
                             "\n" + times + "\n" + disk + "\n" + memory)
                    mem = psutil.virtual_memory()
                    THRESHOLD = 100 * 1024 * 1024  # 100MB
                    if mem.available <= THRESHOLD:
                        SR.speak("Virtual memory is more then 100MB , warning , warning, warning")
                    else:
                        SR.speak("Virtual memory is less then 100MB , it is normal")
                    percentage_usage = psutil.cpu_percent()
                    if 1 <= percentage_usage <= 10:
                        SR.speak(f"Boss CPU usage is too normal")
                    elif 11 <= percentage_usage <= 20:
                        SR.speak(f"Boss CPU usage is  normal")
                    elif 21 <= percentage_usage <= 50:
                        SR.speak(f"Boss CPU usage is high ")
                    else:
                        SR.speak(f"Boss CPU usage is too high ")
                    battray = psutil.sensors_battery()
                    percentage = battray.percent
                    SR.speak(f"our system have {percentage} percentage Battery")
                    if percentage >= 75:
                        SR.speak(f"we could have enough charging to continue our work")
                    elif percentage >= 40 and percentage <= 75:
                        SR.speak(f" we should connect out system to charging point to charge our battery")
                    elif percentage >= 15 and percentage <= 30:
                        SR.speak(f" we don't have enough power to work, please connect to charging")
                    else:
                        SR.speak(
                            f" we have very low power, please connect to charging"
                            f" otherwise the system will shutdown very soon")
                        pass

                elif 'system condition' in query:
                    freq = str(psutil.cpu_freq())
                    times = str(psutil.cpu_times())
                    usage = str(psutil.cpu_percent())
                    disk = str(psutil.disk_usage('/'))
                    memory = str(psutil.virtual_memory())
                    SR.speak("CPU is at" + usage + " percentage \n" + freq +
                             "\n" + times + "\n" + disk + "\n" + memory)
                    mem = psutil.virtual_memory()
                    THRESHOLD = 100 * 1024 * 1024  # 100MB
                    if mem.available <= THRESHOLD:
                        SR.speak("Virtual memory is more then 100MB , warning , warning, warning")
                    else:
                        SR.speak("Virtual memory is less then 100MB , it is normal")
                    percentage_usage = psutil.cpu_percent()
                    if 1 <= percentage_usage <= 10:
                        SR.speak(f"Boss CPU usage is too normal")
                    elif 11 <= percentage_usage <= 20:
                        SR.speak(f"Boss CPU usage is  normal")
                    elif 21 <= percentage_usage <= 50:
                        SR.speak(f"Boss CPU usage is high ")
                    else:
                        SR.speak(f"Boss CPU usage is too high ")
                    battray = psutil.sensors_battery()
                    percentage = battray.percent
                    SR.speak(f"our system have {percentage} percentage Battery")
                    if percentage >= 75:
                        SR.speak(f"we could have enough charging to continue our work")
                    elif percentage >= 40 and percentage <= 75:
                        SR.speak(f" we should connect out system to charging point to charge our battery")
                    elif percentage >= 15 and percentage <= 30:
                        SR.speak(f" we don't have enough power to work, please connect to charging")
                    else:
                        SR.speak(
                            f" we have very low power, please connect to charging"
                            f" otherwise the system will shutdown very soon")
                        pass

                elif 'tell me about my system situation' in query:
                    freq = str(psutil.cpu_freq())
                    times = str(psutil.cpu_times())
                    usage = str(psutil.cpu_percent())
                    disk = str(psutil.disk_usage('/'))
                    memory = str(psutil.virtual_memory())
                    SR.speak("CPU is at" + usage + " percentage \n" + freq +
                             "\n" + times + "\n" + disk + "\n" + memory)
                    mem = psutil.virtual_memory()
                    THRESHOLD = 100 * 1024 * 1024  # 100MB
                    if mem.available <= THRESHOLD:
                        SR.speak("Virtual memory is more then 100MB , warning , warning, warning")
                    else:
                        SR.speak("Virtual memory is less then 100MB , it is normal")
                    percentage_usage = psutil.cpu_percent()
                    if 1 <= percentage_usage <= 10:
                        SR.speak(f"Boss CPU usage is too normal")
                    elif 11 <= percentage_usage <= 20:
                        SR.speak(f"Boss CPU usage is  normal")
                    elif 21 <= percentage_usage <= 50:
                        SR.speak(f"Boss CPU usage is high ")
                    else:
                        SR.speak(f"Boss CPU usage is too high ")
                    battray = psutil.sensors_battery()
                    percentage = battray.percent
                    SR.speak(f"our system have {percentage} percentage Battery")
                    if percentage >= 75:
                        SR.speak(f"we could have enough charging to continue our work")
                    elif percentage >= 40 and percentage <= 75:
                        SR.speak(f" we should connect out system to charging point to charge our battery")
                    elif percentage >= 15 and percentage <= 30:
                        SR.speak(f" we don't have enough power to work, please connect to charging")
                    else:
                        SR.speak(
                            f" we have very low power, please connect to charging"
                            f" otherwise the system will shutdown very soon")
                        pass

                elif 'system situation' in query:
                    freq = str(psutil.cpu_freq())
                    times = str(psutil.cpu_times())
                    usage = str(psutil.cpu_percent())
                    disk = str(psutil.disk_usage('/'))
                    memory = str(psutil.virtual_memory())
                    SR.speak("CPU is at" + usage + " percentage \n" + freq +
                             "\n" + times + "\n" + disk + "\n" + memory)
                    mem = psutil.virtual_memory()
                    THRESHOLD = 100 * 1024 * 1024  # 100MB
                    if mem.available <= THRESHOLD:
                        SR.speak("Virtual memory is more then 100MB , warning , warning, warning")
                    else:
                        SR.speak("Virtual memory is less then 100MB , it is normal")
                    percentage_usage = psutil.cpu_percent()
                    if 1 <= percentage_usage <= 10:
                        SR.speak(f"Boss CPU usage is too normal")
                    elif 11 <= percentage_usage <= 20:
                        SR.speak(f"Boss CPU usage is  normal")
                    elif 21 <= percentage_usage <= 50:
                        SR.speak(f"Boss CPU usage is high ")
                    else:
                        SR.speak(f"Boss CPU usage is too high ")
                    battray = psutil.sensors_battery()
                    percentage = battray.percent
                    SR.speak(f"our system have {percentage} percentage Battery")
                    if percentage >= 75:
                        SR.speak(f"we could have enough charging to continue our work")
                    elif percentage >= 40 and percentage <= 75:
                        SR.speak(f" we should connect out system to charging point to charge our battery")
                    elif percentage >= 15 and percentage <= 30:
                        SR.speak(f" we don't have enough power to work, please connect to charging")
                    else:
                        SR.speak(
                            f" we have very low power, please connect to charging"
                            f" otherwise the system will shutdown very soon")
                        pass

                elif 'check the system condition' in query:
                    freq = str(psutil.cpu_freq())
                    times = str(psutil.cpu_times())
                    usage = str(psutil.cpu_percent())
                    disk = str(psutil.disk_usage('/'))
                    memory = str(psutil.virtual_memory())
                    SR.speak("CPU is at" + usage + " percentage \n" + freq +
                             "\n" + times + "\n" + disk + "\n" + memory)
                    mem = psutil.virtual_memory()
                    THRESHOLD = 100 * 1024 * 1024  # 100MB
                    if mem.available <= THRESHOLD:
                        SR.speak("Virtual memory is more then 100MB , warning , warning, warning")
                    else:
                        SR.speak("Virtual memory is less then 100MB , it is normal")
                    percentage_usage = psutil.cpu_percent()
                    if 1 <= percentage_usage <= 10:
                        SR.speak(f"Boss CPU usage is too normal")
                    elif 11 <= percentage_usage <= 20:
                        SR.speak(f"Boss CPU usage is  normal")
                    elif 21 <= percentage_usage <= 50:
                        SR.speak(f"Boss CPU usage is high ")
                    else:
                        SR.speak(f"Boss CPU usage is too high ")
                    battray = psutil.sensors_battery()
                    percentage = battray.percent
                    SR.speak(f"our system have {percentage} percentage Battery")
                    if percentage >= 75:
                        SR.speak(f"we could have enough charging to continue our work")
                    elif percentage >= 40 and percentage <= 75:
                        SR.speak(f" we should connect out system to charging point to charge our battery")
                    elif percentage >= 15 and percentage <= 30:
                        SR.speak(f" we don't have enough power to work, please connect to charging")
                    else:
                        SR.speak(
                            f" we have very low power, please connect to charging"
                            f" otherwise the system will shutdown very soon")
                        pass

                elif 'check the system situation' in query:
                    freq = str(psutil.cpu_freq())
                    times = str(psutil.cpu_times())
                    usage = str(psutil.cpu_percent())
                    disk = str(psutil.disk_usage('/'))
                    memory = str(psutil.virtual_memory())
                    SR.speak("CPU is at" + usage + " percentage \n" + freq +
                             "\n" + times + "\n" + disk + "\n" + memory)
                    mem = psutil.virtual_memory()
                    THRESHOLD = 100 * 1024 * 1024  # 100MB
                    if mem.available <= THRESHOLD:
                        SR.speak("Virtual memory is more then 100MB , warning , warning, warning")
                    else:
                        SR.speak("Virtual memory is less then 100MB , it is normal")
                    percentage_usage = psutil.cpu_percent()
                    if 1 <= percentage_usage <= 10:
                        SR.speak(f"Boss CPU usage is too normal")
                    elif 11 <= percentage_usage <= 20:
                        SR.speak(f"Boss CPU usage is  normal")
                    elif 21 <= percentage_usage <= 50:
                        SR.speak(f"Boss CPU usage is high ")
                    else:
                        SR.speak(f"Boss CPU usage is too high ")
                    battray = psutil.sensors_battery()
                    percentage = battray.percent
                    SR.speak(f"our system have {percentage} percentage Battery")
                    if percentage >= 75:
                        SR.speak(f"we could have enough charging to continue our work")
                    elif percentage >= 40 and percentage <= 75:
                        SR.speak(f" we should connect out system to charging point to charge our battery")
                    elif percentage >= 15 and percentage <= 30:
                        SR.speak(f" we don't have enough power to work, please connect to charging")
                    else:
                        SR.speak(
                            f" we have very low power, please connect to charging"
                            f" otherwise the system will shutdown very soon")
                        pass

                elif 'check my system condition' in query:
                    freq = str(psutil.cpu_freq())
                    times = str(psutil.cpu_times())
                    usage = str(psutil.cpu_percent())
                    disk = str(psutil.disk_usage('/'))
                    memory = str(psutil.virtual_memory())
                    SR.speak("CPU is at" + usage + " percentage \n" + freq +
                             "\n" + times + "\n" + disk + "\n" + memory)
                    mem = psutil.virtual_memory()
                    THRESHOLD = 100 * 1024 * 1024  # 100MB
                    if mem.available <= THRESHOLD:
                        SR.speak("Virtual memory is more then 100MB , warning , warning, warning")
                    else:
                        SR.speak("Virtual memory is less then 100MB , it is normal")
                    percentage_usage = psutil.cpu_percent()
                    if 1 <= percentage_usage <= 10:
                        SR.speak(f"Boss CPU usage is too normal")
                    elif 11 <= percentage_usage <= 20:
                        SR.speak(f"Boss CPU usage is  normal")
                    elif 21 <= percentage_usage <= 50:
                        SR.speak(f"Boss CPU usage is high ")
                    else:
                        SR.speak(f"Boss CPU usage is too high ")
                    battray = psutil.sensors_battery()
                    percentage = battray.percent
                    SR.speak(f"our system have {percentage} percentage Battery")
                    if percentage >= 75:
                        SR.speak(f"we could have enough charging to continue our work")
                    elif percentage >= 40 and percentage <= 75:
                        SR.speak(f" we should connect out system to charging point to charge our battery")
                    elif percentage >= 15 and percentage <= 30:
                        SR.speak(f" we don't have enough power to work, please connect to charging")
                    else:
                        SR.speak(
                            f" we have very low power, please connect to charging"
                            f" otherwise the system will shutdown very soon")
                        pass

            elif there_exists(
                    ['pause', 'pause the song', 'pause the video', 'pause song', 'pause video',
                     'pause youtube'], query):
                if 'pause' in query:
                    SR.speak("pausing...")
                    pyautogui.hotkey('space')
                    pass

                elif 'pause the song' in query:
                    SR.speak("pausing the song")
                    pyautogui.hotkey('space')
                    pass

                elif 'pause the video' in query:
                    SR.speak("pausing the video")
                    pyautogui.hotkey('space')


                elif 'pause song' in query:
                    SR.speak("pausing the song")
                    pyautogui.hotkey('space')
                    pass

                elif 'pause video' in query:
                    SR.speak("pausing the video")
                    pyautogui.hotkey('space')
                    pass

                elif 'pause youtube' in query:
                    SR.speak("pausing youtube")
                    pyautogui.hotkey('space')
                    pass

            elif there_exists(['Suggest to me a password', 'Password suggestion',
                               'I want password', 'give me password'], query):
                if "Suggest to me a password" in query:
                    m3 = Annex.PasswordGenerator()
                    m3.givePSWD(textarea)
                    del m3
                    pass
                elif "Password suggestion" in query:
                    m3 = Annex.PasswordGenerator()
                    m3.givePSWD(textarea)
                    del m3
                    pass
                elif "I want password" in query:
                    m3 = Annex.PasswordGenerator()
                    m3.givePSWD(textarea)
                    del m3
                    pass
                elif "give me password" in query:
                    m3 = Annex.PasswordGenerator()
                    m3.givePSWD(textarea)
                    del m3
                    pass

            elif there_exists(['top news',
                               'listen some news', 'news of today', 'tell me news',
                               'news today', 'today news', 'tell me news of today'], query):
                if "top news" in query:
                    news = Annex.News(textarea)
                    news.show()
                    pass
                elif "listen some news" in query:
                    news = Annex.News(textarea)
                    news.show()
                    pass
                elif "news of today" in query:
                    news = Annex.News(textarea)
                    news.show()
                    pass
                elif "tell me news" in query:
                    news = Annex.News(textarea)
                    news.show()
                    pass
                elif "news today" in query:
                    news = Annex.News(textarea)
                    news.show()
                    pass
                elif "today news" in query:
                    news = Annex.News(textarea)
                    news.show()
                    pass
                elif "tell me news of today" in query:
                    news = Annex.News(textarea)
                    news.show()
                    pass

            elif there_exists(['send a whatsapp message', 'send whatsapp message',
                               'please send a whatsapp message'], query):
                # +60 11-3776 3521
                # +60 11-6994 5306
                # +60 16_215-0019
                if 'send a whatsapp message' in query:
                    whatsapp = Annex.WhatsApp(textarea)
                    whatsapp.send()
                    del whatsapp
                    pass



                elif 'send whatsapp message' in query:
                    whatsapp = Annex.WhatsApp(textarea)
                    whatsapp.send()
                    del whatsapp
                    pass

                elif 'please send a whatsapp message' in query:
                    whatsapp = Annex.WhatsApp(textarea)
                    whatsapp.send()
                    del whatsapp
                    pass

            elif there_exists(
                    ['take a photo', 'take a selfie', 'take my photo', 'take photo', 'take selfie',
                     'one photo please',
                     'click a photo'], query):
                SR.speak("Show me my master beautiful Smile, Cheeeers.")
                takephoto = Annex.camera()
                Location = takephoto.takePhoto()
                os.startfile(Location)
                del takephoto
                SR.speak("Captured picture is stored in Camera folder.")
                pass


            elif there_exists(['send some files through bluetooth', 'send file through bluetooth', 'bluetooth sharing',
                               'bluetooth file sharing', 'open bluetooth'], query):

                if 'send some files through bluetooth' in query:
                    SR.speak("Opening bluetooth...")
                    os.startfile(r"C:\Windows\System32\fsquirt.exe")
                    pass

                elif 'open bluetooth' in query:
                    SR.speak("Opening bluetooth...")
                    os.startfile(r"C:\Windows\System32\fsquirt.exe")
                    pass

                elif 'send file through bluetooth' in query:
                    SR.speak("Opening bluetooth...")
                    os.startfile(r"C:\Windows\System32\fsquirt.exe")
                    pass

                elif 'bluetooth sharing' in query:
                    SR.speak("Opening bluetooth...")
                    os.startfile(r"C:\Windows\System32\fsquirt.exe")
                    pass

                elif 'bluetooth file sharing' in query:
                    SR.speak("Opening bluetooth...")
                    os.startfile(r"C:\Windows\System32\fsquirt.exe")
                    pass

                elif 'open bluetooth' in query:
                    SR.speak("Opening bluetooth...")
                    os.startfile(r"C:\Windows\System32\fsquirt.exe")
                    pass

            elif there_exists(
                    ['make a note', 'take note', 'take a note', 'note it down', 'make note', 'remember this as note',
                     'open notepad and write'], query):
                SR.speak("What would you like to write down?")
                data = SR.takeCommand()
                n = Annex.note()
                n.Note(data)
                SR.speak("I have a made a note of that.")
                pass

            elif there_exists(["toss a coin", "flip a coin", "toss"], query):
                moves = ["head", "tails"]
                cmove = random.choice(moves)
                SR.speak("It's " + cmove)
                pass

            elif there_exists(['the time', 'tell me the time''tell the time'], query):
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                SR.speak(f"Sir, the time is {strTime}")
                pass

            elif there_exists(['the date', 'tell me the date', 'tell the date'], query):
                strDay = datetime.date.today().strftime("%B %d, %Y")
                SR.speak(f"Today is {strDay}")
                pass

            elif there_exists(['what day it is', 'what day is today', 'which day is today', "today's day name please"],
                              query):
                SR.speak(f"Today is {datetime.datetime.now().strftime('%A')}")
                pass

            elif there_exists(['show me performance of my system', 'open performance monitor', 'performance monitor',
                               'performance of my computer', 'performance of this computer'], query):
                os.startfile("C:\Windows\System32\perfmon.exe")
                pass

            elif there_exists(['open snipping tool', 'snipping tool', 'start snipping tool'], query):
                SR.speak("Opening snipping tool....")
                os.startfile("C:\Windows\System32\SnippingTool.exe")
                pass

            elif there_exists(['open code', 'open visual studio ', 'open vs code'], query):
                SR.speak("Opeining vs code")
                codepath = r"C:\Users\Vishal\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                os.startfile(codepath)
                pass

            elif there_exists(
                    ['open file manager', 'file manager', 'open my computer', 'my computer', 'open file explorer',
                     'file explorer', 'open this pc', 'this pc'], query):
                SR.speak("Opening File Explorer")
                os.startfile("C:\Windows\explorer.exe")
                pass

            elif there_exists(['powershell'], query):
                SR.speak("Opening powershell")
                os.startfile(r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe')
                pass

            elif there_exists(['cmd', 'command prompt', 'command prom', 'commandpromt', ], query):
                SR.speak("Opening command prompt")
                os.startfile(r'C:\Windows\System32\cmd.exe')
                pass

            elif there_exists(['open settings', 'open control panel', 'open this computer setting Window',
                               'open computer setting Window', 'open computer settings', 'open setting',
                               'show me settings', 'open my computer settings'], query):
                SR.speak("Opening settings...")
                os.startfile('C:\Windows\System32\control.exe')
                pass

            elif there_exists(
                    ['open your setting', 'open your settings', 'open settiing window', 'show me setting window',
                     'open voice assistant settings'], query):
                SR.speak("Opening my Setting window..")
                sett_wind = Annex.SettingWindow()
                sett_wind.settingWindow(root)
                pass

            elif there_exists(['take screenshot', 'take a screenshot', 'screenshot please', 'capture my screen'],
                              query):
                SR.speak("Taking screenshot")
                SS = Annex.screenshot()
                SS.takeSS()
                SR.speak('Captured screenshot is saved in Screenshots folder.')
                del SS
                pass

            elif there_exists(['record my voice', 'start voice recorder', 'voice recorder'], query):
                VR = Annex.VoiceRecorer()
                VR.Record(textarea)
                del VR
                pass

            elif there_exists(['text to speech', 'convert my notes to voice'], query):
                SR.speak("Opening Text to Speech mode")
                TS = Annex.TextSpeech()
                del TS
                pass

            elif there_exists(['weather report', 'temperature'], query):
                Weather = Annex.Weather()
                Weather.show(textarea)
                pass

            elif there_exists(['none'], query):
                pass

            elif there_exists(['put alarm', 'set an alarm', 'set alarm', 'put an alarm'], query):
                Alarm = Annex.Alarm(textarea)
                Alarm.alarm1()

                del Alarm
                pass












            elif there_exists(['stop the flow', 'stop the execution', 'halt', 'halt the process', 'stop the process',
                               'stop listening', 'stop the listening'], query):
                SR.speak("Listening halted.")
                break
            elif there_exists(
                    ['search something for me', 'to do a little search', 'search mode', 'i want to search something'],
                    query):
                SR.speak('What you want me to search for?')
                query = SR.takeCommand()
                SR.speak(f"Showing results for {query}")
                try:
                    res = app.query(query)
                    SR.speak(next(res.results).text)
                    pass
                except:
                    print("Sorry, but there is a little problem while fetching the result.")
                    pass

            # what is the capital
            elif there_exists(['what is the capital of', 'capital of', 'capital city of'], query):
                try:
                    res = app.query(query)
                    SR.speak(next(res.results).text)
                    pass
                except:
                    print("Sorry, but there is a little problem while fetching the result.")
                    pass

            elif there_exists(['temperature'], query):
                try:
                    res = app.query(query)
                    SR.speak(next(res.results).text)
                    pass
                except:
                    print("Internet Connection Error")
                    pass
            elif there_exists(
                    ['+', '-', '*', 'x', '/', 'plus', 'add', 'minus', 'subtract', 'divide', 'multiply', 'divided',
                     'multiplied'], query):
                try:
                    res = app.query(query)
                    SR.speak(next(res.results).text)
                    pass
                except:
                    print("Internet Connection Error")
                    pass

            else:
                SR.speak("sorry,I don't know how to replay to that yet.")
                pass

    except Exception as e:
        pass


def gen(n):
    for i in range(n):
        yield i


class MainframeThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        mainframe()


def greet1():
    conn = sqlite3.connect('Heisenberg.db')
    mycursor = conn.cursor()
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        mycursor.execute('select sentences from goodmorning')
        result = mycursor.fetchall()
        SR.speak(random.choice(result)[0])
    elif hour >= 12 and hour < 18:
        mycursor.execute('select sentences from goodafternoon')
        result = mycursor.fetchall()
        SR.speak(random.choice(result)[0])
    elif hour >= 18 and hour < 21:
        mycursor.execute('select sentences from goodevening')
        result = mycursor.fetchall()
        SR.speak(random.choice(result)[0])
    else:
        mycursor.execute('select sentences from night')
        result = mycursor.fetchall()
        SR.speak(random.choice(result)[0])
    conn.commit()
    conn.close()


def there_exists1(terms1, question):
    for term in terms1:
        if term in question:
            return True


def botReply():
    SR.scrollable_text_clearing()

    query_for_future = None
    query_for_name = None
    query_for_username = None
    try:
        while (True):
            delta = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
            uptimeWeeks = divmod(delta.days, 7)[0]
            uptimeHours, remainder = divmod(delta.seconds, 3600)
            uptimeMins = divmod(remainder, 60)[0]
            uptime = f'the computer wake up for {uptimeWeeks:2}week ,{delta.days:2}day, {uptimeHours:2}hour and {uptimeMins:2}minute'
            print(uptime)
            question = qf.get()
            textarea.insert(END, 'You: ' + question + '\n\n')
            if there_exists1(['search wikipedia for', 'wikipedia', 'from wikipedia', 'what is meant by',
                              'who the heck is'], question):
                SR.speak("Searching wikipedia...")
                results = wikipedia.summary(question, sentences=2)
                SR.speak("According to wikipedia:\n")
                SR.speak(results)
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

            elif there_exists1(
                    ['tell me joke', 'tell me a joke', 'tell me some jokes', 'i would like to hear some jokes'
                        , "i'd like to hear some jokes", 'can you please tell me some jokes',
                     'i want to hear a joke'
                        , 'i want to hear some jokes', 'please tell me some jokes',
                     'would like to hear some jokes', 'tell me more jokes'], question):
                answer_chioce = ["ok boss,i will tell some jokes listen to this one:",
                                 "This is a funny joke. Listen:",
                                 "oh, my brother,i have to tell jokes? ok, Hear this joke. It is really funny:"]
                greeting = random.choice(answer_chioce)
                SR.speak(greeting)
                if 'tell me joke' in question:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'tell me a joke' in question:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'tell me some jokes' in question:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'i would like to hear some jokes' in question:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'id like to hear some jokes' in question:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'can you please tell me some jokes' in question:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'i want to hear a joke' in question:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'i want to hear some jokes' in question:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'would like to hear some jokes' in question:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'tell me more jokes' in question:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
            elif there_exists1(['one more joke', "i want more jokes", 'joke more',
                                'more joke', 'i want more joke',
                                'another joke', 'more', 'another one', "again"], question):
                answer_chioce = ["I will tell you more jokes i think you are bored?",
                                 "I think you like to hear jokes a lot so you ask me so I will tell another joke.",
                                 "I think you should find another way to entertain yourself.  Anyway, here's another joke:"]
                greeting = random.choice(answer_chioce)
                SR.speak(greeting)

                if 'one more joke' in question:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'joke more' in question:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'more joke' in question:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'i want more joke' in question:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'another joke' in question:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'i want more jokes' in question:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'another one' in question:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'more' in question:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'again' in question:
                    SR.speak(pyjokes.get_joke(language="en", category="all"))
                    query_for_future = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(["what is your name",
                                "tell me your name", 'who are you', "your name", "who the hell are you",
                                "name please"], question):
                if 'what is your name' in question:
                    answer_chioce = ["My name is Alex and I'm here to serve you.",
                                     "My name is Alex!  Did you forget me sir?",
                                     "I'm sad because you don't remember me.  I'm Alex your personal assistant!"]
                    greeting = random.choice(answer_chioce)
                    SR.speak(greeting)
                    query_for_name = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'tell me your name' in question:
                    answer_chioce = ["My name is Alex and I'm here to serve you.",
                                     "My name is Alex!  Did you forget me sir?",
                                     "I'm sad because you don't remember me.  I'm Alex your personal assistant!"]
                    greeting = random.choice(answer_chioce)
                    SR.speak(greeting)
                    query_for_name = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'who are you' in question:
                    answer_chioce = ["My name is Alex and I'm here to serve you.",
                                     "My name is Alex!  Did you forget me sir?",
                                     "I'm sad because you don't remember me.  I'm Alex your personal assistant!"]
                    greeting = random.choice(answer_chioce)
                    SR.speak(greeting)
                    query_for_name = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'your name' in question:
                    answer_chioce = ["My name is Alex and I'm here to serve you.",
                                     "My name is Alex!  Did you forget me sir?",
                                     "I'm sad because you don't remember me.  I'm Alex your personal assistant!"]
                    greeting = random.choice(answer_chioce)
                    SR.speak(greeting)
                    query_for_name = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'who the hell are you' in question:
                    answer_chioce = ["My name is Alex and I'm here to serve you.",
                                     "My name is Alex!  Did you forget me sir?",
                                     "I'm sad because you don't remember me.  I'm Alex your personal assistant!"]
                    greeting = random.choice(answer_chioce)
                    SR.speak(greeting)
                    query_for_name = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'who the hell are you' in question:
                    answer_chioce = ["My name is Alex and I'm here to serve you.",
                                     "My name is Alex!  Did you forget me sir?",
                                     "I'm sad because you don't remember me.  I'm Alex your personal assistant!"]
                    greeting = random.choice(answer_chioce)
                    SR.speak(greeting)
                    query_for_name = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'name please' in question:
                    answer_chioce = ["My name is Alex and I'm here to serve you.",
                                     "My name is Alex!  Did you forget me sir?",
                                     "I'm sad because you don't remember me.  I'm Alex your personal assistant!"]
                    greeting = random.choice(answer_chioce)
                    SR.speak(greeting)
                    query_for_name = question
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(['how are you', 'how are you doing', 'are you ok', 'how do you feel'], question):
                conn = sqlite3.connect('Heisenberg.db')
                mycursor = conn.cursor()
                mycursor.execute('select sentences from howareyou')
                result = mycursor.fetchall()
                temporary_data = random.choice(result)[0]
                SR.updating_ST_No_newline(temporary_data + '😃\n')
                SR.nonPrintSpeak(temporary_data)
                conn.close()
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

            elif there_exists1(['what is my name', 'tell me my name', "i don't remember my name", " I want my name",
                                "do you know my name", "my name is"], question):
                SR.speak("Your name is " + str(getpass.getuser()))
                query_for_username = question
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break


            elif there_exists1(['show me calendar', 'display calendar', 'open my calendar',
                                'show me my calendar', "calendar"], question):
                webbrowser.open('https://calendar.google.com/calendar/')
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

            elif there_exists1(['open youtube', 'show youtube',
                                'access youtube'], question):
                if 'open youtube' in question:
                    SR.speak("Opening youtube")
                    webbrowser.open("https://www.youtube.com")

                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'show youtube' in question:
                    SR.speak("Opening youtube")
                    webbrowser.open("https://www.youtube.com")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'access youtube' in question:
                    SR.speak("Opening youtube")
                    webbrowser.open("https://www.youtube.com")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(['play on youtube', 'music in youtube', 'youtube music', 'play song', 'music youtube'],
                               question):
                if 'play on youtube' in question:
                    song = question.replace('play on youtube', '')
                    SR.speak('playing' + song)
                    pywhatkit.playonyt(song)
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'music in youtube' in question:
                    song = question.replace('music in youtube', '')
                    SR.speak('playing' + song)
                    pywhatkit.playonyt(song)
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'youtube music' in question:
                    song = question.replace('youtube music', '')
                    SR.speak('playing' + song)
                    pywhatkit.playonyt(song)
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'play song' in question:
                    song = question.replace('play song', '')
                    SR.speak('playing' + song)
                    pywhatkit.playonyt(song)
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'music youtube' in question:
                    song = question.replace('music youtube', '')
                    SR.speak('playing' + song)
                    pywhatkit.playonyt(song)
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(['open google', 'show google',
                                'access google'], question):
                if 'open google' in question:
                    SR.speak("Opening Google")
                    webbrowser.open("https://www.google.com")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'show google' in question:
                    SR.speak("Opening Google")
                    webbrowser.open("https://www.google.com")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'access google' in question:
                    SR.speak("Opening Google")
                    webbrowser.open("https://www.google.com")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(['open facebook', 'show facebook',
                                'access facebook'], question):
                if 'open facebook' in question:
                    SR.speak("Opening Facebook")
                    webbrowser.open("https://www.facebook.com")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'show facebook' in question:
                    SR.speak("Opening Facebook")
                    webbrowser.open("https://www.facebook.com")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'access facebook' in question:
                    SR.speak("Opening Facebook")
                    webbrowser.open("https://www.facebook.com")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(['google and search'
                                   , 'search on google', 'find in google'], question):
                if 'google and search' in question:
                    google = question.replace("google and search", "")
                    webbrowser.open("https://www.google.com/search?q={}".format(google))
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'search on google' in question:
                    google = question.replace("search on google", "")
                    webbrowser.open("https://www.google.com/search?q={}".format(google))
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'find in google' in question:
                    google = question.replace("find in google", "")
                    webbrowser.open("https://www.google.com/search?q={}".format(google))
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
            elif there_exists1(['open microsoft edge', 'show microsoft edge',
                                'access microsoft edge', 'microsoft edge'], question):
                if 'open microsoft edge' in question:
                    opening = question.replace('open microsoft edge', 'microsoft edge')
                    SR.speak("Opening Microsoft Edge")
                    pyautogui.hotkey('win', 'd')
                    pyautogui.press('win')
                    pyautogui.write(opening)
                    pyautogui.press("enter")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'show microsoft edge' in question:
                    opening = question.replace('show microsoft edge', 'microsoft edge')
                    SR.speak("Opening Microsoft Edge")
                    pyautogui.hotkey('win', 'd')
                    pyautogui.press('win')
                    pyautogui.write(opening)
                    pyautogui.press("enter")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'access microsoft edge' in question:
                    opening = question.replace('access microsoft edge', 'microsoft edge')
                    SR.speak("Opening Microsoft Edge")
                    pyautogui.hotkey('win', 'd')
                    pyautogui.press('win')
                    pyautogui.write(opening)
                    pyautogui.press("enter")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'microsoft edge' in question:
                    opening = question.replace('microsoft edge', 'microsoft edge')
                    SR.speak("Opening Microsoft Edge")
                    pyautogui.hotkey('win', 'd')
                    pyautogui.press('win')
                    pyautogui.write(opening)
                    pyautogui.press("enter")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(['open gmail', 'show gmail',
                                'access gmail', 'gmail'], question):
                if 'open gmail' in question:
                    webbrowser.open('https://mail.google.com/mail/')
                    SR.speak("Opening gmail")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break


                elif 'show gmail' in question:
                    webbrowser.open('https://mail.google.com/mail/')
                    SR.speak("Opening gmail")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'access gmail' in question:
                    webbrowser.open('https://mail.google.com/mail/')
                    SR.speak("Opening gmail")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'gmail' in question:
                    webbrowser.open('https://mail.google.com/mail/')
                    SR.speak("Opening gmail")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(['open maps', 'show maps',
                                'access maps', 'maps'], question):
                if 'open maps' in question:
                    webbrowser.open('https://www.google.co.in/maps/')
                    SR.speak("Opening Google Maps")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break


                elif 'show maps' in question:
                    webbrowser.open('https://www.google.co.in/maps/')
                    SR.speak("Opening Google Maps")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'access maps' in question:
                    webbrowser.open('https://www.google.co.in/maps/')
                    SR.speak("Opening Google Maps")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'maps' in question:
                    webbrowser.open('https://www.google.co.in/maps/')
                    SR.speak("Opening Google Maps")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(['open calculator', 'show calculator',
                                'access calculator'], question):
                if 'open calculator' in question:
                    SR.speak('Opening calculator')
                    os.startfile('C:\\Windows\\System32\\calc.exe')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'show calculator' in question:
                    SR.speak('Opening calculator')
                    os.startfile('C:\\Windows\\System32\\calc.exe')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'access calculator' in question:
                    SR.speak('Opening calculator')
                    os.startfile('C:\\Windows\\System32\\calc.exe')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break


            elif there_exists1(['open notepad', 'show notepad',
                                'access notepad'], question):
                if 'open notepad' in question:
                    SR.speak('Opening notepad')
                    os.startfile('c:\\Windows\\System32\\notepad.exe')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'show notepad' in question:
                    SR.speak('Opening notepad')
                    os.startfile('c:\\Windows\\System32\\notepad.exe')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'access notepad' in question:
                    SR.speak('Opening notepad')
                    os.startfile('c:\\Windows\\System32\\notepad.exe')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break


            elif there_exists1(['close notepad', 'deny notepad'
                                ], question):
                if 'close notepad' in question:
                    SR.speak(" Closing notepad")
                    os.system("taskkill /f /im notepad.exe")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'deny notepad' in question:
                    SR.speak(" Closing notepad")
                    os.system("taskkill /f /im notepad.exe")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(['close calculator', 'deny calculator'
                                ], question):
                if 'close calculator' in question:
                    SR.speak(" Closing calculator")
                    os.system("taskkill /f /im calc.exe'")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'deny calculator' in question:
                    SR.speak(" Closing calculator")
                    os.system("taskkill /f /im calc.exe'")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(['shut down', 'shut down my pc', 'shut this pc down', 'shut down the pc'
                                ], question):
                if 'shut down' in question:
                    SR.speak("Shut down your Pc")
                    os.system("shutdown /s /t 30")
                    break

                elif 'shut this pc down' in question:
                    SR.speak("Shut down your Pc")
                    os.system("shutdown /s /t 30")
                    break

                elif 'shut down my pc' in question:
                    SR.speak("Shut down your Pc")
                    os.system("shutdown /s /t 30")
                    break

                elif 'shut down the pc' in question:
                    SR.speak("Shut down your Pc")
                    os.system("shutdown /s /t 30")
                    break

            elif there_exists1(['restart', 'restart my pc', 'restart this pc down', 'restart the pc'
                                ], question):
                if 'restart' in question:
                    SR.speak("Restart your Pc")
                    os.system("shutdown /r /t 30")
                    break

                elif 'restart this pc down' in question:
                    SR.speak("Restart your Pc")
                    os.system("shutdown /r /t 30")
                    break

                elif 'restart my pc' in question:
                    SR.speak("Restart your Pc")
                    os.system("shutdown /r /t 30")
                    break

                elif 'restart the pc' in question:
                    SR.speak("Restart your Pc")
                    os.system("shutdown /r /t 30")
                    break

            elif there_exists1(['log out my pc', 'log out this pc down', 'log out the pc'
                                ], question):
                if 'log out my pc' in question:
                    SR.speak("Loging out")
                    os.system("shutdown /l")
                    break

                elif 'log out this pc down' in question:
                    SR.speak("Loging out")
                    os.system("shutdown /l")
                    break

                elif 'log out the pc' in question:
                    SR.speak("Loging out")
                    os.system("shutdown /l")
                    break

            elif there_exists1(['mute my pc', 'mute this pc ', 'mute the pc'
                                ], question):
                if 'mute my pc' in question:
                    SR.speak("Muting Sound")
                    pyautogui.hotkey('volumemute')
                    break
                elif 'mute this pc' in question:
                    SR.speak("Muting Sound")
                    pyautogui.hotkey('volumemute')
                    break
                elif 'mute the pc' in question:
                    SR.speak("Muting Sound")
                    pyautogui.hotkey('volumemute')
                    break

            elif there_exists1(
                    ['minimize my screen', 'minimize my window ', 'minimize', 'small screen', 'small my screen'
                     ], question):
                if 'minimize my screen' in question:
                    SR.speak("Minimizing Screen")
                    pyautogui.keyDown('winleft')
                    pyautogui.keyDown('down')
                    pyautogui.keyUp('winleft')
                    pyautogui.keyUp('down')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'minimize my window' in question:
                    SR.speak("Minimizing Screen")
                    pyautogui.keyDown('winleft')
                    pyautogui.keyDown('down')
                    pyautogui.keyUp('winleft')
                    pyautogui.keyUp('down')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'minimize' in question:
                    SR.speak("Minimizing Screen")
                    pyautogui.keyDown('winleft')
                    pyautogui.keyDown('down')
                    pyautogui.keyUp('winleft')
                    pyautogui.keyUp('down')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'small screen' in question:
                    SR.speak("Minimizing Screen")
                    pyautogui.keyDown('winleft')
                    pyautogui.keyDown('down')
                    pyautogui.keyUp('winleft')
                    pyautogui.keyUp('down')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'small my screen' in question:
                    SR.speak("Minimizing Screen")
                    pyautogui.keyDown('winleft')
                    pyautogui.keyDown('down')
                    pyautogui.keyUp('winleft')
                    pyautogui.keyUp('down')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(
                    ['maximize my screen', 'maximize my window ', 'maximize', 'big screen', 'big my screen'
                     ], question):
                if 'maximize my screen' in question:
                    SR.speak("Maximizing Screen")
                    pyautogui.keyDown('winleft')
                    pyautogui.keyDown('up')
                    pyautogui.keyUp('winleft')
                    pyautogui.keyUp('up')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'maximize my window' in question:
                    SR.speak("Maximizing Screen")
                    pyautogui.keyDown('winleft')
                    pyautogui.keyDown('up')
                    pyautogui.keyUp('winleft')
                    pyautogui.keyUp('up')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'maximize' in question:
                    SR.speak("Maximizing Screen")
                    pyautogui.keyDown('winleft')
                    pyautogui.keyDown('up')
                    pyautogui.keyUp('winleft')
                    pyautogui.keyUp('up')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'big screen' in question:
                    SR.speak("Maximizing Screen")
                    pyautogui.keyDown('winleft')
                    pyautogui.keyDown('up')
                    pyautogui.keyUp('winleft')
                    pyautogui.keyUp('up')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'big my screen' in question:
                    SR.speak("Maximizing Screen")
                    pyautogui.keyDown('winleft')
                    pyautogui.keyDown('up')
                    pyautogui.keyUp('winleft')
                    pyautogui.keyUp('up')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(
                    ['exit my screen', 'exit my window ', 'exit', 'exit screen', 'exit my screen'
                     ], question):
                if 'exit my screen' in question:
                    SR.speak("EXIT")
                    pyautogui.keyDown('altleft')
                    pyautogui.keyDown('f4')
                    pyautogui.keyUp('altleft')
                    pyautogui.keyUp('f4')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'exit my window' in question:
                    SR.speak("EXIT")
                    pyautogui.keyDown('altleft')
                    pyautogui.keyDown('f4')
                    pyautogui.keyUp('altleft')
                    pyautogui.keyUp('f4')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'exit' in question:
                    SR.speak("EXIT")
                    pyautogui.keyDown('altleft')
                    pyautogui.keyDown('f4')
                    pyautogui.keyUp('altleft')
                    pyautogui.keyUp('f4')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'exit screen' in question:
                    SR.speak("EXIT")
                    pyautogui.keyDown('altleft')
                    pyautogui.keyDown('f4')
                    pyautogui.keyUp('altleft')
                    pyautogui.keyUp('f4')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'exit my screen' in question:
                    SR.speak("EXIT")
                    pyautogui.keyDown('altleft')
                    pyautogui.keyDown('f4')
                    pyautogui.keyUp('altleft')
                    pyautogui.keyUp('f4')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(
                    ['back', 'go back', 'move back', 'moveback'
                     ], question):
                if 'back' in question:
                    SR.speak("Back")
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('left')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('left')
                    break
                elif 'go back' in question:
                    SR.speak("Back")
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('left')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('left')
                    break
                elif 'move back' in question:
                    SR.speak("Back")
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('left')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('left')
                    break
                elif 'moveback' in question:
                    SR.speak("Back")
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('left')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('left')
                    break

            elif there_exists1(
                    ['forward', 'go forward', 'move forward', 'moveforward'
                     ], question):
                if 'forward' in question:
                    SR.speak("Forward")
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('right')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('right')
                    break
                elif 'go forward' in question:
                    SR.speak("Forward")
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('right')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('right')
                    break
                elif 'move forward' in question:
                    SR.speak("Forward")
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('right')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('right')
                    break
                elif 'moveforward' in question:
                    SR.speak("Forward")
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('right')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('right')
                    break

            elif there_exists1(
                    ['search and open'
                     ], question):
                if 'search and open' in question:
                    question = question.replace("search and open", "")
                    SR.speak("Opening" + question)
                    pyautogui.hotkey('win', 'd')
                    pyautogui.press('win')
                    pyautogui.write(question)
                    pyautogui.press("enter")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(
                    ['go up', 'up'
                     ], question):
                if 'go up' in question:
                    SR.speak("Up")
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('up')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('up')
                    break
                elif 'up' in question:
                    SR.speak("Up")
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('up')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('up')
                    break
            elif there_exists1(['find location of', 'show location of', 'find location for', 'show location for'],
                               question):
                if 'of' in question:
                    url = 'https://google.nl/maps/place/' + question[question.find('of') + 3:] + '/&amp'
                    webbrowser.get(chrome_path).open(url)
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'for' in question:
                    url = 'https://google.nl/maps/place/' + question[question.find('for') + 4:] + '/&amp'
                    webbrowser.get(chrome_path).open(url)
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(['put alarm', 'set an alarm', 'set alarm', 'put an alarm'], question):
                if 'put alarm' in question:
                    question = question.replace("put alarm", "")
                    SR.speak('set alarm at ' + question)
                    SR.speak(question)
                    MyAlarm.alarm(question)
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'set an alarm' in question:
                    question = question.replace("set an alarm", "")
                    SR.speak('set alarm at ' + question)
                    SR.speak(question)
                    MyAlarm.alarm(question)
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'set alarm' in question:
                    question = question.replace("set alarm", "")
                    SR.speak('set alarm at ' + question)
                    SR.speak(question)
                    MyAlarm.alarm(question)
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'put an alarm' in question:
                    question = question.replace("put an alarm", "")
                    SR.speak('set alarm at ' + question)
                    SR.speak(question)
                    MyAlarm.alarm(question)
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break













            elif there_exists1(["show my location", "what is my location", "tell me my location",
                                "tell me my current location", "what is my current location"], question):
                if "show my location" in question:
                    SR.speak("Showing your location on google maps...")
                    url = "https://www.google.com/maps/search/Where+am+I+?/"
                    webbrowser.get().open(url)
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif "what is my location" in question:
                    SR.speak("Showing your location on google maps...")
                    url = "https://www.google.com/maps/search/Where+am+I+?/"
                    webbrowser.get().open(url)
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif "tell me my location" in question:
                    SR.speak("Showing your location on google maps...")
                    url = "https://www.google.com/maps/search/Where+am+I+?/"
                    webbrowser.get().open(url)
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif "tell me my current location" in question:
                    SR.speak("Showing your location on google maps...")
                    url = "https://www.google.com/maps/search/Where+am+I+?/"
                    webbrowser.get().open(url)
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif "what is my current location" in question:
                    SR.speak("Showing your location on google maps...")
                    url = "https://www.google.com/maps/search/Where+am+I+?/"
                    webbrowser.get().open(url)
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(["where am i", "where do i live", "where i live", 'tell me where am i'], question):
                if "where am i" in question:
                    Ip_info = requests.get(
                        'https://api.ipdata.co?api-key=aa4b921dc121bf96c60cb33e7e9dc05eef7e191206228b9e09c0bbc6').json()
                    region = Ip_info['region']
                    country = Ip_info['country_name']
                    latitude = Ip_info['latitude']
                    longitude = Ip_info['longitude']
                    postal = Ip_info['postal']
                    SR.speak(f"You must be somewhere in {region} in {country} with {latitude}"
                             f" as latitude and {longitude} as longitude and you postal code is {postal} ")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif "where do i live" in question:
                    Ip_info = requests.get(
                        'https://api.ipdata.co?api-key=aa4b921dc121bf96c60cb33e7e9dc05eef7e191206228b9e09c0bbc6').json()
                    region = Ip_info['region']
                    country = Ip_info['country_name']
                    latitude = Ip_info['latitude']
                    longitude = Ip_info['longitude']
                    postal = Ip_info['postal']
                    SR.speak(f"You must be somewhere in {region} in {country} with {latitude}"
                             f" as latitude and {longitude} as longitude and you postal code is {postal} ")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif "where i live" in question:
                    Ip_info = requests.get(
                        'https://api.ipdata.co?api-key=aa4b921dc121bf96c60cb33e7e9dc05eef7e191206228b9e09c0bbc6').json()
                    region = Ip_info['region']
                    country = Ip_info['country_name']
                    latitude = Ip_info['latitude']
                    longitude = Ip_info['longitude']
                    postal = Ip_info['postal']
                    SR.speak(f"You must be somewhere in {region} in {country} with {latitude}"
                             f" as latitude and {longitude} as longitude and you postal code is {postal} ")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif "tell me where am i" in question:
                    Ip_info = requests.get(
                        'https://api.ipdata.co?api-key=aa4b921dc121bf96c60cb33e7e9dc05eef7e191206228b9e09c0bbc6').json()
                    region = Ip_info['region']
                    country = Ip_info['country_name']
                    latitude = Ip_info['latitude']
                    longitude = Ip_info['longitude']
                    postal = Ip_info['postal']
                    SR.speak(f"You must be somewhere in {region} in {country} with {latitude}"
                             f" as latitude and {longitude} as longitude and you postal code is {postal} ")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break


            elif there_exists1(["tell me about my system", "tell me about my system condition", "system condition",
                                "tell me about my system situation", "system situation", "check the system condition",
                                "check my system condition", "check the system situation", "check my system condition"],
                               question):
                if 'tell me about my system' in question:
                    freq = str(psutil.cpu_freq())
                    times = str(psutil.cpu_times())
                    usage = str(psutil.cpu_percent())
                    disk = str(psutil.disk_usage('/'))
                    memory = str(psutil.virtual_memory())
                    SR.speak("CPU is at" + usage + " percentage \n" + freq +
                             "\n" + times + "\n" + disk + "\n" + memory)
                    mem = psutil.virtual_memory()
                    THRESHOLD = 100 * 1024 * 1024  # 100MB
                    if mem.available <= THRESHOLD:
                        SR.speak("Virtual memory is more then 100MB , warning , warning, warning")
                    else:
                        SR.speak("Virtual memory is less then 100MB , it is normal")
                    percentage_usage = psutil.cpu_percent()
                    if 1 <= percentage_usage <= 10:
                        SR.speak(f"Boss CPU usage is too normal")
                    elif 11 <= percentage_usage <= 20:
                        SR.speak(f"Boss CPU usage is  normal")
                    elif 21 <= percentage_usage <= 50:
                        SR.speak(f"Boss CPU usage is high ")
                    else:
                        SR.speak(f"Boss CPU usage is too high ")
                    battray = psutil.sensors_battery()
                    percentage = battray.percent
                    SR.speak(f"our system have {percentage} percentage Battery")
                    if percentage >= 75:
                        SR.speak(f"we could have enough charging to continue our work")
                    elif percentage >= 40 and percentage <= 75:
                        SR.speak(f" we should connect out system to charging point to charge our battery")
                    elif percentage >= 15 and percentage <= 30:
                        SR.speak(f" we don't have enough power to work, please connect to charging")
                    else:
                        SR.speak(
                            f" we have very low power, please connect to charging"
                            f" otherwise the system will shutdown very soon")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'tell me about my system condition' in question:
                    freq = str(psutil.cpu_freq())
                    times = str(psutil.cpu_times())
                    usage = str(psutil.cpu_percent())
                    disk = str(psutil.disk_usage('/'))
                    memory = str(psutil.virtual_memory())
                    SR.speak("CPU is at" + usage + " percentage \n" + freq +
                             "\n" + times + "\n" + disk + "\n" + memory)
                    mem = psutil.virtual_memory()
                    THRESHOLD = 100 * 1024 * 1024  # 100MB
                    if mem.available <= THRESHOLD:
                        SR.speak("Virtual memory is more then 100MB , warning , warning, warning")
                    else:
                        SR.speak("Virtual memory is less then 100MB , it is normal")
                    percentage_usage = psutil.cpu_percent()
                    if 1 <= percentage_usage <= 10:
                        SR.speak(f"Boss CPU usage is too normal")
                    elif 11 <= percentage_usage <= 20:
                        SR.speak(f"Boss CPU usage is  normal")
                    elif 21 <= percentage_usage <= 50:
                        SR.speak(f"Boss CPU usage is high ")
                    else:
                        SR.speak(f"Boss CPU usage is too high ")
                    battray = psutil.sensors_battery()
                    percentage = battray.percent
                    SR.speak(f"our system have {percentage} percentage Battery")
                    if percentage >= 75:
                        SR.speak(f"we could have enough charging to continue our work")
                    elif percentage >= 40 and percentage <= 75:
                        SR.speak(f" we should connect out system to charging point to charge our battery")
                    elif percentage >= 15 and percentage <= 30:
                        SR.speak(f" we don't have enough power to work, please connect to charging")
                    else:
                        SR.speak(
                            f" we have very low power, please connect to charging"
                            f" otherwise the system will shutdown very soon")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'system condition' in question:
                    freq = str(psutil.cpu_freq())
                    times = str(psutil.cpu_times())
                    usage = str(psutil.cpu_percent())
                    disk = str(psutil.disk_usage('/'))
                    memory = str(psutil.virtual_memory())
                    SR.speak("CPU is at" + usage + " percentage \n" + freq +
                             "\n" + times + "\n" + disk + "\n" + memory)
                    mem = psutil.virtual_memory()
                    THRESHOLD = 100 * 1024 * 1024  # 100MB
                    if mem.available <= THRESHOLD:
                        SR.speak("Virtual memory is more then 100MB , warning , warning, warning")
                    else:
                        SR.speak("Virtual memory is less then 100MB , it is normal")
                    percentage_usage = psutil.cpu_percent()
                    if 1 <= percentage_usage <= 10:
                        SR.speak(f"Boss CPU usage is too normal")
                    elif 11 <= percentage_usage <= 20:
                        SR.speak(f"Boss CPU usage is  normal")
                    elif 21 <= percentage_usage <= 50:
                        SR.speak(f"Boss CPU usage is high ")
                    else:
                        SR.speak(f"Boss CPU usage is too high ")
                    battray = psutil.sensors_battery()
                    percentage = battray.percent
                    SR.speak(f"our system have {percentage} percentage Battery")
                    if percentage >= 75:
                        SR.speak(f"we could have enough charging to continue our work")
                    elif percentage >= 40 and percentage <= 75:
                        SR.speak(f" we should connect out system to charging point to charge our battery")
                    elif percentage >= 15 and percentage <= 30:
                        SR.speak(f" we don't have enough power to work, please connect to charging")
                    else:
                        SR.speak(
                            f" we have very low power, please connect to charging"
                            f" otherwise the system will shutdown very soon")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'tell me about my system situation' in question:
                    freq = str(psutil.cpu_freq())
                    times = str(psutil.cpu_times())
                    usage = str(psutil.cpu_percent())
                    disk = str(psutil.disk_usage('/'))
                    memory = str(psutil.virtual_memory())
                    SR.speak("CPU is at" + usage + " percentage \n" + freq +
                             "\n" + times + "\n" + disk + "\n" + memory)
                    mem = psutil.virtual_memory()
                    THRESHOLD = 100 * 1024 * 1024  # 100MB
                    if mem.available <= THRESHOLD:
                        SR.speak("Virtual memory is more then 100MB , warning , warning, warning")
                    else:
                        SR.speak("Virtual memory is less then 100MB , it is normal")
                    percentage_usage = psutil.cpu_percent()
                    if 1 <= percentage_usage <= 10:
                        SR.speak(f"Boss CPU usage is too normal")
                    elif 11 <= percentage_usage <= 20:
                        SR.speak(f"Boss CPU usage is  normal")
                    elif 21 <= percentage_usage <= 50:
                        SR.speak(f"Boss CPU usage is high ")
                    else:
                        SR.speak(f"Boss CPU usage is too high ")
                    battray = psutil.sensors_battery()
                    percentage = battray.percent
                    SR.speak(f"our system have {percentage} percentage Battery")
                    if percentage >= 75:
                        SR.speak(f"we could have enough charging to continue our work")
                    elif percentage >= 40 and percentage <= 75:
                        SR.speak(f" we should connect out system to charging point to charge our battery")
                    elif percentage >= 15 and percentage <= 30:
                        SR.speak(f" we don't have enough power to work, please connect to charging")
                    else:
                        SR.speak(
                            f" we have very low power, please connect to charging"
                            f" otherwise the system will shutdown very soon")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'system situation' in question:
                    freq = str(psutil.cpu_freq())
                    times = str(psutil.cpu_times())
                    usage = str(psutil.cpu_percent())
                    disk = str(psutil.disk_usage('/'))
                    memory = str(psutil.virtual_memory())
                    SR.speak("CPU is at" + usage + " percentage \n" + freq +
                             "\n" + times + "\n" + disk + "\n" + memory)
                    mem = psutil.virtual_memory()
                    THRESHOLD = 100 * 1024 * 1024  # 100MB
                    if mem.available <= THRESHOLD:
                        SR.speak("Virtual memory is more then 100MB , warning , warning, warning")
                    else:
                        SR.speak("Virtual memory is less then 100MB , it is normal")
                    percentage_usage = psutil.cpu_percent()
                    if 1 <= percentage_usage <= 10:
                        SR.speak(f"Boss CPU usage is too normal")
                    elif 11 <= percentage_usage <= 20:
                        SR.speak(f"Boss CPU usage is  normal")
                    elif 21 <= percentage_usage <= 50:
                        SR.speak(f"Boss CPU usage is high ")
                    else:
                        SR.speak(f"Boss CPU usage is too high ")
                    battray = psutil.sensors_battery()
                    percentage = battray.percent
                    SR.speak(f"our system have {percentage} percentage Battery")
                    if percentage >= 75:
                        SR.speak(f"we could have enough charging to continue our work")
                    elif percentage >= 40 and percentage <= 75:
                        SR.speak(f" we should connect out system to charging point to charge our battery")
                    elif percentage >= 15 and percentage <= 30:
                        SR.speak(f" we don't have enough power to work, please connect to charging")
                    else:
                        SR.speak(
                            f" we have very low power, please connect to charging"
                            f" otherwise the system will shutdown very soon")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'check the system condition' in question:
                    freq = str(psutil.cpu_freq())
                    times = str(psutil.cpu_times())
                    usage = str(psutil.cpu_percent())
                    disk = str(psutil.disk_usage('/'))
                    memory = str(psutil.virtual_memory())
                    SR.speak("CPU is at" + usage + " percentage \n" + freq +
                             "\n" + times + "\n" + disk + "\n" + memory)
                    mem = psutil.virtual_memory()
                    THRESHOLD = 100 * 1024 * 1024  # 100MB
                    if mem.available <= THRESHOLD:
                        SR.speak("Virtual memory is more then 100MB , warning , warning, warning")
                    else:
                        SR.speak("Virtual memory is less then 100MB , it is normal")
                    percentage_usage = psutil.cpu_percent()
                    if 1 <= percentage_usage <= 10:
                        SR.speak(f"Boss CPU usage is too normal")
                    elif 11 <= percentage_usage <= 20:
                        SR.speak(f"Boss CPU usage is  normal")
                    elif 21 <= percentage_usage <= 50:
                        SR.speak(f"Boss CPU usage is high ")
                    else:
                        SR.speak(f"Boss CPU usage is too high ")
                    battray = psutil.sensors_battery()
                    percentage = battray.percent
                    SR.speak(f"our system have {percentage} percentage Battery")
                    if percentage >= 75:
                        SR.speak(f"we could have enough charging to continue our work")
                    elif percentage >= 40 and percentage <= 75:
                        SR.speak(f" we should connect out system to charging point to charge our battery")
                    elif percentage >= 15 and percentage <= 30:
                        SR.speak(f" we don't have enough power to work, please connect to charging")
                    else:
                        SR.speak(
                            f" we have very low power, please connect to charging"
                            f" otherwise the system will shutdown very soon")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'check the system situation' in question:
                    freq = str(psutil.cpu_freq())
                    times = str(psutil.cpu_times())
                    usage = str(psutil.cpu_percent())
                    disk = str(psutil.disk_usage('/'))
                    memory = str(psutil.virtual_memory())
                    SR.speak("CPU is at" + usage + " percentage \n" + freq +
                             "\n" + times + "\n" + disk + "\n" + memory)
                    mem = psutil.virtual_memory()
                    THRESHOLD = 100 * 1024 * 1024  # 100MB
                    if mem.available <= THRESHOLD:
                        SR.speak("Virtual memory is more then 100MB , warning , warning, warning")
                    else:
                        SR.speak("Virtual memory is less then 100MB , it is normal")
                    percentage_usage = psutil.cpu_percent()
                    if 1 <= percentage_usage <= 10:
                        SR.speak(f"Boss CPU usage is too normal")
                    elif 11 <= percentage_usage <= 20:
                        SR.speak(f"Boss CPU usage is  normal")
                    elif 21 <= percentage_usage <= 50:
                        SR.speak(f"Boss CPU usage is high ")
                    else:
                        SR.speak(f"Boss CPU usage is too high ")
                    battray = psutil.sensors_battery()
                    percentage = battray.percent
                    SR.speak(f"our system have {percentage} percentage Battery")
                    if percentage >= 75:
                        SR.speak(f"we could have enough charging to continue our work")
                    elif percentage >= 40 and percentage <= 75:
                        SR.speak(f" we should connect out system to charging point to charge our battery")
                    elif percentage >= 15 and percentage <= 30:
                        SR.speak(f" we don't have enough power to work, please connect to charging")
                    else:
                        SR.speak(
                            f" we have very low power, please connect to charging"
                            f" otherwise the system will shutdown very soon")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'check my system condition' in question:
                    freq = str(psutil.cpu_freq())
                    times = str(psutil.cpu_times())
                    usage = str(psutil.cpu_percent())
                    disk = str(psutil.disk_usage('/'))
                    memory = str(psutil.virtual_memory())
                    SR.speak("CPU is at" + usage + " percentage \n" + freq +
                             "\n" + times + "\n" + disk + "\n" + memory)
                    mem = psutil.virtual_memory()
                    THRESHOLD = 100 * 1024 * 1024  # 100MB
                    if mem.available <= THRESHOLD:
                        SR.speak("Virtual memory is more then 100MB , warning , warning, warning")
                    else:
                        SR.speak("Virtual memory is less then 100MB , it is normal")
                    percentage_usage = psutil.cpu_percent()
                    if 1 <= percentage_usage <= 10:
                        SR.speak(f"Boss CPU usage is too normal")
                    elif 11 <= percentage_usage <= 20:
                        SR.speak(f"Boss CPU usage is  normal")
                    elif 21 <= percentage_usage <= 50:
                        SR.speak(f"Boss CPU usage is high ")
                    else:
                        SR.speak(f"Boss CPU usage is too high ")
                    battray = psutil.sensors_battery()
                    percentage = battray.percent
                    SR.speak(f"our system have {percentage} percentage Battery")
                    if percentage >= 75:
                        SR.speak(f"we could have enough charging to continue our work")
                    elif percentage >= 40 and percentage <= 75:
                        SR.speak(f" we should connect out system to charging point to charge our battery")
                    elif percentage >= 15 and percentage <= 30:
                        SR.speak(f" we don't have enough power to work, please connect to charging")
                    else:
                        SR.speak(
                            f" we have very low power, please connect to charging"
                            f" otherwise the system will shutdown very soon")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(
                    ['pause', 'pause the song', 'pause the video', 'pause song', 'pause video',
                     'pause youtube'], question):
                if 'pause' in question:
                    SR.speak("pausing...")
                    pyautogui.hotkey('space')
                    break

                elif 'pause the song' in question:
                    SR.speak("pausing the song")
                    pyautogui.hotkey('space')
                    break

                elif 'pause the video' in question:
                    SR.speak("pausing the video")
                    pyautogui.hotkey('space')
                    break

                elif 'pause song' in question:
                    SR.speak("pausing the song")
                    pyautogui.hotkey('space')
                    break

                elif 'pause video' in question:
                    SR.speak("pausing the video")
                    pyautogui.hotkey('space')
                    break

                elif 'pause youtube' in question:
                    SR.speak("pausing youtube")
                    pyautogui.hotkey('space')
                    break

            elif there_exists1(['suggest to me a password', 'password suggestion',
                                'i want password', 'give me password'], question):
                if "suggest to me a password" in question:
                    SR.updating_ST("Your Password is : " + "".join(
                        random.sample(string.ascii_letters + string.digits + string.punctuation, 13)),
                                   )
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif "password suggestion" in question:
                    SR.updating_ST("Your Password is : " + "".join(
                        random.sample(string.ascii_letters + string.digits + string.punctuation, 13)),
                                   )
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif "i want password" in question:
                    SR.updating_ST("Your Password is : " + "".join(
                        random.sample(string.ascii_letters + string.digits + string.punctuation, 13)),
                                   )

                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif "give me password" in question:
                    SR.updating_ST("Your Password is : " + "".join(
                        random.sample(string.ascii_letters + string.digits + string.punctuation, 13)),
                                   )
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(['top news',
                                'listen some news', 'news of today', 'tell me news',
                                'news today', 'today news', 'tell me news of today'], question):
                if "top news" in question:
                    news = Annex.News(textarea)
                    news.show()
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif "listen some news" in question:
                    news = Annex.News(textarea)
                    news.show()
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif "news of today" in question:
                    news = Annex.News(textarea)
                    news.show()
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif "tell me news" in question:
                    news = Annex.News(textarea)
                    news.show()
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif "news today" in question:
                    news = Annex.News(textarea)
                    news.show()
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif "today news" in question:
                    news = Annex.News(textarea)
                    news.show()
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif "tell me news of today" in question:
                    news = Annex.News(textarea)
                    news.show()
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(
                    ['take a photo', 'take a selfie', 'take my photo', 'take photo', 'take selfie',
                     'one photo please',
                     'click a photo'], question):
                SR.speak("Show me my master beautiful Smile, Cheeeers.")
                takephoto = Annex.camera()
                Location = takephoto.takePhoto()
                os.startfile(Location)
                del takephoto
                SR.speak("Captured picture is stored in Camera folder.")
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

            elif there_exists1(['send some files through bluetooth', 'send file through bluetooth', 'bluetooth sharing',
                                'bluetooth file sharing', 'open bluetooth'], question):

                if 'send some files through bluetooth' in question:
                    SR.speak("Opening bluetooth...")
                    os.startfile(r"C:\Windows\System32\fsquirt.exe")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'open bluetooth' in question:
                    SR.speak("Opening bluetooth...")
                    os.startfile(r"C:\Windows\System32\fsquirt.exe")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'send file through bluetooth' in question:
                    SR.speak("Opening bluetooth...")
                    os.startfile(r"C:\Windows\System32\fsquirt.exe")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'bluetooth sharing' in question:
                    SR.speak("Opening bluetooth...")
                    os.startfile(r"C:\Windows\System32\fsquirt.exe")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'bluetooth file sharing' in question:
                    SR.speak("Opening bluetooth...")
                    os.startfile(r"C:\Windows\System32\fsquirt.exe")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

                elif 'open bluetooth' in question:
                    SR.speak("Opening bluetooth...")
                    os.startfile(r"C:\Windows\System32\fsquirt.exe")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(
                    ['make a note', 'take note', 'take a note', 'note it down', 'make note', 'remember this as note'
                     ], question):
                if "make a note" in question:
                    data = question.replace("make a note", '')
                    date = datetime.datetime.now()
                    filename = str(date).replace(':', '-') + '-note.txt'
                    a = os.getcwd()
                    if not os.path.exists('Notes'):
                        os.mkdir('Notes')
                    os.chdir(a + r'\Notes')
                    with open(filename, 'w') as f:
                        f.write(data)
                    subprocess.Popen(['notepad.exe', filename])
                    os.chdir(a)
                    SR.speak('note has created and saved in notes file!')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'take note' in question:
                    data = question.replace("take note", '')
                    date = datetime.datetime.now()
                    filename = str(date).replace(':', '-') + '-note.txt'
                    a = os.getcwd()
                    if not os.path.exists('Notes'):
                        os.mkdir('Notes')
                    os.chdir(a + r'\Notes')
                    with open(filename, 'w') as f:
                        f.write(data)
                    subprocess.Popen(['notepad.exe', filename])
                    os.chdir(a)
                    SR.speak('note has been created and saved in notes file!')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'take a note' in question:
                    data = question.replace("take a note", '')
                    date = datetime.datetime.now()
                    filename = str(date).replace(':', '-') + '-note.txt'
                    a = os.getcwd()
                    if not os.path.exists('Notes'):
                        os.mkdir('Notes')
                    os.chdir(a + r'\Notes')
                    with open(filename, 'w') as f:
                        f.write(data)
                    subprocess.Popen(['notepad.exe', filename])
                    os.chdir(a)
                    SR.speak('note has been created and saved in notes file!')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'note it down' in question:
                    data = question.replace("note it down", '')
                    date = datetime.datetime.now()
                    filename = str(date).replace(':', '-') + '-note.txt'
                    a = os.getcwd()
                    if not os.path.exists('Notes'):
                        os.mkdir('Notes')
                    os.chdir(a + r'\Notes')
                    with open(filename, 'w') as f:
                        f.write(data)
                    subprocess.Popen(['notepad.exe', filename])
                    os.chdir(a)
                    SR.speak('note has been created and saved in notes file!')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'make note' in question:
                    data = question.replace("make note", '')
                    date = datetime.datetime.now()
                    filename = str(date).replace(':', '-') + '-note.txt'
                    a = os.getcwd()
                    if not os.path.exists('Notes'):
                        os.mkdir('Notes')
                    os.chdir(a + r'\Notes')
                    with open(filename, 'w') as f:
                        f.write(data)
                    subprocess.Popen(['notepad.exe', filename])
                    os.chdir(a)
                    SR.speak('note has been created and saved in notes file!')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                elif 'remember this as note' in question:
                    data = question.replace("remember this as note", '')
                    date = datetime.datetime.now()
                    filename = str(date).replace(':', '-') + '-note.txt'
                    a = os.getcwd()
                    if not os.path.exists('Notes'):
                        os.mkdir('Notes')
                    os.chdir(a + r'\Notes')
                    with open(filename, 'w') as f:
                        f.write(data)
                    subprocess.Popen(['notepad.exe', filename])
                    os.chdir(a)
                    SR.speak('note has been created and saved in notes file!')
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break




            elif there_exists1(["toss a coin", "flip a coin", "toss"], question):
                moves = ["head", "tails"]
                cmove = random.choice(moves)
                SR.speak("It's " + cmove)
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

            elif there_exists1(['the time', 'tell me the time''tell the time'], question):
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                SR.speak(f"Sir, the time is {strTime}")
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

            elif there_exists1(['the date', 'tell me the date', 'tell the date'], question):
                strDay = datetime.date.today().strftime("%B %d, %Y")
                SR.speak(f"Today is {strDay}")
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

            elif there_exists1(['what day it is', 'what day is today', 'which day is today', "today's day name please"],
                               question):
                SR.speak(f"Today is {datetime.datetime.now().strftime('%A')}")
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

            elif there_exists1(['show me performance of my system', 'open performance monitor', 'performance monitor',
                                'performance of my computer', 'performance of this computer'], question):
                os.startfile("C:\Windows\System32\perfmon.exe")
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

            elif there_exists1(['open snipping tool', 'snipping tool', 'start snipping tool'], question):
                SR.speak("Opening snipping tool....")
                os.startfile("C:\Windows\System32\SnippingTool.exe")
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

            elif there_exists1(['open code', 'open visual studio ', 'open vs code'], question):
                SR.speak("Opeining vs code")
                codepath = r"C:\Users\Vishal\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                os.startfile(codepath)
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

            elif there_exists1(
                    ['open file manager', 'file manager', 'open my computer', 'my computer', 'open file explorer',
                     'file explorer', 'open this pc', 'this pc'], question):
                SR.speak("Opening File Explorer")
                os.startfile("C:\Windows\explorer.exe")
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

            elif there_exists1(['powershell'], question):
                SR.speak("Opening powershell")
                os.startfile(r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe')
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

            elif there_exists1(['cmd', 'command prompt', 'command prom', 'commandpromt', ], question):
                SR.speak("Opening command prompt")
                os.startfile(r'C:\Windows\System32\cmd.exe')
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

            elif there_exists1(['open settings', 'open control panel', 'open this computer setting Window',
                                'open computer setting Window', 'open computer settings', 'open setting',
                                'show me settings', 'open my computer settings'], question):
                SR.speak("Opening settings...")
                os.startfile('C:\Windows\System32\control.exe')
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

            elif there_exists1(
                    ['open your setting', 'open your settings', 'open settiing window', 'show me setting window',
                     'open voice assistant settings'], question):
                SR.speak("Opening my Setting window..")
                sett_wind = Annex.SettingWindow()
                sett_wind.settingWindow(root)
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

            elif there_exists1(['take screenshot', 'take a screenshot', 'screenshot please', 'capture my screen'],
                               question):
                SR.speak("Taking screenshot")
                SS = Annex.screenshot()
                SS.takeSS()
                SR.speak('Captured screenshot is saved in Screenshots folder.')
                del SS
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

            elif there_exists1(['record my voice', 'start voice recorder', 'voice recorder'], question):
                VR = Annex.VoiceRecorer()
                VR.Record(textarea)
                del VR
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

            elif there_exists1(['text to speech', 'convert my notes to voice'], question):
                SR.speak("Opening Text to Speech mode")
                TS = Annex.TextSpeech()
                del TS
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

            elif there_exists1(['weather report', 'temperature'], question):
                Weather = Annex.Weather()
                Weather.show(textarea)
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

            elif there_exists1(['none'], question):
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break
            elif there_exists1(['stop the flow', 'stop the execution', 'halt', 'halt the process', 'stop the process',
                                'stop listening', 'stop the listening'], question):
                SR.speak("Listening halted.")
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break
            elif there_exists1(['what is the capital of', 'capital of', 'capital city of'], question):
                try:
                    res = app.query(question)
                    SR.speak(next(res.results).text)
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                except:
                    print("Sorry, but there is a little problem while fetching the result.")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            elif there_exists1(['temperature'], question):
                try:
                    res = app.query(question)
                    SR.speak(next(res.results).text)
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                except:
                    print("Internet Connection Error")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
            elif there_exists1(
                    ['+', '-', '*', 'x', '/', 'plus', 'add', 'minus', 'subtract', 'divide', 'multiply', 'divided',
                     'multiplied'], question):
                try:
                    res = app.query(question)
                    SR.speak("the result is " + next(res.results).text)
                    if (uptimeMins >= 4 or uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break
                except:
                    print("Internet Connection Error")
                    if (uptimeHours >= 4 or uptimeWeeks >= 1):
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        winsound.PlaySound('abc', winsound.SND_LOOP)
                        SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                    break

            else:
                SR.speak("sorry,I don't know how to replay to that yet.")
                if (uptimeHours >= 4 or uptimeWeeks >= 1):
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    winsound.PlaySound('abc', winsound.SND_LOOP)
                    SR.speak("Take Rest Sir You Are Using Pc For Long Time!")

                break

    except Exception as e:
        pass


def Launching_thread():
    Thread_ID = gen(1000)
    global MainframeThread_object
    MainframeThread_object = MainframeThread(Thread_ID.__next__(), "Mainframe")
    MainframeThread_object.start()


if __name__ == "__main__":
    # tkinter code
    try:
        App = QApplication(sys.argv)
        trayIcon = QSystemTrayIcon(QIcon("Mic.png"), parent=App)
        trayIcon.setToolTip(' Alex')
        trayIcon.show()
        menu = QMenu()
        exitaction = menu.addAction('Exit')
        exitaction.triggered.connect(App.__exit__)
        trayIcon.setContextMenu(menu)

    except :
        pass
    root = themed_tk.ThemedTk()
    root.set_theme("winnative")
    root.geometry("{}x{}+{}+{}".format(745, 360, int(root.winfo_screenwidth() / 2 - 745 / 2),
                                       int(root.winfo_screenheight() / 2 - 360 / 2)))
    root.resizable(0, 0)
    root.title("Alex")
    root.iconbitmap('defaultFace4.ico')
    root.configure(bg='#2c4557')
    centerFrame = tk.Frame(root)
    centerFrame.pack()

    scrollbar = tk.Scrollbar(centerFrame)
    scrollbar.pack(side=RIGHT)

    textarea = tk.Text(centerFrame, font=('times new roman', 12, 'bold'), width=360, height=14,
                       yscrollcommand=scrollbar.set
                       , wrap='word', bg='#800080')
    textarea.pack(side=LEFT)
    scrollbar.config(command=textarea.yview)
    mic_img = Image.open("Mic.png")
    mic_img = mic_img.resize((55, 55), Image.ANTIALIAS)
    mic_img = ImageTk.PhotoImage(mic_img)
    Speak_label = tk.Label(root, text="SPEAK:", fg="#FFD700", font='"Times New Roman" 12 ', borderwidth=0, bg='#2c4557')
    Speak_label.place(x=100, y=300)
    """Setting up objects"""
    SR = Annex.SpeakRecog(textarea)  # Speak and Recognition class instance
    Listen_Button = tk.Button(root, image=mic_img, borderwidth=0, activebackground='#2c4557', bg='#2c4557',
                              command=Launching_thread)
    Listen_Button.place(x=180, y=280)
    myMenu = tk.Menu(root)
    Ask_label = tk.Label(root, text="ASK:", fg="#FFD700", font='"Times New Roman" 12 ', borderwidth=0, bg='#2c4557')
    Ask_label.place(x=240, y=300)
    Askpic = Image.open("ASB.png")
    Askpic = Askpic.resize((55, 55), Image.ANTIALIAS)
    Askpic = ImageTk.PhotoImage(Askpic)

    qf = Entry(root, font='"Times New Roman" 12 ', width=30, )
    qf.place(x=300, y=300)

    Ask_Button = tk.Button(root, image=Askpic, borderwidth=0, activebackground='#2c4557', bg='#2c4557',
                           command=botReply)
    Ask_Button.place(x=570, y=280)

    m1 = tk.Menu(myMenu, tearoff=0)  # tearoff=0 means the submenu can't be teared of from the window
    m1.add_command(label='Commands List', command=CommandsList)
    myMenu.add_cascade(label="Help", menu=m1)
    stng_win = Annex.SettingWindow()
    myMenu.add_cascade(label="Settings", command=partial(stng_win.settingWindow, root))
    myMenu.add_cascade(label="Clear Screen", command=clearScreen)

    root.config(menu=myMenu)

    root.mainloop()
