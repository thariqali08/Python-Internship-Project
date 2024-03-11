import tkinter as tk
import os
from pygame import mixer
import fnmatch

#intitialize  pygame
mixer.init()


def play_music():
    label.config(text=listSong.get("anchor"))
    mixer.music.load(rootpath + "\\" + listSong.get("anchor"))
    mixer.music.play()


paused=False
def pause_music():
     global paused
     if paused :
       mixer.music.unpause() #resume the song
       paused = False
    
     else:
      mixer.music.pause() #pause the song
      paused=True
    
def prev_music():
    next_song=listSong.curselection()
    next_song=next_song[0]-1
    next_song_name=listSong.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath+"\\"+next_song_name)
    mixer.music.play()

    listSong.select_clear(0,'end')
    listSong.activate(next_song)
    listSong.select_set(next_song)

def forw_music():
    next_song=listSong.curselection()
    next_song=next_song[0]+1
    next_song_name=listSong.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath+"\\"+next_song_name)
    mixer.music.play()

    listSong.select_clear(0,'end')
    listSong.activate(next_song)
    listSong.select_set(next_song)

def adjust_volume(vol):
    mixer.music.set_volume(float(vol))
    

#create a main window 
root = tk.Tk()
root.title("MUSIC PLAYER")
root.geometry("600x600")
root.config(bg="white")

#create music file rootpath
rootpath="C:\\Users\HI\Desktop\MUSIC" 
pattern = "*.mp3"

#create a list song window
listSong=tk.Listbox(root,fg="blue",bg="black",width=100,height=10,font=(15))
listSong.pack(padx=5,pady=10)

for rot,dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listSong.insert('end',filename)

#Show current song play
label = tk.Label(root,text='',fg="brown",bg="white",font=(20))
label.pack(pady=15)
vol_label=tk.Label(root,text="Volume",bg="white",fg="black",font=(23))
vol_label.pack()

volume_scale = tk.Scale(root, from_=0, to=1, resolution=0.1, orient="horizontal", command=adjust_volume)
volume_scale.set(0.5)
volume_scale.pack(pady=10)

#insert image button 
prev_img=tk.PhotoImage(file='prev_button.png')
forw_img=tk.PhotoImage(file='forw_button.png')
play_img=tk.PhotoImage(file='play_button.png')
pause_img=tk.PhotoImage(file='pause_button.png')

#create control frame button
control_frame=tk.Frame(root,bg="white")
control_frame.pack(padx=10,pady=5,anchor='center')

#create a music buttons
prv_btn=tk.Button(control_frame,image=prev_img,borderwidth=0,command=prev_music)
prv_btn.pack(padx=10,in_=control_frame,side="left")
pause_btn=tk.Button(control_frame,image=pause_img,borderwidth=0,command=pause_music)
pause_btn.pack(padx=10,in_=control_frame,side="left")
play_btn=tk.Button(control_frame,image=play_img,borderwidth=0,command=play_music)
play_btn.pack(padx=10,in_=control_frame,side="left")
forw_btn=tk.Button(control_frame,image=forw_img,borderwidth=0,command=forw_music)
forw_btn.pack(padx=10,in_=control_frame,side="left")
#vol_btn=tk.Button(control_frame,text="Volume",bg="black")
root.mainloop()