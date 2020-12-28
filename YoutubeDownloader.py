import tkinter as tk
from pytube import YouTube
def downloadVideo():
	global e1
	s=e1.get()
	y=YouTube(str(s))
	videos=y.streams.all()
	c=1
	for v in videos:
		print(str(c)+'.'+str(v))
		c+=1
	n=int(input('Enter your Choice:'))
	video=videos[n-1]
	destination=input('Enter Destination Folder:')
	video.download(str(destination))
	print(y.title+'....'+'has been downloaded')
	root.destroy()

root=tk.Tk()
root.geometry("300x150")
w=tk.Label(root,text='YOUTUBE DOWNLOADER')
w.pack()

e1=tk.Entry(root,bd=5)
e1.pack(side=tk.TOP)


b=tk.Button(root,text='Download',fg="black",command=downloadVideo) 
b.pack(side=tk.BOTTOM)

root.mainloop()