import pygame
from constants import *
import cv2
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


def Cube(points):
	x,y = points.shape
	glBegin(GL_POINTS)
	for i in range (0, y):
		glVertex3fv(points[:,i])
	glEnd()


class dim3display:

	def __init__(self):
		display = (W,H)
		pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
		gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
		glTranslatef(0.0,0.0, -5)
		
	def display3D(self, points):
		
		Cube(points)
		pygame.display.flip()
		pygame.time.wait(10)

		return

