from tkinter import *
from PIL import Image,ImageTk
import cv2
import keyboard


prev_char=-1
cur_char=-1
cap = cv2.VideoCapture(-1)
#video_capture = cv2.VideoCapture(0)
font1=cv2.FONT_HERSHEY_SIMPLEX
font2=cv2.FONT_HERSHEY_DUPLEX
#/////////////////////////////////////////////////////////////////////

face_cascade = cv2.CascadeClassifier('faces.xml')
eye_cascade = cv2.CascadeClassifier('eye.xml')
smile_cascade = cv2.CascadeClassifier('smile.xml')
nose_cascade=cv2.CascadeClassifier('nose.xml')
mouth_cascade=cv2.CascadeClassifier('mouth.xml')
hd_cascade= cv2.CascadeClassifier('headshoulder.xml')

#/////////////////////////////////////////////////////////////////////

def FACE(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    cv2.putText(frame,'face detection system is activated',(50,20),font2,1,(0,0,100),1)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)
        cv2.putText(frame,'face detector',(185,460),font1,1,(0,0,0),2)
    return frame

def HAIR(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    cv2.putText(frame,'Hair detection system is activated',(50,20),font2,1,(0,0,100),1)
    for (x, y, w, h) in faces:
        #cv2.rectangle(frame,(x,y),(x+w,y+h-250),(255,0,0),3)
        cv2.putText(frame,'Hair',(x,y),font1,1,(0,255,0),2)
        cv2.putText(frame,'Hair detector',(185,460),font1,1,(0,0,0),2)
    return frame


def EYES(gray,frame):
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 10)
    cv2.putText(frame,'Eyes detection system is activated',(50,20),font2,1,(0,0,100),1)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 5)
        cv2.putText(frame,'Eyes detector',(185,460),font1,1,(0,0,0),2)
    return frame
   
def EYEBROWS(gray,frame):
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 10)
    cv2.putText(frame,'Eyebrows detection system is activated',(50,20),font2,1,(0,0,100),1)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(frame, (ex, ey-15), (ex+ew+10, ey+eh-40), (0, 255, 0), 5)
        cv2.putText(frame,'EyeBrow detector',(180,460),font1,1,(0,0,0),2)
    return frame

def CHEEK(gray,frame):
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    cv2.putText(frame,'Cheek detection system is activated',(50,20),font2,1,(0,0,100),1)
    for (ex, ey, ew, eh) in eyes:
        cv2.circle(frame,(ex+25,ey+60),(20),(255,0,0),3)
        cv2.putText(frame,'Cheek detector',(185,460),font1,1,(0,0,0),2)
    return frame
        
def SMILE(gray,frame):
    smiles = smile_cascade.detectMultiScale(gray, 1.7, 50)
    cv2.putText(frame,'Smile detection system is activated',(50,20),font2,1,(0,0,100),1)
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(frame, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 5)
        cv2.putText(frame,'Smile detector',(185,460),font1,1,(0,0,0),2)
    return frame

def NOSE(gray,frame):
    h=nose_cascade.detectMultiScale(gray,1.7,5)
    cv2.putText(frame,'Nose detection system is activated',(50,20),font2,1,(0,0,100),1)
    for(x,y,w,h) in h:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
        cv2.putText(frame,'Nose detector',(185,460),font1,1,(0,0,0),2)
    return frame

def CHIN(gray,frame):
    h=nose_cascade.detectMultiScale(gray,1.7,5)
    cv2.putText(frame,'Chin detection system is activated',(50,20),font2,1,(0,0,100),1)
    for(x,y,w,h) in h:
        cv2.rectangle(frame,(x,y+140),(x+w,y+h+40),(255,0,0),3)
        cv2.putText(frame,'Chin detector',(185,460),font1,1,(0,0,0),2)
    return frame

def HandS(gray,frame):
    h=hd_cascade.detectMultiScale(gray,1.5,5)
    cv2.putText(frame,'Head and Shoulder detection system is activated',(50,20),font2,1,(0,0,100),1)
    for(x,y,w,h) in h:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
        cv2.putText(frame,'Head&Shoulder detector',(170,460),font1,1,(0,0,0),2)
    return frame

