import numpy as np 
import cv2
from matplotlib import pyplot as plt
from constants import *

def Pose(H):
	W = np.array([[0,-1,0 ], [ 1,0,0], [0,0,1]], dtype=float)
	
	U, sigma, V = np.linalg.svd(H)
	if np.linalg.det(U) < 0:
		U *= -1.0
	if np.linalg.det(V) < 0:
		V *= -1.0
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
	for i in range(0, len(pt)):	
		x1 = np.array([pt[i,0,0], pt[i,0,1], 1])
		x2 = np.array([pt[i,1,0], pt[i,1,1], 1])
		x1 = np.matmul(Kinv, x1.T).T
		x2 = np.matmul(Kinv, x2.T).T
		point = [x1[:2], x2[:2]] 
		ret.append(point)

	ret = np.array(ret)
	# print 'pt', pt[0]
	# print 'ret', ret[0]
	return ret


