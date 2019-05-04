import numpy as np 
import cv2
from matplotlib import pyplot as plt
import pygame

X = 500
Y = 500
pygame.init()
screen = pygame.display.set_mode([X,Y])

def process_frame(frame):
	
	frame = cv2.resize(frame, (X, Y))
	frame_1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	corners = cv2.goodFeaturesToTrack(frame_1,300,0.01,10)
	corners = np.int0(corners)
	frame = np.rot90(frame)


	disp = pygame.surfarray.make_surface(frame)
	disp = pygame.transform.flip(disp, True, False)
	for i in corners:
	    x,y = i.ravel()
	    pygame.draw.circle(disp,(255,0,0),(x,y),2)

	
	
	screen.blit(disp, (0,0))
	pygame.display.update()
	pygame.display.flip()
	
	cv2.waitKey(25)

	return
	
cap = cv2.VideoCapture('initial_key_frame.mp4')  
frame_init = []
while cap.isOpened():
    
    ret, frame = cap.read()
    if (ret == False):
    	break
    frame_init.append(frame)
    
    #process_frame(frame)
    

# When everything done, release the capture
print('a')

# extract ORB features

for frame in frame_init:
	orb = cv2.ORB_create()
	frame_1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	corners = cv2.goodFeaturesToTrack(frame_1,300,0.01,10)
	keypoint_object = []
	for i in corners:
	    u,v = i.ravel()
	    keypoint_object.append(cv2.KeyPoint(u,v, _size=20))

	kp, des = orb.compute(frame, keypoint_object)
	# Extraction and 
	

