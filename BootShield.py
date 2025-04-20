import tkinter as tk
from tkinter import messagebox
import time
import os
import keyboard
import sys

PASSWORD = "secondpass" 
WAIT_TIME = 100  

def check_password():
    recorded_keys = []
    start_time = time.time()
    
    root = tk.Tk()
    root.withdraw()

    while time.time() - start_time < WAIT_TIME:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            print(recorded_keys)
            recorded_keys.append(event.name)
            if "".join(recorded_keys[-len(PASSWORD):]) == PASSWORD:
                messagebox.showinfo("Success", "Boot Gaurd disabled !")
                sys.exit(0)
    

    messagebox.showerror("Warning", "timeout reached, turning off...")
    os.system("shutdown /s /t 1")

if __name__ == "__main__":
    check_password()