import tkinter as tk
import fnmatch
import os
from pygame import mixer
from tkinter import filedialog
import shutil

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("500x500")
canvas.config(bg='black')

rootpath = "Songs"
pattern = "*.mp3"

mixer.init()

prev_img = tk.PhotoImage(file = "icons/prev_img.png")
next_img = tk.PhotoImage(file = "icons/next_img.png")
play_img = tk.PhotoImage(file = "icons/play_img.png")
pause_img = tk.PhotoImage(file = "icons/pause_img.png")
stop_img = tk.PhotoImage(file = "icons/stop_img.png")

def add_song():
    song = filedialog.askopenfilename(initialdir="/",title="Choose a Song",filetypes=(("mp3 Files",pattern),))
    shutil.move(song,rootpath)
    listBox.delete(0,"end")
    for root, dirs, files in os.walk(rootpath):
        for filename in fnmatch.filter(files, pattern):
            listBox.insert("end", filename)

def select():
    label.config(text = listBox.get("anchor"))
    mixer.music.load(rootpath+"//"+listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0]+1
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath + "//" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0,"end")
    listBox.activate(next_song)
    listBox.select_set(next_song)

def play_prev():
    prev_song = listBox.curselection()
    prev_song = prev_song[0] - 1
    prev_song_name = listBox.get(prev_song)
    label.config(text=prev_song_name)

    mixer.music.load(rootpath + "//" + prev_song_name)
    mixer.music.play()

    listBox.select_clear(0, "end")
    listBox.activate(prev_song)
    listBox.select_set(prev_song)

def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"]="Play"
        # pauseButton["image"]=play_img
    else:
        mixer.music.unpause()
        pauseButton["text"]= "Pause"
        # pauseButton["image"]=pause_img

add_songs_button = tk.Button(canvas,text="Add Songs",bg='black',font = ("poppins",14),fg='cyan',command=add_song)
add_songs_button.pack(pady=20,padx=20)

listBox = tk.Listbox(canvas,fg="cyan",bg='black',width=200,font = ("poppins",14))
listBox.pack(padx=15,pady=15)

label = tk.Label(canvas,text="",bg='black',fg="yellow",font = ("poppins",14))
label.pack(pady=15)

top = tk.Frame(canvas,bg="black")
top.pack(padx=10,pady=5,anchor='center')

prevButton = tk.Button(canvas,text="Prev",image=prev_img,bg='black',borderwidth=0,command=play_prev)
prevButton.pack(pady=15,in_=top,side='left')

stopButton = tk.Button(canvas,text="Stop",image=stop_img,bg='black',borderwidth=0,command=stop)
stopButton.pack(pady=15,in_=top,side='left')

playButton = tk.Button(canvas,text="Play",image=play_img,bg='black',borderwidth=0,command=select)
playButton.pack(pady=15,in_=top,side='left')

pauseButton = tk.Button(canvas,text="Pause",image=pause_img,bg='black',borderwidth=0,command=pause_song)
pauseButton.pack(pady=15,in_=top,side='left')

nextButton = tk.Button(canvas,text="Next",image=next_img,bg='black',borderwidth=0,command=play_next)
nextButton.pack(pady=15,in_=top,side='left')

for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listBox.insert("end",filename)

canvas.mainloop()