def FandE(gray, frame):
    faces=face_cascade.detectMultiScale(gray, 1.3, 5)
    cv2.putText(frame,'Face and Eye detection system is activated',(50,20),font2,1,(0,0,100),1)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame,'Multi detector',(185,460),font1,1,(0,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)   
    return frame

def MandS(gray, frame):
    mouth=mouth_cascade.detectMultiScale(gray, 1.3, 50)
    cv2.putText(frame,'Mouth and Smile detection system is activated',(50,20),font2,1,(0,0,100),1)
    for (x, y, w, h) in mouth:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame,'Multi detector',(185,460),font1,1,(0,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        smile = smile_cascade.detectMultiScale(roi_gray, 1.3,10)
        for (ex, ey, ew, eh) in smile:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)   
    return frame

def MOUTH(gray,frame):
    h=mouth_cascade.detectMultiScale(gray,1.3,50)
    cv2.putText(frame,'Mouth detection system is activated',(50,20),font2,1,(0,0,100),1)
    for(x,y,w,h) in h:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
        cv2.putText(frame,'Mouth detector',(185,460),font1,1,(0,0,0),2)
    return frame


#/////////////////////////////////////FRAMES OF OBJECT/////////////////////////////////////////////////////

def face_frame():
   _, face_frame.frame = cap.read()
   face_frame.frame = cv2.flip(face_frame.frame, 1)
   gray= cv2.cvtColor(face_frame.frame, cv2.COLOR_BGR2GRAY)
   canvas=FACE(gray,face_frame.frame)
   img = Image.fromarray(canvas)
   imgtk = ImageTk.PhotoImage(image=img)
   face_module.lmain.imgtk = imgtk
   face_module.lmain.configure(image=imgtk)
   face_module.lmain.after(10, face_frame)

def eyes_frame():
   _, eyes_frame.frame = cap.read()
   eyes_frame.frame = cv2.flip(eyes_frame.frame, 1)
   gray= cv2.cvtColor(eyes_frame.frame, cv2.COLOR_BGR2GRAY)
   canvas=EYES(gray,eyes_frame.frame)
   img = Image.fromarray(canvas)
   imgtk = ImageTk.PhotoImage(image=img)
   eyes_module.lmain.imgtk = imgtk
   eyes_module.lmain.configure(image=imgtk)
   eyes_module.lmain.after(10, eyes_frame)

def eyebrows_frame():
   _, eyebrows_frame.frame = cap.read()
   eyebrows_frame.frame = cv2.flip(eyebrows_frame.frame, 1)
   gray= cv2.cvtColor(eyebrows_frame.frame, cv2.COLOR_BGR2GRAY)
   canvas=EYEBROWS(gray,eyebrows_frame.frame)
   img = Image.fromarray(canvas)
   imgtk = ImageTk.PhotoImage(image=img)
   eyebrows_module.lmain.imgtk = imgtk
   eyebrows_module.lmain.configure(image=imgtk)
   eyebrows_module.lmain.after(10, eyebrows_frame)

def cheek_frame():
   _, cheek_frame.frame = cap.read()
   cheek_frame.frame = cv2.flip(cheek_frame.frame, 1)
   gray= cv2.cvtColor(cheek_frame.frame, cv2.COLOR_BGR2GRAY)
   canvas=CHEEK(gray,cheek_frame.frame)
   img = Image.fromarray(canvas)
   imgtk = ImageTk.PhotoImage(image=img)
   cheek_module.lmain.imgtk = imgtk
   cheek_module.lmain.configure(image=imgtk)
   cheek_module.lmain.after(10, cheek_frame)

def mouth_frame():
   _, mouth_frame.frame = cap.read()
   mouth_frame.frame = cv2.flip(mouth_frame.frame, 1)
   gray= cv2.cvtColor(mouth_frame.frame, cv2.COLOR_BGR2GRAY)
   canvas=MOUTH(gray,mouth_frame.frame)
   img = Image.fromarray(canvas)
   imgtk = ImageTk.PhotoImage(image=img)
   mouth_module.lmain.imgtk = imgtk
   mouth_module.lmain.configure(image=imgtk)
   mouth_module.lmain.after(10, mouth_frame)

