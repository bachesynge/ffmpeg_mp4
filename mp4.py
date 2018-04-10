import cv2
import os

img_idr = ''
v_dir = ''
fps = 15
num =110
img_size = (360, 640)

fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
videoWriter = cv2.VideoWriter(video_dir, fourcc, fps, img_size)

for i in range(1,num):
    im_name = os.path.join(im_dir, str(i).zfill(6)+'.jpg')
    frame = cv2.imread(im_name)
    videoWriter.write(frame)
    print im_name

#videoWriter.release()
