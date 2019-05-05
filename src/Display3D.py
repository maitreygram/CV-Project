import pygame
from constants import *
import cv2
import OpenGL.GL as gl
from OpenGL.GLU import *
from pygame.locals import *
import sys
import pangolin
import numpy as np
from multiprocessing import Process, Queue


def Cube(points):
	x,y, z = points.shape
	glBegin(GL_POINTS)
	for i in range (0, x):
		glVertex3fv(points[i,:3,:])
		print(points[i,:3,:])
	glEnd()

class dim3display(object):

	def __init__(self):
		super(dim3display, self).__init__()
		self.frames = None
		self.points = None
		self.data = Queue()
		self.vp = Process(target=self.viewer_thread, args=(self.data,))
		self.vp.daemon = True
		self.vp.start()

	def viewer_thread(self, data):
		self.viewer_init(1024, 768)
		while 1:
			self.viewer_refresh(data)

	def viewer_init(self, w, h):
		pangolin.CreateWindowAndBind('Map Viewer', w, h)
		gl.glEnable(gl.GL_DEPTH_TEST)

		self.scam = pangolin.OpenGlRenderState(
			pangolin.ProjectionMatrix(w, h, 420, 420, w//2, h//2, 0.2, 10000),
			pangolin.ModelViewLookAt(0, -10, -8,
									0, 0, 0,
									0, -1, 0))
		self.handler = pangolin.Handler3D(self.scam)

		# Create Interactive View in window
		self.dcam = pangolin.CreateDisplay()
		self.dcam.SetBounds(pangolin.Attach(0), pangolin.Attach(1),
					  pangolin.Attach(0), pangolin.Attach(1),w/h)
		self.dcam.SetHandler(self.handler)
		# hack to avoid small Pangolin, no idea why it's *2
		self.dcam.Resize(pangolin.Viewport(0,0,w*2,h*2))
		self.dcam.Activate()
		# exit(0)

	def viewer_refresh(self, data):
		top = None
		while not data.empty():
			top = data.get()

		if top is None:
			return

		self.frames = top[0]
		self.points = top[1]

		gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
		gl.glClearColor(0.0, 0.0, 0.0, 1.0)
		self.dcam.Activate(self.scam)

		if self.frames is not None:
			gl.glColor3f(0.0, 1.0, 0.0)
			pangolin.DrawCameras(self.frames[:-1])


		if self.points is not None and self.points.shape[0] > 0:
			# draw keypoints

			colors = np.zeros((len(self.points), 3))
			# print(self.points.shape)
			colors[:, 1] = 1 -self.points[:, 0] / 10.0
			colors[:, 2] = 1 - self.points[:, 1] / 10.0
			colors[:, 0] = 1 - self.points[:, 2] / 10.0

			gl.glPointSize(2)
			gl.glColor3f(0.0, 0.0, 1.0)
			# pangolin.DrawPoints(self.points, colors)

		pangolin.FinishFrame()
	
	def dispAdd(self, frames, points):
		if self.data is None:
			return

		poses = []
		points3D = []
		for f in frames:
			# invert pose for display only
			poses.append(np.linalg.inv(f.pose))

		for ptset in points:
			for pt in ptset:
				points3D.append(pt[:3])


		# print(points.shape)
		# for pt in points:

		# print(np.array(points3D).shape)
		self.data.put((np.array(poses), np.array(points3D)))