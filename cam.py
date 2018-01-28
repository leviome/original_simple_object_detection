# coding:utf-8
import cv2
import sys
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(1, 10.0)
#此处fourcc的在MAC上有效，如果视频保存为空，那么可以改一下这个参数试试, 也可以是-1
fourcc = cv2.CV_FOURCC('m', 'p', '4', 'v')
# 第三个参数则是镜头快慢的，10为正常，小于10为慢镜头
out = cv2.VideoWriter('output2.avi', fourcc,10,(640,480))
cap.release()
out.release()