def hd_frame():
   _, hd_frame.frame = cap.read()
   hd_frame.frame = cv2.flip(hd_frame.frame, 1)
   gray= cv2.cvtColor(hd_frame.frame, cv2.COLOR_BGR2GRAY)
   canvas=HandS(gray,hd_frame.frame)
   img = Image.fromarray(canvas)
   imgtk = ImageTk.PhotoImage(image=img)
   hd_module.lmain.imgtk = imgtk
   hd_module.lmain.configure(image=imgtk)
   hd_module.lmain.after(10,hd_frame)

def fe_frame():
   _, fe_frame.frame = cap.read()
   fe_frame.frame = cv2.flip(fe_frame.frame, 1)
   gray= cv2.cvtColor(fe_frame.frame, cv2.COLOR_BGR2GRAY)
   canvas=FandE(gray,fe_frame.frame)
   img = Image.fromarray(canvas)
   imgtk = ImageTk.PhotoImage(image=img)
   fe_module.lmain.imgtk = imgtk
   fe_module.lmain.configure(image=imgtk)
   fe_module.lmain.after(10,fe_frame)

def ms_frame():
   _, ms_frame.frame = cap.read()
   ms_frame.frame = cv2.flip(ms_frame.frame, 1)
   gray= cv2.cvtColor(ms_frame.frame, cv2.COLOR_BGR2GRAY)
   canvas=MandS(gray,ms_frame.frame)
   img = Image.fromarray(canvas)
   imgtk = ImageTk.PhotoImage(image=img)
   ms_module.lmain.imgtk = imgtk
   ms_module.lmain.configure(image=imgtk)
   ms_module.lmain.after(10,ms_frame)

def nose_frame():
   _, nose_frame.frame = cap.read()
   nose_frame.frame = cv2.flip(nose_frame.frame, 1)
   gray= cv2.cvtColor(nose_frame.frame, cv2.COLOR_BGR2GRAY)
   canvas=NOSE(gray,nose_frame.frame)
   img = Image.fromarray(canvas)
   imgtk = ImageTk.PhotoImage(image=img)
   nose_module.lmain.imgtk = imgtk
   nose_module.lmain.configure(image=imgtk)
   nose_module.lmain.after(10, nose_frame)

def chin_frame():
   _, chin_frame.frame = cap.read()
   chin_frame.frame = cv2.flip(chin_frame.frame, 1)
   gray= cv2.cvtColor(chin_frame.frame, cv2.COLOR_BGR2GRAY)
   canvas=CHIN(gray,chin_frame.frame)
   img = Image.fromarray(canvas)
   imgtk = ImageTk.PhotoImage(image=img)
   chin_module.lmain.imgtk = imgtk
   chin_module.lmain.configure(image=imgtk)
   chin_module.lmain.after(10, chin_frame)

def smile_frame():
   _, smile_frame.frame = cap.read()
   smile_frame.frame = cv2.flip(smile_frame.frame, 1)
   gray= cv2.cvtColor(smile_frame.frame, cv2.COLOR_BGR2GRAY)
   canvas=SMILE(gray,smile_frame.frame)
   img = Image.fromarray(canvas)
   imgtk = ImageTk.PhotoImage(image=img)
   smile_module.lmain.imgtk = imgtk
   smile_module.lmain.configure(image=imgtk)
   smile_module.lmain.after(10, smile_frame)

def hair_frame():
   _, hair_frame.frame = cap.read()
   hair_frame.frame = cv2.flip(hair_frame.frame, 1)
   gray= cv2.cvtColor(hair_frame.frame, cv2.COLOR_BGR2GRAY)
   canvas=HAIR(gray,hair_frame.frame)
   img = Image.fromarray(canvas)
   imgtk = ImageTk.PhotoImage(image=img)
   hair_module.lmain.imgtk = imgtk
   hair_module.lmain.configure(image=imgtk)
   hair_module.lmain.after(10, hair_frame)

#//////////////////////////////////////////OBJECT MODULE////////////////////////////////////////////////////////


def face_module():
   root = Toplevel()
   face_module.lmain =Label(root)
   face_module.lmain.pack()
   exit_button=Button(root,text="quit",height=5,width=45,fg="red",bg="white",command=root.destroy)
   exit_button.pack()
   face_frame()
   root.mainloop()
   cap.release()

