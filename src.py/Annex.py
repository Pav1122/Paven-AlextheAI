import datetime, subprocess, os, pyautogui, string, random, time
from tkinter.ttk import Entry

import psutil

import MyAlarm

import Heisenberg
from Heisenberg import Launching_thread
import pyttsx3
import speech_recognition as sr
import sounddevice, pywhatkit
from scipy.io.wavfile import write
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import pyperclip, cv2, playsound, requests, json
from playsound import playsound
from ttkthemes import themed_tk as tkth
import tkinter.scrolledtext as textarea
from functools import partial
import tkinter.messagebox as tmsg, sqlite3



class SpeakRecog:
    def __init__(self, textarea):
        self.textarea = textarea

    # database connection
    conn = sqlite3.connect('Heisenberg.db')
    mycursor = conn.cursor()
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', mycursor.execute('select rate from speech_rate').fetchone()[
        0])  # setting up new voice rate in words per minute

    """VOLUME"""
    volume = engine.getProperty('volume')
    engine.setProperty('volume', (
    mycursor.execute('select vol from volume').fetchone()[0]) / 10)  # setting up volume level  between 0 and 1
    conn.commit()
    conn.close()
    textarea = None

    def STS(self, textarea):
        self.textarea = textarea

    def updating_ST(self, data):
        self.textarea.configure(state='normal')
        self.textarea.insert('end', data + '\n')
        self.textarea.configure(state='disabled')
        self.textarea.see('end')
        self.textarea.update()

    def updating_ST_No_newline(self, data):
        self.textarea.configure(state='normal')
        self.textarea.insert('end', data)
        self.textarea.configure(state='disabled')
        self.textarea.see('end')
        self.textarea.update()

    def scrollable_text_clearing(self):
        self.textarea.configure(state='normal')
        self.textarea.delete(1.0, 'end')
        self.textarea.configure(state='disabled')
        self.textarea.update()

    def speak(self, audio):
        self.updating_ST(audio)
        self.engine.say(audio)
        self.engine.runAndWait()
        # engine.stop()

    def nonPrintSpeak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def takeCommand(self):
        recog = sr.Recognizer()
        # mic=Microphone()
        with sr.Microphone() as source:
            # r.adjust_for_ambient_noise(source)
            self.updating_ST("\nListening...")
            recog.pause_threshold = 1
            # r.energy_threshold = 45.131829621150224
            # print(sr.Microphone.list_microphone_names())
            # print(r.energy_threshold)
            audio = recog.listen(source)

        try:
            self.updating_ST("Recognizing...")
            query = recog.recognize_google(audio)
            self.updating_ST(f"You: {query}\n")


        except Exception as e:
            self.updating_ST("Say that again please...")
            return 'None'
        return query
class PasswordGenerator:
    def action(self, pswd):
        pyperclip.copy(pswd)



    def showpswd(self, data, pswd):
        root = tk.Toplevel()
        root.title("Password Generator")
        root.iconbitmap('PasswordGenerator.ico')
        style = ttk.Style()
        style.configure('W.TButton', font=('calibri', 10, 'bold'), foreground='purple', borderwidth='4',
                        background="pink")
        root.geometry("320x80+540+270")
        label1 = ttk.Label(root, text=data, font=("comicsansms", 9, 'bold')).pack()
        button1 = ttk.Button(root, text='Copy to clipboard', style='W.TButton',
                             command=partial(self.action, pswd)).pack(pady=20)
        root.resizable(0, 0)
        root.mainloop()
        del root
        pass


    def givePSWD(self, textarea):
        SR = SpeakRecog(textarea)
        SR.speak("What type of password you want?")
        SR.updating_ST("\nPassword Level we have:-\n\nPoor Level\nAverage Level\nStrong Level\n")
        while (True):
            query = SR.takeCommand().lower()
            if ('poor' in query):
                self.showpswd("Your Password is : " + "".join(random.sample(string.ascii_letters, 7)),
                              "".join(random.sample(string.ascii_letters, 7)))

                pass
            elif ('average' in query):
                self.showpswd("Your Password is : " + "".join(random.sample(string.ascii_letters + string.digits, 10)),
                              "".join(random.sample(string.ascii_letters + string.digits, 10)))
                pass
            elif ('strong' in query):
                self.showpswd("Your Password is : " + "".join(
                    random.sample(string.ascii_letters + string.digits + string.punctuation, 13)),
                              "".join(random.sample(string.ascii_letters + string.digits + string.punctuation, 13)))
                pass
            else:
                SR.speak("Please say it again")
                pass
        del SR




