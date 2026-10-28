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
shortcuts = {'<ctrl>+<alt>+m' : show_message, '<ctrl>+<alt>+s' : list_folder, '<ctrl>+s' : quit_app}


with keyboard.GlobalHotKeys(shortcuts) as listener :
    listener.join()