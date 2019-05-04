import numpy as np 
import cv2
from matplotlib import pyplot as plt
from constants import *

def Similarity(H):
	U, sigma, V = np.linalg.svd(H)
	if np.linalg.det(U) < 0:
		U *= -1.0
	if np.linalg.det(V) < 0:
		V *= -1.0
	W = np.array([[0,-1,0 ], [1,0,0], [0,0,1]], dtype=float)
	R = np.dot(np.dot(U, W), V)
	if np.sum(R.diagnol() < 0):
		R = np.dot(np.dot(U, W.T), V)
	t = U[:,2]
	if t[2]<0:
		t *= -1
	similarity = np.eye(4)
	similarity[:3, :3] = R
	similarity[:3, 3] = t
	return similarity

def transform_coordinates(pt):
	ret = []
	point = pt[0]
	# print(pt[0].shape)
	for i in range(0, len(pt)):
		
		x1 = np.array([pt[i][0][0], pt[i][0][1], 1])
		x2 = np.array([pt[i][1][0], pt[i][1][1], 1])
		x1 = np.matmul(Kinv, x1.T).T
		x2 = np.matmul(Kinv, x2.T).T
		point[0] = x1[:2] 
		point[1] = x2[:2] 
		ret.append(point)
		# print(point)	
	ret = np.array(ret)
	print(pt[-1], 'pt')
	print(point, 'point')
	exit(0)
	return ret