class TextSpeech:
    def txtspk(self):
        SR = SpeakRecog(None)
        SR.nonPrintSpeak(self.text.get(1.0, tk.END))
        del SR

    def opentxt(self):
        self.root.focus_force()
        try:
            file_path = filedialog.askopenfilename(
                initialdir=r"C:\Users\Vishal\Documents\Projects or important programs\jarvis\Notes",
                title="Select file", filetypes=(('text file', "*.txt"), ("All files", "*.*")))
            with open(file_path, 'r') as f:
                g = f.read()

            self.root.focus_force()
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.INSERT, g)
            self.text.update()
            SR = SpeakRecog(None)
            SR.nonPrintSpeak(g)
            del SR
        except FileNotFoundError as e:
            self.root.focus_force()
            pass

    def __init__(self):
        self.root = tkth.ThemedTk()
        self.root.get_themes()
        self.root.set_theme("radiance")
        self.root.resizable(0, 0)
        self.root.configure(background='white')
        self.root.title("Text to Speech")
        self.root.iconbitmap('text_to_speech.ico')
        # root widget
        self.text = textarea.textarea(self.root, width=30, height=10, wrap=tk.WORD, padx=10, pady=10,
                                              borderwidth=5, relief=tk.RIDGE)
        self.text.grid(row=0, columnspan=3)
        # buttons
        self.listen_btn = ttk.Button(self.root, text="Listen", width=7, command=self.txtspk).grid(row=2, column=0,
                                                                                                  ipadx=2)
        self.clear_btn = ttk.Button(self.root, text="Clear", width=7,
                                    command=lambda: self.text.delete(1.0, tk.END)).grid(row=2, column=1, ipadx=2)
        self.open_btn = ttk.Button(self.root, text="Open", width=7, command=self.opentxt).grid(row=2, column=2, ipadx=2)
        self.root.focus_set()
        self.root.mainloop()


class note:
    def Note(self, data):
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


class screenshot:
    def takeSS(self):
        img_captured = pyautogui.screenshot()
        a = os.getcwd()
        if not os.path.exists("Screenshots"):
            os.mkdir("Screenshots")
        os.chdir(a + '\Screenshots')
        ImageName = 'screenshot-' + str(datetime.datetime.now()).replace(':', '-') + '.png'
        img_captured.save(ImageName)
        os.startfile(ImageName)
        os.chdir(a)




class SettingWindow:
    def Apply(self):
        # Database connection
        conn = sqlite3.connect('Heisenberg.db')
        mycursor = conn.cursor()
        Speech_Rate = self.speech_rate_text_box.get()
        if not (Speech_Rate.isdigit()):
            tmsg.showinfo("Error.", f"Please enter integers.")
            self.setting.focus_force()
        else:
            mycursor.execute('update speech_rate set rate=?', (int(Speech_Rate),))
            value = int((self.volume_slider.get()))
            mycursor.execute('update volume set vol=?', (value,))
            conn.commit()
            conn.close()
            # print(f"{value} type is {type(value)}")
            tmsg.showinfo("Point to be noted.", f"Setting will be applied after reboot of this program.")
            self.setting.destroy()

    def settingWindow(self, root):
        # database connection
        conn = sqlite3.connect('Heisenberg.db')
        mycursor = conn.cursor()
        self.setting = tk.Toplevel(root)
        canvas = tk.Canvas(self.setting)
        canvas.create_line(0, 135, 285, 135)
        canvas.create_line(0, 138, 285, 138)
        canvas.pack()
        self.setting.title("Settings")
        self.setting.iconbitmap('setting.ico')
        self.setting.geometry("285x180+500+200")
        self.setting.resizable(0, 0)
        self.volume = ttk.Label(self.setting, text="Alex's Volume: ", borderwidth=0,
                                font=('"Times New Roman"')).place(x=3, y=17)
        self.volume = ttk.Label(self.setting, text='Speech Rate[WPM]:', borderwidth=0,
                                font=('"Times New Roman"')).place(x=3, y=77)
        self.volume_slider = tk.Scale(self.setting, from_=0, to=10, orient=tk.HORIZONTAL)
        Integer_class = tk.IntVar(self.setting, value=mycursor.execute('select rate from speech_rate').fetchone()[0])
        self.speech_rate_text_box = ttk.Entry(self.setting, textvariable=Integer_class)
        self.volume_slider.place(x=137, y=0)
        self.speech_rate_text_box.place(x=140, y=77)
        self.volume_slider.set((mycursor.execute('select vol from volume').fetchone()[0]))
        conn.commit()
        conn.close()
        qf = Entry(root, font='"Times New Roman" 12 ')
        qf.pack()
        self.Apply_Button = ttk.Button(self.setting, text="Apply", command=self.Apply).place(x=200, y=150)
        self.setting.mainloop()


class camera:
    def takePhoto(self):
        self.video = cv2.VideoCapture(0)
        self.result = True
        a = os.getcwd()
        if not os.path.exists("Camera"):
            os.mkdir("Camera")
        os.chdir(a + '\Camera')
        self.ImageName = "Image-" + str(datetime.datetime.now()).replace(':', '-') + ".jpg"
        while (self.result):
            self.ret, self.frame = self.video.read()
            cv2.imwrite(self.ImageName, self.frame)
            self.result = False
        self.video.release()
        cv2.destroyAllWindows()

        os.chdir(a)
        playsound.playsound("camera-shutter-click.mp3")
        return "Camera\\" + self.ImageName
        pass