def eyes_module():
   root = Toplevel()
   eyes_module.lmain =Label(root)
   eyes_module.lmain.pack()
   exit_button=Button(root,text="quit",height=5,width=45,fg="red",bg="white",command=root.destroy)
   exit_button.pack()
   eyes_frame()
   root.mainloop()
   cap.release()

def eyebrows_module():
   root = Toplevel()
   eyebrows_module.lmain =Label(root)
   eyebrows_module.lmain.pack()
   exit_button=Button(root,text="quit",height=5,width=45,fg="red",bg="white",command=root.destroy)
   exit_button.pack()
   eyebrows_frame()
   root.mainloop()
   cap.release()

def cheek_module():
   root = Toplevel()
   cheek_module.lmain =Label(root)
   cheek_module.lmain.pack()
   exit_button=Button(root,text="quit",height=5,width=45,fg="red",bg="white",command=root.destroy)
   exit_button.pack()
   cheek_frame()
   root.mainloop()
   cap.release()

def mouth_module():
   root = Toplevel()
   mouth_module.lmain =Label(root)
   mouth_module.lmain.pack()
   exit_button=Button(root,text="quit",height=5,width=45,fg="red",bg="white",command=root.destroy)
   exit_button.pack()
   mouth_frame()
   root.mainloop()
   cap.release()

def smile_module():
   root = Toplevel()
   smile_module.lmain =Label(root)
   smile_module.lmain.pack()
   exit_button=Button(root,text="quit",height=5,width=45,fg="red",bg="white",command=root.destroy)
   exit_button.pack()
   smile_frame()
   root.mainloop()
   cap.release()

def hd_module():
   root = Toplevel()
   hd_module.lmain =Label(root)
   hd_module.lmain.pack()
   exit_button=Button(root,text="quit",height=5,width=45,fg="red",bg="white",command=root.destroy)
   exit_button.pack()
   hd_frame()
   root.mainloop()
   cap.release()

def fe_module():
   root = Toplevel()
   fe_module.lmain =Label(root)
   fe_module.lmain.pack()
   exit_button=Button(root,text="quit",height=5,width=45,fg="red",bg="white",command=root.destroy)
   exit_button.pack()
   fe_frame()
   root.mainloop()
   cap.release()

def ms_module():
   root = Toplevel()
   ms_module.lmain =Label(root)
   ms_module.lmain.pack()
   exit_button=Button(root,text="quit",height=5,width=45,fg="red",bg="white",command=root.destroy)
   exit_button.pack()
   ms_frame()
   root.mainloop()
   cap.release()

def nose_module():
   root = Toplevel()
   nose_module.lmain =Label(root)
   nose_module.lmain.pack()
   exit_button=Button(root,text="quit",height=5,width=45,fg="red",bg="white",command=root.destroy)
   exit_button.pack()
   nose_frame()
   root.mainloop()
   cap.release()

def chin_module():
   root = Toplevel()
   chin_module.lmain =Label(root)
   chin_module.lmain.pack()
   exit_button=Button(root,text="quit",height=5,width=45,fg="red",bg="white",command=root.destroy)
   exit_button.pack()
   chin_frame()
   root.mainloop()
   cap.release()

def hair_module():
   root = Toplevel()
   hair_module.lmain =Label(root)
   hair_module.lmain.pack()
   exit_button=Button(root,text="quit",height=5,width=45,fg="red",bg="white",command=root.destroy)
   exit_button.pack()
   hair_frame()
   root.mainloop()
   cap.release()
   

