from tkinter import *
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import time

class App:
    def __init__(self, video_source=0):
        self.window = Tk()
        self.window.resizable(0,0)
        self.window['bg'] = 'black'
        self.video_source = video_source

        self.vid = Cam(self.video_source)
        self.label = Label(self.window, text ='OpenCV_Camera', font = 16, bg='blue', fg='white').pack(side=TOP, fill=BOTH)
        self.canvas = Canvas(self.window, width = self.vid.width, height = self.vid.height, bg='black')
        self.canvas.pack()

        self.button = Button(self.window, text="Capture",width=30, bg='grey', command = self.Capture)
        self.button.pack(anchor = CENTER, expand = True)
        self.update()
        self.window.mainloop()

    def Capture(self):
        check, frame = self.vid.getFrame()
        if check:
            print("Capture")

            img = "IMG-" + time.strftime("%H-%M-%S-%d-%m") + ".jpg"
            cv2.imwrite(img, frame)
            messagebox.showinfo("OpenCV_Camera","Image has been saved!")


    def update(self):
        isTrue, frame = self.vid.getFrame()
        if isTrue:
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
            self.canvas.create_image(0,0, image = self.photo, anchor = NW)

        self.window.after(20, self.update)
        


class Cam:
    def __init__(self, video_source=0):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open Camera")

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    def getFrame(self):
        if self.vid.isOpened():
            isTrue, frame = self.vid.read()
            if isTrue:
                return(isTrue,cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return(isTrue,None)
        else:
            return(isTrue, None)
        

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

if __name__ == "__main__":
    App()


