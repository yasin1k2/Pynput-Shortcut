# imports and global variables
from pynput import keyboard
import os


# actions
def show_message():
    print("This is the shortcut to write this message")

def list_folder():
    os.startfile(".")

def quit_app():
    print("Exiting program...")
    listener.stop()


# shortcuts
shortcuts = {'<esc>+1+s' : show_message, '<esc>+2+s' : list_folder, '<esc>+3+s' : quit_app}


with keyboard.GlobalHotKeys(shortcuts) as listener :
    listener.join()