#////////////////////////////////////////////////////////////////////////////////////////
def second_module():
   root2=Toplevel()
   root2.title("FOT")
   root2.configure(background='white')
   root2.iconbitmap("images/saeICO.ico")

   header=Label(root2,text="FACE OBJECT TRACKING",bg="white",fg="black",font= ('times', 20, 'bold'))
   header.grid(row=0,column=1)

   info1=Label(root2,text="  Object Detection using Haar feature-based cascade classifiers is an effective object_detection  ")
   info1.grid(row=1,column=1)

   info2=Label(root2,text="method proposed by Paul Viola and Michael Jones in their paper, Rapid Object Detection using")
   info2.grid(row=2,column=1)

   info3=Label(root2,text="a Boosted Cascade of Simple Features in 2001.")
   info3.grid(row=3,column=1)

   face=Button(root2,text="FACE",fg="black",font= ('times', 15, 'bold'),command=face_module)
   face.grid(row=4,column=0,sticky=N+S+E+W)

   eyes=Button(root2,text="EYES",fg="black",font= ('times', 15, 'bold'),command=eyes_module)
   eyes.grid(row=4,column=1,sticky=N+S+E+W)

   nose=Button(root2,text="NOSE",fg="black",font= ('times', 15, 'bold'),command=nose_module)
   nose.grid(row=4,column=2,sticky=N+S+E+W)

   mouth=Button(root2,text="MOUTH",fg="black",font= ('times', 15, 'bold'),command=mouth_module)
   mouth.grid(row=5,column=0,sticky=N+S+E+W)

   smile=Button(root2,text="SMILE",fg="black",font= ('times',15, 'bold'),command=smile_module)
   smile.grid(row=5,column=1,sticky=N+S+E+W)

   hair=Button(root2,text="HAIR",fg="black",font= ('times', 15, 'bold'),command=hair_module)
   hair.grid(row=5,column=2,sticky=N+S+E+W)

   hd=Button(root2,text="HEAD & SHOULDER",fg="black",font= ('times', 15, 'bold'),command=hd_module)
   hd.grid(row=6,column=0,sticky=N+S+E+W)

   fe=Button(root2,text="FACE + EYES",fg="black",font= ('times', 15, 'bold'),command=fe_module)
   fe.grid(row=6,column=1,sticky=N+S+E+W)

   ms=Button(root2,text="MOUTH + SMILES",fg="black",font= ('times', 15, 'bold'),command=ms_module)
   ms.grid(row=6,column=2,sticky=N+S+E+W)

   eyebrows=Button(root2,text="EYEBROWS",fg="black",font= ('times', 15, 'bold'),command=eyebrows_module)
   eyebrows.grid(row=7,column=0,sticky=N+S+E+W)

   cheek=Button(root2,text="CHEEKS",fg="black",font= ('times', 15, 'bold'),command=cheek_module)
   cheek.grid(row=7,column=1,sticky=N+S+E+W)

   chin=Button(root2,text="CHIN",fg="black",font= ('times', 15, 'bold'),command=chin_module)
   chin.grid(row=7,column=2,sticky=N+S+E+W)

   exit_button=Button(root2,text="QUIT",fg="red",bg="black",height=3,width=10,command=root2.destroy,font= ('times',10, 'bold'))
   exit_button.grid(row=9,column=1)

   root2.mainloop()

def MainModule():
   global main
   main=Tk()
   main.title("SAE(security asylum evident)")
   main.maxsize(500,500)
   main.minsize(500,500)
   main.iconbitmap("images/saeICO.ico")
   main.configure(bg="white")

   #FIRST FRAME
   FirstFrame=Frame(main,bg="white")
   
   back=Image.open("images/saeICO.ico")
   background=ImageTk.PhotoImage(back)

   
   
   Label(FirstFrame,bg="white",width=300, height=300,border=0,highlightthickness=0,image=background).pack()
   Label(FirstFrame,bg="white",fg="sky blue",width=3, height=1,text="SAE",border=0,font="helvetica 50 bold").pack(side=TOP)

   Label(FirstFrame,bg="white",fg="sky blue",text="DETECTING SYSTEM",border=0,font="helvetica 15 bold").pack()
   
   FirstFrame.grid(row=0,column=0)
   
   #SECOND FRAME
   SecondFrame=Frame(main)

   image1=Image.open("images/masterButton.png")
   master=ImageTk.PhotoImage(image1)
   image2=Image.open("images/helpButton.png")
   Help=ImageTk.PhotoImage(image2)
   image3=Image.open("images/exitButton.png")
   quitB=ImageTk.PhotoImage(image3)
   
   masterButton=Button(SecondFrame,image=master,border=0,highlightthickness=0,command=second_module)
   masterButton.grid(row=0,column=1)
   #helpButton=Button(SecondFrame,image=Help,border=0,highlightthickness=0,command=HelpModule)
   #helpButton.grid(row=2,column=1)
   quitButton=Button(SecondFrame,image=quitB,border=0,highlightthickness=0,command=quit)
   quitButton.grid(row=3,column=1)
   
   SecondFrame.grid(row=0,column=1)
   
   main.mainloop()

MainModule()



