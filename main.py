from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from time import time, ctime
from kivy.clock import Clock

def refresh(self):
    global timevar
    global timervar
    global timeforalarm
    text1 = str(ctime(time()))
    if timerstarted and timervar != 0:
        timervar -= 1
    if stopwatchstarted:
        timevar += 1
    text2 = 'Stopwatch: ' + str(timevar) + ' seconds'
    text3 = 'Timer: ' + str(timervar) + ' seconds'
    display.text = (text1 + '\n' + text2 + '\n' + text3)

def start(self):
    global stopwatchstarted
    stopwatchstarted = True

def stop(self):
    global stopwatchstarted
    stopwatchstarted = False

def reset(self):
    global timevar
    global stopwatchstarted
    stopwatchstarted = False
    timevar = 0

def startt(self):
    try:
        global timervar
        global timerstarted
        timervar = int(timerinput.text)
        timerstarted = True
    except:
        pass

def stopt(self):
    global timerstarted
    timerstarted = False

def resett(self):
    global timervar
    global timerstarted
    timervar = 0
    timerstarted = False

class Window(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global display
        global timerinput
        display = Label()   
        l1 = Label(text = 'stopwatch controls') 
        l2 = Label(text = "timer controls")
        pb1 = Button(text = "start", size_hint = (0.5, 0.5))
        pb2 = Button(text = "stop", size_hint = (0.5, 0.5))
        pb3 = Button(text = "reset", size_hint = (0.5, 0.5))
        pb4 = Button(text = "start", size_hint = (0.5, 0.5))
        pb5 = Button(text = "stop", size_hint = (0.5, 0.5))
        pb6 = Button(text = "reset", size_hint = (0.5, 0.5))
        l3 = Label(text = "Enter seconds:", size_hint = (0.5, 0.3))
        timerinput = TextInput(multiline = False, size_hint = (0.5, 0.3))
        lv1 = BoxLayout(orientation = "vertical")
        lh1 = BoxLayout(orientation = "horizontal")
        lh2 = BoxLayout(orientation = "horizontal")
        lh3 = BoxLayout(orientation = "horizontal")
        lh4 = BoxLayout(orientation = "horizontal")
        lh1.add_widget(pb1)
        lh1.add_widget(pb2)
        lh1.add_widget(pb3)
        lh2.add_widget(pb4)
        lh2.add_widget(pb5)
        lh2.add_widget(pb6)
        lh3.add_widget(display)
        lv1.add_widget(l1)
        lv1.add_widget(lh1)
        lv1.add_widget(l2)
        lv1.add_widget(lh2)
        lh4.add_widget(l3)
        lh4.add_widget(timerinput)
        lv1.add_widget(lh4)
        lh3.add_widget(lv1)
        display.text = text1 + '\n' + text2 + '\n' + text3
        pb1.bind(on_press = start)
        pb2.bind(on_press = stop)
        pb3.bind(on_press = reset)
        pb4.bind(on_press = startt)
        pb5.bind(on_press = stopt)
        pb6.bind(on_press = resett)
        Clock.schedule_interval(refresh, 1)
        self.add_widget(lh3)


class Watch(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(Window())
        return manager

timevar = 0
timervar = 0
timeforalarm = None
timerstarted = False
stopwatchstarted = False
text1 = str(ctime(time()))
text2 = 'Stopwatch: ' + str(timevar) + ' seconds'
text3 = 'Timer: ' + str(timervar) + ' seconds'
app = Watch()
app.run()