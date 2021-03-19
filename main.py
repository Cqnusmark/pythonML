# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#一个界面框
# from tkinter import *
# def print_hi(name):
#      #Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#     top = Tk()
#     top.mainloop()
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



#一个界面框
# from kivy.app import App
# from kivy.uix.button import Button
#
# class TestApp(App):
#     def build(self):
#         return Button(text ="Hello, kivy")
#
# TestApp().run()

#识别照相机中的脸部和眼睛
# from cv2 import *
# import numpy as np
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# if face_cascade.empty():
#     raise IOError("Unable to load the face cascade classifier xml file")
# if eye_cascade.empty():
#     raise IOError("Unable to load the eye cascade classifier xml file")
#
# cap = cv2.VideoCapture(0)
#
# scaling_factor = 0.5
#
# while True:
#     ret, frame = cap.read()
#
#     frame = cv2.resize(frame, None, fx=scaling_factor, fy= scaling_factor, interpolation = cv2.INTER_AREA)
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
#
#     for(x, y, w, h) in face_rects:
#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = frame[y:y+h, x:x+w]
#         eye_rects = eye_cascade.detectMultiScale(roi_gray)
#
#         for(x_eye, y_eye, w_eye, h_eye) in eye_rects:
#             center = (int(x_eye+0.5*w_eye), int(y_eye+0.5*h_eye))
#             radius = int(0.3 * (w_eye+h_eye))
#             color = (0,100,0)
#             thickness = 3
#             cv2.circle(roi_color, center, radius, color, thickness)
#
#         # cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),3)
#     cv2.imshow("Face Detector", frame)
#
#     c = cv2.waitKey(1)
#     if c==27:
#         break
# cap.release()
# cv2.destroyAllWindows()


#识别图片中的脸
# import cv2
# filename = 'img3.jpg'
#
# def detect(filename):
#     face_cascade1 = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
#     img = cv2.imread(filename)
#
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade1.detectMultiScale(gray,1.3,5)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
#
#     cv2.namedWindow("people")
#     cv2.imshow("people",img)
#     cv2.imwrite('cxks.png',img)
#     cv2.waitKey(0)
#
# detect(filename)


