import tkinter as tk
import random
import time

root = tk.Tk()
root.title("EYE BLINKER")


def start_game():
    global start_time
    button.config(state=tk.DISABLED)
    random_time = random.randint(3,9)
    root.after(random_time * 1000,change_to_green)

def change_to_green():
    global start_time
    button.config(bg='green',state=tk.NORMAL)
    start_time = time.time()

def on_button_click():
    global start_time
    if start_time:
        reaction_time = time.time() - start_time
        last_reaction_time = f'Reaction time : {reaction_time:.2f} seconds'
        label.config(text=last_reaction_time)
        button.config(bg='red',state=tk.DISABLED)
        root.after(1000,start_game)


root.geometry("900x700")

 
button = tk.Button(root,text='Text your reaction time',bg='red',command=on_button_click,width=60,height=20)
button.pack()

last_reaction_time = "Last reaction time : N/A"

label = tk.Button(root,text=last_reaction_time)
label.pack()

start_time = None

root.after(1000,start_game)

root.mainloop()