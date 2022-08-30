# import the necessary packages
from __future__ import print_function
from PIL import Image
from PIL import ImageTk

import tkinter as tki
#from Tkinter import *
from tkinter import Entry
from tkinter import Label
from tkinter import PhotoImage

import threading
import datetime
import imutils
import cv2
import os


class PhotoBoothApp:
	global i
	def __init__(self, vs, outputPath):
		# store the video stream object and output path, then initialize
		# the most recently read frame, thread for reading frames, and
		# the thread stop event
		self.vs = vs
		self.outputPath = outputPath
		self.frame = None
		self.thread = None
		self.stopEvent = None

		# initialize the root window and image panel
		self.root = tki.Tk()
		self.panel = None

		# create a button, that when pressed, will take the current
		# frame and save it to file
		btn = tki.Button(self.root, text="Capture!",
			command=self.takeSnapshot).grid(row=4, column=8, sticky='nsew',columnspan=2, rowspan=1, padx=5, pady=5)
		#btn.pack(side="bottom", fill="both", expand="no", padx=10,pady=10)
		#labels and textField(Entry)
		label=Label(self.root,text="ID").grid(row=1, column=8, sticky ='w' ,padx=5, pady=5)
		#label.pack(side="top",padx=10,pady=10)


		self.entry = Entry(self.root) #width=10
		#self.entry.pack(side="top",padx=10,pady=10)
		self.entry.focus_set()
		self.entry.grid(row=1, column=9, sticky ='w', padx=5, pady=5)

		label1=Label(self.root,text="Initialise number").grid(row=2, column=8, sticky= 'w',padx=5, pady=5)
		#label1.pack(side="top",padx=10,pady=10)

		self.initialize = tki.StringVar()
		self.entry1 = Entry(self.root,textvariable=self.initialize).grid(row=2, column=9, sticky='w',padx=5, pady=5)
		#self.entry1.pack(side="top",padx=10,pady=10)

		global i
		i=1
		self.initialize.set(i)
		#self.entry1.insert(0,i)
		#unique=entry.get()
		# print(unique)
		# Label(self.root, text="1. Left").pack(side="bottom")
		# Label(self.root, text="2. Right").pack(side="bottom")
		# Label(self.root, text="3. Up").pack(side="bottom")
		# Label(self.root, text="4. Down").pack(side="bottom")
		# Label(self.root, text="5. Front").pack(side="bottom")
		# #Label(self.root, text="Last Name").grid(row=1)
		self.b1=tki.Button(self.root)
		#self.image1 = Image.open("deep.jpg")
		self.photo1 = ImageTk.PhotoImage(file="deep.jpg")
		self.b1.config(image=self.photo1)
		#self.b.image=self.photo1

		#photo1 = tki.PhotoImage(file="deep.jpg")
		self.b1.grid(row=13,column=0,columnspan=2,rowspan=2,padx=5,pady=5)
		Label(self.root,text="Normal").grid(row=15,column=0,columnspan=2,rowspan=1,padx=5,pady=5)
		
		self.b2=tki.Button(self.root)
		self.photo2 = ImageTk.PhotoImage(file="2.jpg")
		self.b2.config(image=self.photo2)
		self.b2.grid(row=13,column=3,columnspan=2,rowspan=2,padx=5,pady=5)

		Label(self.root,text="Upward").grid(row=15,column=3,columnspan=2,rowspan=1,padx=5,pady=5)
		
		self.b3=tki.Button(self.root)
		self.photo3 = ImageTk.PhotoImage(file="3.jpg")
		self.b3.config(image=self.photo3)
		self.b3.grid(row=13,column=6,columnspan=2,rowspan=2,padx=5,pady=5)

		Label(self.root,text="Downward").grid(row=15,column=6,columnspan=2,rowspan=1,padx=5,pady=5)

		self.b4=tki.Button(self.root)
		self.photo4 = ImageTk.PhotoImage(file="4.jpg")
		self.b4.config(image=self.photo4)
		self.b4.grid(row=13,column=9,columnspan=2,rowspan=2,padx=5,pady=5)

		Label(self.root,text="Left").grid(row=15,column=9,columnspan=2,rowspan=1,padx=5,pady=5)

		self.b5=tki.Button(self.root)
		self.photo5 = ImageTk.PhotoImage(file="1.jpg")
		self.b5.config(image=self.photo5)
		self.b5.grid(row=13,column=12,columnspan=2,rowspan=2,padx=5,pady=5)

		Label(self.root,text="Right").grid(row=15,column=12,columnspan=2,rowspan=1,padx=5,pady=5)


		self.b6=tki.Button(self.root)
		self.photo6 = ImageTk.PhotoImage(file="0.jpg")
		self.b6.config(image=self.photo6)
		self.b6.grid(row=13,column=15,columnspan=2,rowspan=2,padx=5,pady=5)

		Label(self.root,text="Occlusion").grid(row=15,column=15,columnspan=2,rowspan=1,padx=5,pady=5)
		# start a thread that constantly pools the video sensor for
		# the most recently read frame
		self.stopEvent = threading.Event()
		self.thread = threading.Thread(target=self.videoLoop, args=())
		self.thread.start()

		# set a callback to handle when the window is closed
		self.root.wm_title("PhotoBooth")
		self.root.minsize(width=666 , height=500)
		self.root.wm_protocol("WM_DELETE_WINDOW", self.onClose)


	def videoLoop(self):
		# DISCLAIMER:
		# I'm not a GUI developer, nor do I even pretend to be. This
		# try/except statement is a pretty ugly hack to get around
		# a RunTime error that Tkinter throws due to threading
		try:
			# keep looping over frames until we are instructed to stop
			while not self.stopEvent.is_set():
				# grab the frame from the video stream and resize it to
				# have a maximum width of 300 pixels
				self.frame = self.vs.read()
				self.frame = imutils.resize(self.frame, width=400)
				#imgResp=urllib.urlopen(url)
    			#imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    			#img=cv2.imdecode(imgNp,-1)
				# OpenCV represents images in BGR order; however PIL
				# represents images in RGB order, so we need to swap
				# the channels, then convert to PIL and ImageTk format
				image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
				image = Image.fromarray(image)
				image = ImageTk.PhotoImage(image)
		
				# if the panel is not None, we need to initialize it
				if self.panel is None:
					self.panel = tki.Label(image=image)
					self.panel.image = image
					#self.panel.pack(side="left", padx=10, pady=10)
					self.panel.grid(row=0, column=0, columnspan=7, rowspan=7, padx=10, pady=10)
		
				# otherwise, simply update the panel
				else:
					self.panel.configure(image=image)
					self.panel.image = image

		except RuntimeError:
			print("[INFO] caught a RuntimeError")

	def takeSnapshot(self):
		# grab the current timestamp and use it to construct the
		# output path
		uniquee=self.entry.get()
		print(uniquee)
		print(cv2.__version__)

		global i
		i=self.initialize.get()
		i=int(i)
		print(i)
		
		if os.path.exists(os.path.expanduser(uniquee)):
			print("Already exists")
		# 	if os.listdir(raw_input(uniquee)):
		# 		print("not empty")
		# 	else:
		# 		print("empty")
			filename = uniquee + "-" + str(i)+".jpg"
			i=i+1
			#self.initialize.set(i)
			#self.entry1.delete(0,END)
			#self.entry1.insert(0,str(i))
			#filename = uniquee + "-" +"%s.jpg" %(i+1)
		else:
			os.mkdir(os.path.expanduser(uniquee))
			i=1

			filename = uniquee + "-" + str(i)+".jpg"
			i=i+1
		#ts = datetime.datetime.now()
		#filename = uniquee + "-" + str(i)+".jpg"
		#filename = uniquee+"-"+str(i)+"-"+"{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
		#if filename.exists():
		self.initialize.set(i)
		p = os.path.sep.join((uniquee,filename))
		g = os.path.sep.join((self.outputPath,filename))
		# save the file

		cv2.imwrite(p, self.frame.copy())
		cv2.imwrite(g, self.frame.copy())
		print("[INFO] saved {}".format(filename))

	def onClose(self):
		# set the stop event, cleanup the camera, and allow the rest of
		# the quit process to continue
		print("[INFO] closing...")
		self.stopEvent.set()
		self.vs.stop()
		self.root.quit()