class VoiceRecorer:
    def Record(self, textarea):
        SR = SpeakRecog(textarea)
        SR.speak("This recording is of 10 seconds.")
        fs = 44100
        second = 10
        SR.updating_ST("Recording.....")
        record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
        sounddevice.wait()
        a = os.getcwd()
        if not os.path.exists("Recordings"):
            os.mkdir("Recordings")
        os.chdir(a + '\Recordings')
        write("Recording-" + str(datetime.datetime.now()).replace(':', '-') + ".wav", fs, record_voice)
        SR.speak("Voice is recorded in \'Recordings\' folder.")
        os.chdir(a)
        del SR

class Alarm:
    def __init__(self, textarea):
        self.SR = SpeakRecog(textarea)

    def alarm1(self):

        self.SR.speak("can you please tell me the time of alarm sir!")
        TT = self.SR.takeCommand()
        TT = TT.replace('','')
        TT = TT.replace(".","")
        TT =TT.upper()
        self.SR.speak(TT)

        while(True):
            try:
                MyAlarm.alarm(TT)
                continue
            except:
                pass









class News:
    def __init__(self, textarea):
        self.SR = SpeakRecog(textarea)

    def show(self):
        self.SR.speak("Showing top  news of today.")
        self.SR.scrollable_text_clearing()
        self.SR.updating_ST("-----------------------------Top  news of all categories.----------------------------")
        r = requests.get('http://newsapi.org/v2/top-headlines?country=in&apiKey=43f50ba4f6154700af10a1efcae42a51')
        data = json.loads(r.content)
        for i in range(10):
            self.SR.updating_ST_No_newline(f'News {i + 1}:  ')
            self.SR.speak(data['articles'][i]['title'] + '\n')


class WhatsApp:
    def __init__(self, textarea):
        self.SR = SpeakRecog(textarea)

    def send(self):
        self.SR.speak("Please tell me the mobile number whom do you want to send message to?")
        mobile_number = None
        while (True):
            mobile_number = self.SR.takeCommand().replace(' ', '')
            if mobile_number[0] == '0':
                mobile_number = mobile_number[1:]
            if not mobile_number.isdigit() or len(mobile_number) != 9:
                self.SR.speak("Please say it again")
            else:
                break
        mobile_number.replace(' ', '')
        self.SR.speak("Tell me your message......")
        message = self.SR.takeCommand()
        self.SR.speak("Opening whatsapp web to send your message.")
        self.SR.speak("Please be patient, sometimes it takes time.")
        while (True):
            try:
                pywhatkit.sendwhatmsg("+60" + mobile_number, message, datetime.datetime.now().hour,
                                      datetime.datetime.now().minute + 1)
                break
            except Exception:
                pass
        time.sleep(20)
        self.SR.speak('Message sent successfully.')


class Weather:
    def show(self, textarea):
        SR = SpeakRecog(textarea)
        base_url = "http://api.openweathermap.org/data/2.5/weather?id=524901&appid=07e3b193491c9849bed54809a1831b01"

        data = requests.get(base_url).json()
        SR.scrollable_text_clearing()
        SR.speak("-----------------------------Weather Report of Your City------------------------------")

        SR.speak("Temperature:   " + str(int(data['main']['temp'])) + ' Fahrenheit\n' +
                       "Wind Speed:    " + str(data['wind']['speed']) + ' m/s\n' +
                       "Latitude:      " + str(data['coord']['lat']) +
                       "\nLongitude:     " + str(data['coord']['lon']) +
                       "\nDescription:   " + str(data['weather'][0]['description']) + '\n')


class restart:
    def rest(self, textarea):
        SR = SpeakRecog(textarea)
        SR.speak("do you really want to restart your pc ?")
        SR.updating_ST("1:yes \n 2:no")
        while (True):
            query = SR.takeCommand().lower()
            if ('yes' in query):
                os.system("shutdown /r /t 30")
                break
            elif ('no' in query):
                pass
            else:
                SR.speak("Please say it again")
                pass
        del SR

class shutdown:
    def shut(self, textarea):
        SR = SpeakRecog(textarea)
        SR.speak("do you really want to shutdown your pc ?")
        SR.updating_ST("1:yes \n 2:no")
        while (True):
            query = SR.takeCommand().lower()
            if ('yes' in query):
                os.system("shutdown /s /t 30")
                break
            elif ('no' in query):
                pass
            else:
                SR.speak("Please say it again")
                pass
        del SR


class logout:
    def log(self, textarea):
        SR = SpeakRecog(textarea)
        SR.speak("do you really want to logout your pc ?")
        SR.updating_ST("1:yes \n 2:no")
        while (True):
            query = SR.takeCommand().lower()
            if ('yes' in query):
                os.system("shutdown /l")

                break
            elif ('no' in query):
                pass
            else:
                SR.speak("Please say it again")
                pass
        del SR