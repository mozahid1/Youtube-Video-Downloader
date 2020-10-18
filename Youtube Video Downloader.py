from pytube import YouTube
import os
from tkinter import *

root=Tk()
# Create Output Background Size
root.geometry('330x200')
root.title('Youtube Video Downloader')

# Create First Output Line
Label1=Label(root,text="Youtube Video Link", font=("bold",20))
Label1.place(x=43,y=20)

# Create Second Output Line
Label2=Label(root, text="Developed By: Md.Mozahidul Islam",width=35, font=("bold",10))
Label2.place(x=25,y=160)

link=StringVar()

# Create Youtube Link Paste Option
paste_link=Entry(root, width=50, textvariable=link)
paste_link.place(x=10, y=60)

# Download Condition
def Download():
    x=str(link.get())
    ytvideo=YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists('./Videos'):
        os.makedirs('./Videos')
    ytvideo.download('./Videos')

# Create a button
Button(root,text="Download", width=20, bg='red',fg="white",font="bold",command=Download).place(x=70, y=100)

root.mainloop()
