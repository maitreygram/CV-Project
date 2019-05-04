import numpy as np 
import cv2
from matplotlib import pyplot as plt
import pygame
from frame import *
from constants import *

pygame.init()
screen = pygame.display.set_mode([W,H])

def process_frame(frame):
	
	frame = cv2.resize(frame, (W, H))
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
	
cap = cv2.VideoCapture('drive.mp4')  

# KeyFrames = []
current_frames = []
while cap.isOpened():
	
	ret, frame = cap.read()
	if (ret == False):
		break

	frame = cv2.resize(frame, (W, H))
	frame = Frame(frame)
	current_frames.append(frame)

	getFeatures(frame)

	# print len(current_frames)
	if len(current_frames) > 1:
		F1, F2, matches, numMatched = matchFeatures(current_frames[-1], current_frames[-2])
		f = np.rot90(frame.image)
		disp = pygame.surfarray.make_surface(f)
		disp = pygame.transform.flip(disp, True, False)
		
		for pt1, pt2 in matches:
			u1,v1 = map(lambda x: int(round(x)), pt1)
			u2,v2 = map(lambda x: int(round(x)), pt2)

			pygame.draw.circle(disp,(255,0,0),(u1,v1),2)
			pygame.draw.line(disp,(0,0,255),(u1,v1),(u2,v2),2)

		screen.blit(disp, (0,0))
		pygame.display.update()
		pygame.display.flip()
	
		cv2.waitKey(25)

	# kp = [p.pt for p in frame.KeyPts]
	# f = np.rot90(frame.image)
	# corners = kp
	# corners = np.int0(corners)

	# disp = pygame.surfarray.make_surface(f)
	# disp = pygame.transform.flip(disp, True, False)
	# for i in corners:
	# 	x,y = i.ravel()
	# 	pygame.draw.circle(disp,(255,0,0),(x,y),2)

	# screen.blit(disp, (0,0))
	# pygame.display.update()
	# pygame.display.flip()
	
	# cv2.waitKey(25)
	

	
	# process_frame(frame)
	

# When everything done, release the capture
# extract ORB features

# for frame in frame_init:
# 	orb = cv2.ORB_create()
# 	frame_1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# 	corners = cv2.goodFeaturesToTrack(frame_1,300,0.01,10)
# 	keypoint_object = []
# 	for i in corners:
# 		u,v = i.ravel()
# 		keypoint_object.append(cv2.KeyPoint(u,v, _size=20))

# 	kp, des = orb.compute(frame, keypoint_object)
# 	# Extraction and 