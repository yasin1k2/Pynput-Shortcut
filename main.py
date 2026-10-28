# imports and global variables
from pynput import keyboard
import os


# actions
def show_message():
    print("This is the shortcut to write this message")

def list_folder():
    os.startfile(".")


# shortcuts
shortcuts = {'<ctrl>+<alt>+m' : show_message, '<ctrl>+<alt>+s' : list_folder}


with keyboard.GlobalHotKeys(shortcuts) as listener :
    listener.join()