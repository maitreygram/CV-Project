import numpy as np 
import cv2
#import g2o
from matplotlib import pyplot as plt
import pygame
from frame import *
from constants import *
from Display2D import *
from Display3D import *


# f2d = dim2display()
f3d = dim3display()

# pygame.init()
# screen = pygame.display.set_mode([W,H])
	
cap = cv2.VideoCapture('drive.mp4')  
s = 1
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
		features1, features2, pose, matches, numMatched = matchFeatures(current_frames[-1], current_frames[-2])
		
		worldCoords = cv2.triangulatePoints(I44[:3], pose[:3], features1.T, features2.T)
		current_frames[-1].pose = np.matmul(pose, current_frames[-2].pose)

		# print(worldCoords)
		# nice_worldCoords
		# print(current_frames[-1].pose)
		# print(np.linalg.det(current_frames[-1].pose[:3,:3]))
		# print(worldCoords[:,np.abs(worldCoords[3,:]) > 0.005].shape)
		# worldCoords = worldCoords[:,np.abs(worldCoords[3,:]) > 0.005]
		
		worldCoords = np.array(worldCoords[:,(np.abs(worldCoords[3,:]) > 0.00005) & (worldCoords[2,:] > 0)])

		if worldCoords.shape[1] > 0:
			worldCoords /= worldCoords[3,:]
			print(worldCoords[0,0], '\t', worldCoords[1,0], '\t', worldCoords[2,0], '\t', worldCoords[3,0])

		# print("numMatched \n", numMatched)
		# print(pose)
		# exit(0)

		print((worldCoords[:3, :]))

		# f2d.display2D(frame.image, matches)
		f3d.display3D(worldCoords[:3, :])

		# f = np.rot90(frame.image)
		# disp = pygame.surfarray.make_surface(f)
		# disp = pygame.transform.flip(disp, True, False)
		
		# for pt1, pt2 in matches:
		# 	u1,v1 = map(lambda x: int(round(x)), pt1)
		# 	u2,v2 = map(lambda x: int(round(x)), pt2)

		# 	pygame.draw.circle(disp,(255,0,0),(u1,v1),2)
		# 	pygame.draw.line(disp,(0,0,255),(u1,v1),(u2,v2),2)

		# screen.blit(disp, (0,0))
		# pygame.display.update()
		# pygame.display.flip()
	
		# cv2.waitKey(25)

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
