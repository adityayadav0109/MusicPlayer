from tkinter import *
from pygame import mixer
from tkinter.filedialog import askopenfilename
import os
from mutagen.mp3 import MP3
import tkinter.messagebox as tkmsg
from tkinter.ttk import Progressbar
import time
import threading
from tkinter import ttk

root = Tk()
root.geometry("700x700")
root.title('MusicPlayer - by Aditya')
root.wm_iconbitmap('logo.ico')
mixer.init()

song_data_list = []

def open_file():
    global status_val
    global song
    global song_name
    song = askopenfilename()
    status_val.set('Loaded New File')
    #defaultextension = '.mp3', filetypes =[("All Files", "*.*"), ("Music Documents", "*.mp3")]


pause = False
def pause_music():
    global status_val
    global Paused
    Paused = TRUE
    pause = True
    mixer.music.pause()
    status_val.set('Paused')


def pause_music_btn(event):
    global status_val
    global Paused
    Paused = TRUE
    mixer.music.pause()
    status_val.set('Paused')


root.bind('<space>', pause_music_btn)



# def music_details():
#     if pause is False:
#         file = MP3(song)
#         total_length = int(file.info.length)
#         min,sec = divmod(total_length, 60)
#         full_info = '{:02d}:{:02d}'.format(min,sec)
#         detail.set(full_info)
#         while total_length >= 1 and pause is False:
#             total_length -= 1
#             time.sleep(1)
#             min, sec = divmod(total_length, 60)
#             full_info = '{:02d}:{:02d}'.format(min, sec)
#             detail.set(full_info)
#             show_details = Label(root, textvariable=detail, font="calibri 15 bold").update()
#
#     else:
#         pass
#
# def length_increase(Tl):
#     current_len = mixer.music.get_pos()//1000
#     while current_len<=Tl:
#         song_length['value'] = current_len




def play_music():
    global status_val
    global Paused
    global song
    global song_name

    # print

    try:
        # Paused
        selected_song = list.curselection()
        index = selected_song[0]
        song = song_data_list[index]
        mixer.music.load(song)

        mixer.music.play()



    except:
        mixer.music.load(song)
        mixer.music.play()
        status_val.set('Playing')


    else:
        mixer.music.unpause()
        status_val.set('Playing')

    # t = threading.Thread(target=music_details)
    # t.start()
    # music_details()
    song_name.set('Playing - ' + str(os.path.basename(song)))
    # print('Playing - ' + os.path.basename(music_file))
    file = MP3(song)
    total_length = int(file.info.length)
    # song_length['maximum']= total_length
    # t1 = threading.Thread(target=length_increase, args=total_length)
    # t1.start()



def play_music_btn(event):
    global status_val
    global Paused
    global song
    try:
        Paused

    except:
        mixer.music.load(song)
        mixer.music.play()
        status_val.set('Playing')


    else:
        mixer.music.unpause()
        status_val.set('Playing')

    song_name.set('Playing - ' + str(os.path.basename(song)))
root.bind('<Return>', play_music_btn)



def vol(val):
    mixer.music.set_volume(int(val)/100)



def help_me():
    tkmsg.showinfo("Help Center", "You can add your ofline music file and play in this music player"
                                  "\nYou can add several files in Playlist\nPress 'Space' button to "
                                  "Pause and 'Enter' button to resume it...\n\nThankYou")


def about():
    tkmsg.showinfo('About Us', 'This music player is developed by Aditya Yadav')

def contact():
    tkmsg.showinfo("Contact Center", "You can contact us on adityayadav1743@gmail.com\n\nThankYou")


def mute():
    mixer.music.set_volume(0.0)
    status_val.set('Muted')


def unmute():
    vol('30')
    status_val.set('Playing')


def replay():
    mixer.music.pause()
    mixer.music.load(song)
    mixer.music.play()
    status_val.set('Replayed')


# def length(val):
#     current_pos = mixer.music.get_pos()//1000
#     song_length[val]=current_pos



