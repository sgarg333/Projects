# USAGE
# python photo_booth.py --output output

# import the necessary packages
from __future__ import print_function
from pyimagesearch.photoboothapp import PhotoBoothApp
from imutils.video import VideoStream
import argparse
import time
import numpy as np
import cv2
import urllib

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
	help="path to output directory to store snapshots")
ap.add_argument("-p", "--picamera", type=int, default=-1,
	help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())

# initialize the video stream and allow the camera sensor to warmup
print("[INFO] warming up camera...")
print(cv2.__version__)
url='http://192.168.23.2:8080/shot.jpg'

# while True:
#     imgResp=urllib.urlopen(url)
#     imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
#     img=cv2.imdecode(imgNp,-1)

#     # all the opencv processing is done here
#     vs=cv2.imshow('test',img)
#     if ord('q')==cv2.waitKey(10):
#         exit(0)
vs = VideoStream(src=1,usePiCamera=args["picamera"] > 0,resolution=(3264,2448)).start() # 2592 , 1920   	7680x4320    3840x2160
time.sleep(2.0)

# start the app
pba = PhotoBoothApp(vs, args["output"])
pba.root.mainloop()
