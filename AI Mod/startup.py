import gsm
import configparser
import win32gui, win32con
from multiprocessing import Process
import time

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
    

if __name__ == "__main__":
    p1 = Process(target=start_game)
    p2 = Process(target=fullscreen)
    p1.start()
    time.sleep(10)
    p2.start()
   
    