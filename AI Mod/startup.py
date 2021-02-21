import gsm
import configparser
import win32gui, win32con
from multiprocessing import Process
import time
import keyboard 
import sys


def start_game():
    cp = configparser.RawConfigParser()
    cp.read("./account.config")

    username = cp.get("mojang","username")
    password = cp.get("mojang","password")

    gs = gsm.GameSeshManager(username,password)

    gs.start()

def fullscreen():
    window = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(window, win32con.SW_MAXIMIZE)

def kb_monitor(e):
    #log keyboard input
    print(e.name)

keyboard.on_press(callback=kb_monitor) #todo -find where this belongs, ex when it should start monitoring

if __name__ == "__main__":
    p1 = Process(target=start_game)
    p2 = Process(target=fullscreen)
    p1.start()
    time.sleep(10)
    p2.start()
   
    