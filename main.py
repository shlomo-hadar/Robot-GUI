import tkinter as tk
import cv2
from PIL import ImageTk, Image



def video_stream():
    _, frame = cap.read()
    if _:
        frame = cv2.resize(frame, (int(screen_width / 2), int(screen_height / 2)), interpolation=cv2.INTER_AREA)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        NWFLabel.imgtk = imgtk
        NWFLabel.configure(image=imgtk)
    NWFLabel.after(1, video_stream2)


def video_stream2():
    _, frame = cap2.read()
    if _:
        frame = cv2.resize(frame, (int(screen_width / 2), int(screen_height / 2)), interpolation=cv2.INTER_AREA)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        SWFLabel.imgtk = imgtk
        SWFLabel.configure(image=imgtk)
    SWFLabel.after(1, video_stream)


root = tk.Tk()

root.title('Robot Gui')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

canvas = tk.Canvas(root, height=screen_width, width=screen_width, bg="red")
canvas.pack()

NWFrame = tk.Frame(root, bg="blue")
NWFrame.place(x=0, y=0, width=((screen_width / 2) - 1), height=(screen_height / 2 - 1))

SWFrame = tk.Frame(root, bg="black")
SWFrame.place(x=0, y=screen_height / 2, width=((screen_width / 2) - 1), height=(screen_height / 2 - 1))

EFrame = tk.Frame(root, bg="orange")
EFrame.place(x=screen_width / 2, y=0, width=(screen_width / 2), height=screen_height)

cap = cv2.VideoCapture('shniki.mp4')
NWFLabel = tk.Label(NWFrame, width=int(screen_width / 2 - 1), height=int(screen_height / 2 - 1))
NWFLabel.pack()

# TODO verify ip camera stream address
cap2 = cv2.VideoCapture('rtsp://10.0.22.120:554')
SWFLabel = tk.Label(SWFrame, bg="cyan", width=int(screen_width / 2 - 1), height=int(screen_height / 2 - 1))
SWFLabel.pack()

try:
    video_stream()
except cv2.error:
    print("shniki")
finally:
    print("The 'try except' is finished")
print("shniki")
root.mainloop()
