from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_name = ""

def openLocation():
    global Folder_name
    Folder_name = filedialog.askdirectory()
    if (len(Folder_name) > 1):
       location_error.config(text=Folder_name,fg="green")

    else: 
        location_error.config(text="Please choose folder",fg="red")

#Downloading the video

def Download():
    choice = video_choices.get()
    url = ytd_entry.get()

    if (len(url)>1):
        ytd_error.config(text="")
        yt = YouTube(url)

        if (choice == choices[0]):
            select = yt.streams.get_highest_resolution()

        elif (choice == choices[1]):
            select = yt.streams.get_lowest_resolution()

        elif (choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()
        else:
            ytd_error.config(text = "Paste link again!", fg ="red")

    #download function
    select.download(Folder_name)
    ytd_error.config(text="Download complete!")




root = Tk()
root.title("Youtube Downloader")
root.geometry("450x500")
root.columnconfigure(0,weight=1) # set all content in the center

#Downloader Link Label

ytdLabel = Label(root, text="Enter URL of the the video", font=("Arial Black",15))
ytdLabel.grid()

# url entry
ytd_entry_var = StringVar
ytd_entry = Entry(root,width=50, textvariable=ytd_entry_var)
ytd_entry.grid()

#Error msg

ytd_error = Label(root,text="Error", fg="red", font=("Arial Black",10))
ytd_error.grid()

#Path selection label

save_label= Label(root,text="Save the video file", fg="black", font=("Arial Black",15, "bold"))
save_label.grid()

# Path selection button

save_entry = Button(root,width=20, bg="grey",text="Choose file location", fg="white", font=("Arial Black",10), command=openLocation)
save_entry.grid()

#Error msg of location
location_error = Label(root,text="Error, path not selected", fg="red", font=("Arial Black",10))
location_error.grid()

#Download quality

quality = Label(root,text="Select Quality", fg="red", font=("Arial Black",10))

choices = ["720p","144p", "Audio"]
video_choices = ttk.Combobox(root, values=choices)
video_choices.grid()

#Download button

download_button = Button(root, text= "Download",width=10,bg="red",fg="white", command=Download)
download_button.grid()
root.mainloop()