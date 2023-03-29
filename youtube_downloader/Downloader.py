from tkinter import *
from tkinter import messagebox, filedialog
from pytube import YouTube


def show_info_dialog(message):
    messagebox.showinfo('Information', message)


def download_video():
    try:
        # validate url
        url = link.get()
        if not url:
            show_info_dialog('Please enter a valid YouTube URL')
            return

        # validate path
        path = path_var.get()
        if not path:
            show_info_dialog('Please select a download location')
            return

        # get selected quality
        selected_quality = quality.get()
        video = YouTube(url)

        # filter out progressive streams (they have both audio and video)
        # only get streams that include audio and video
        streams = video.streams.filter(progressive=False)

        # filter streams based on selected quality
        if selected_quality == '1080p':
            streams = streams.filter(resolution='1080p')
        elif selected_quality == '720p':
            streams = streams.filter(resolution='720p')
        elif selected_quality == '480p':
            streams = streams.filter(resolution='480p')
        elif selected_quality == '360p':
            streams = streams.filter(resolution='360p')
        elif selected_quality == '240p':
            streams = streams.filter(resolution='240p')
        elif selected_quality == '144p':
            streams = streams.filter(resolution='144p')

        # get the first stream
        stream = streams.first()
        stream.download(output_path=path)

        show_info_dialog('Video downloaded successfully!')

    except Exception as e:
        show_info_dialog(f'Error: {e}')


def select_path():
    path = filedialog.askdirectory()
    if path:
        path_var.set(path)


root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title('YouTube Downloader')

# URL label and entry
Label(root, text='YouTube URL', font='Arial 12 bold').place(x=30, y=20)
link = StringVar()
Entry(root, width=50, textvariable=link).place(x=150, y=20)

# Quality label and options
Label(root, text='Quality', font='Arial 12 bold').place(x=30, y=60)
quality = StringVar(value='720p')
quality_options = ['144p', '240p', '360p', '480p', '720p', '1080p']
OptionMenu(root, quality, *quality_options).place(x=150, y=60)

# Path label, entry and button
Label(root, text='Save to', font='Arial 12 bold').place(x=30, y=100)
path_var = StringVar()
path_entry = Entry(root, width=50, textvariable=path_var)
path_entry.place(x=150, y=100)
path_button = Button(root, text='Select Folder', font='Arial 10', command=select_path)
path_button.place(x=350, y=130)

# Download button
Button(root, text='Download', font='Arial 12 bold', bg='pale violet red', padx=2, command=download_video).place(x=200, y=150)

root.mainloop()