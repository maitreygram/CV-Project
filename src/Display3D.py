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
# sys.path.append('/home/youknowwho/Documents/software/pangolin')


def Cube(points):
	# print(points.shape)
	x,y, z = points.shape

	# print(points)
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
		while not data.empty():
			self.frames = data.get()

		gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
		gl.glClearColor(0.0, 0.0, 0.0, 1.0)
		self.dcam.Activate(self.scam)

		if self.frames is not None:
	  # if self.frames[0].shape[0] >= 2:
	  #   # draw poses
	  #   gl.glColor3f(0.0, 1.0, 0.0)
	  #   pangolin.DrawCameras(self.current[0][:-1])

	  # if self.state[0].shape[0] >= 1:
	  #   # draw current pose as yellow
	  #   gl.glColor3f(1.0, 1.0, 0.0)
	  #   pangolin.DrawCameras(self.state[0][-1:])

	  # if self.state[1].shape[0] != 0:
	  #   # draw keypoints
	  #   gl.glPointSize(5)
	  #   gl.glColor3f(1.0, 0.0, 0.0)
	  #   pangolin.DrawPoints(self.state[1], self.state[2])

			gl.glColor3f(0.0, 1.0, 0.0)
			pangolin.DrawCameras(self.frames[:-1])
		pangolin.FinishFrame()

	# def __init__(self):
	# 	self.data = []
	# 	display = (W,H)
	# 	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	# 	gluPerspective(45, (display[0]/display[1]), 0.1, 5.0)
	# 	glTranslatef(0.0,0.0, -5)
		
	# def display3D(self, points):

	# 	self.data.append(points)
	# 	Cube(np.array(self.data))
	# 	pygame.display.flip()
	# 	pygame.time.wait(10)

	# 	return
	
	def dispAdd(self, frames):
		if self.data is None:
			return

		poses = []
		for f in frames:
			# invert pose for display only
			poses.append(np.linalg.inv(f.pose))      	

		self.data.put(np.array(poses))
  #   	poses, pts, colors = [], [], []
  #   	for f in mapp.frames:
  #     		# invert pose for display only
  #     		poses.append(np.linalg.inv(f.pose))
  #   	for p in mapp.points:
  #     		pts.append(p.pt)
  #     		colors.append(p.color)
		# self.q.put((np.array(poses), np.array(pts), np.array(colors)/256.0))