def add_to_list():
    n = 1
    song = askopenfilename()
    song_data_list.insert(n, song)
    song = os.path.basename(song)
    list.insert(n, song)

    n += 1


def exit_app():
    response = tkmsg.askyesno("Exit - Music Player", "Do you want to exit ?")
    if response is True:
        root.destroy()

    else:
        pass



menubar = Menu(root, fg = "white", bg = 'blue')
filemenu = Menu(menubar)
filemenu.add_command(label = 'Open', command = open_file)
filemenu.add_command(label = 'Exit', command = exit_app)

menubar.add_cascade(label = 'File', menu = filemenu)

help_menu = Menu(menubar)
help_menu.add_command(label = "Help", command = help_me)
help_menu.add_command(label = "About Us", command = about)
help_menu.add_command(label = "Contact Us", command = contact)

menubar.add_cascade(label = 'Help', menu = help_menu)


root.config(menu = menubar,  background = 'gray')


song_name = StringVar()
song_name.set('WELCOME')



name = Label(root, textvariable = song_name, font = "lucida 14 bold", pady = 20, bg = 'gray', fg = 'white')
name.pack()

# detail = StringVar()
# detail.set('00:00')
# show_details = Label(root, textvariable = detail, font = "calibri 15 bold").pack()


add_btn = Button(root, fg = 'blue', bg = 'white', command = open_file, text = "+", font = 'lucida 20 bold', padx = 15)
add_btn.pack(pady = 20)


pause_photo = PhotoImage(file='pause.png')
play_photo = PhotoImage(file='resume.png')
replay_photo = PhotoImage(file = 'bckwrd.png')
mute_photo = PhotoImage(file = 'mute.png')
unmute_photo = PhotoImage(file = 'unmute.png')

f1 = Frame(root, bg = 'gray')
f1.pack(pady = 20)


mute_btn = Button(f1, image = mute_photo, bg = 'grey', fg = 'black', command = mute, padx = 10)
mute_btn.pack(side = LEFT, padx = 20)


play_btn = Button(f1, image = play_photo, command = play_music, padx = 10, bg = 'grey')
play_btn.pack(side = LEFT, padx = 20)


replay_btn = Button(f1, image = replay_photo, command = replay, bg = 'grey')
replay_btn.pack(side = LEFT, padx = 20)

pause_btn = Button(f1, image = pause_photo, command = pause_music, padx = 10, bg = 'grey')
pause_btn.pack(side = LEFT, padx = 20)


unmute_btn = Button(f1, image = unmute_photo, bg = 'grey', fg = 'black', command = unmute, padx = 10)
unmute_btn.pack(side = LEFT, padx = 20)


vol_scale = Scale(root, from_ =0, to=100, command = vol, orient = HORIZONTAL, bg = 'grey')
vol_scale.set(30)
vol_scale.pack(pady = 20)



# song_length = Progressbar(root, orient = HORIZONTAL, value = 0).pack(fill = X)

Button(root, text = "ADD TO PLAYLIST", fg = "white", bg = "red", command = add_to_list, padx = 5, pady = 5, font = "calibri 10 bold").pack(pady = 20)

list = Listbox(root, bg = "grey26", fg = 'white', justify = "center", borderwidth = 5, relief = SUNKEN)
list.pack(fill = BOTH, padx = 10, pady = 20)

statusbar = Frame(root, bg = 'cyan', borderwidth = 2, relief = SUNKEN)
statusbar.pack(fill = X, side = BOTTOM)

status_val = StringVar()
status_val.set('Ready...')

status = Label(statusbar, bg = 'cyan', fg = 'black', textvariable = status_val, font = "calibri 10 bold")
status.pack(side = LEFT)

caption = Label(statusbar, text = 'MusicPlayer - by Aditya', bg = 'cyan', fg = 'black', font = "calibri 10 bold")
caption.pack(side = RIGHT)

root.mainloop()