import tkinter as tk
import cv2
from PIL import ImageTk, Image
import time

# import imageio

# def stream():
#     try:
#         image = video.get_next_data()
#         frame_image = Image.fromarray(image)
#         frame_image=ImageTk.PhotoImage(frame_image)
#         l1.config(image=frame_image)
#         l1.image = frame_image
#         l1.after(delay, lambda: stream())
#     except:
#         video.close()
#         return
# ########### Main Program ############
# root = Tk()
# root.title('Robot Gui')
# f1=Frame()
# l1 = Label(f1)
# l1.pack()
# f1.pack()
# video_name = "shniki.mp4"   #Image-path
# video = imageio.get_reader(video_name)
# delay = int(1000 / video.get_meta_data()['fps'])
# stream()
# root.mainloop()

# ##########
# import tkinter as tk
#
# root = tk.Tk()
#
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# print(str(screen_width)+"+"+str(screen_height))

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.title('Robot Gui')
# screen.geometry(x=screen_width,y=screen_height)
# root.geometry("1920x1080")

canvas = tk.Canvas(root, height=screen_width, width=screen_width, bg="red")
canvas.pack()

NWFrame = tk.Frame(root, bg="blue")
NWFrame.place(x=0, y=0, width=((screen_width / 2) - 1), height=(screen_height / 2 - 1))

SWFrame = tk.Frame(root, bg="black")
SWFrame.place(x=0, y=screen_height / 2, width=((screen_width / 2) - 1), height=(screen_height / 2 - 1))

EFrame = tk.Frame(root, bg="orange")
EFrame.place(x=screen_width / 2, y=0, width=(screen_width / 2), height=screen_height)



cap = cv2.VideoCapture('shniki.mp4')
NWFlabel = tk.Label(NWFrame, width=int(screen_width / 2 - 1), height=int(screen_height / 2 - 1))
NWFlabel.pack()

cap2 = cv2.VideoCapture('WhatsApp Video 2021-03-01 at 13.37.13.mp4')
SWFLabel = tk.Label(SWFrame, bg="cyan", width=int(screen_width / 2 - 1), height=int(screen_height / 2 - 1))
SWFLabel.pack()

def video_stream():
    _, frame = cap.read()
    frame = cv2.resize(frame, (int(screen_width/2), int(screen_height/2)), interpolation=cv2.INTER_AREA)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    NWFlabel.imgtk = imgtk
    NWFlabel.configure(image=imgtk)
    NWFlabel.after(1, video_stream2)

def video_stream2():
    _, frame = cap2.read()
    frame = cv2.resize(frame, (int(screen_width/2), int(screen_height/2)), interpolation=cv2.INTER_AREA)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    SWFLabel.imgtk = imgtk
    SWFLabel.configure(image=imgtk)
    SWFLabel.after(1, video_stream)

try:

    video_stream()
    # video_stream2()
except cv2.error:
    print("shniki")
finally:
    print("The 'try except' is finished")
print("shniki")
root.mainloop()
