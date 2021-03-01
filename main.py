import tkinter as tk
import cv2
from PIL import ImageTk, Image

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
lmain = tk.Label(NWFrame, width=int(screen_width / 2 - 1), height=int(screen_height / 2 - 1))

lmain.pack()


def video_stream():
    _, frame = cap.read()
    frame = cv2.resize(frame, (960, 540), interpolation=cv2.INTER_AREA)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream)


try:
    video_stream()
except cv2.error:
    print("shniki")
finally:
    print("The 'try except' is finished")
print("shniki")
root.mainloop()
