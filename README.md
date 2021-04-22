# Robot-GUI

project was conducted on a system with OS ubuntu 20.04 and the noetic ros distrobution

required libraries in python:
    tkinter 
	(installation info at "https://www.tutorialspoint.com/how-to-install-tkinter-in-python")
    openCV (cv2)
        ("pip install opencv-python" in the terminal)
    PIL
	("pip install Pillow" in the terminal)
	(if you have installed two python versions type 
	"python3 -m pip install Pillow" to install it for python 3)

also required are the following ros packages:
	rviz_camera_stream (can be found at "https://github.com/lucasw/rviz_camera_stream")
	web_video_server (can be found at "https://github.com/RobotWebTools/web_video_server")

after you're all set up to launch the project you have two options.
1)after you are all set up open a terminal window and type ./file

2) you will need to open a terminal with three windows

	a)in the first you will launch the "roscore" command

	b)in the second you will launch the command "~/catkin_ws$ roslaunch rviz_camera_stream 			demo.launch" (the command starts at the roslaunch)

	c)in the third you will launch the command "~/catkin_ws$ rosrun web_video_server 			web_video_server" (the command starts at the rosrun)

	at this point you can launch your python "main.py" to run the program

© all the rights reserved to Kohelet.


