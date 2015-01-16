#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import urllib

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

TRACE = True
DEBUG = False

class OpenGLView(object):
	"""OpenGLビュー。"""

	window_postion = [100, 100]

	@classmethod
	def get_window_postion(a_class):
		"""ウィンドウを開くための位置を応答する。"""
		if TRACE: print __name__, a_class.get_window_postion.__doc__

		current_position = a_class.window_postion
		a_class.window_postion = map((lambda value: value + 30), a_class.window_postion)

		return current_position

	def __init__(self, a_model):
		"""OpenGLビューのコンストラクタ。"""
		if TRACE: print __name__, self.__init__.__doc__

		self._model = a_model
		controller_class = self._model.default_controllerew_class()
		self._controller = controller_class(self)
		self._angle_x = 0.0
		self._angle_y = 0.0
		self._angle_z = 0.0
		self._width = 400
		self._height = 400

		glutInit(sys.argv)
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
		glutInitWindowPosition(*OpenGLView.get_window_postion())
		glutInitWindowSize(self._width, self._height)
		glutCreateWindow(self._model.default_window_title())

		glutDisplayFunc(self.display)
		glutReshapeFunc(self.reshape)
		glutKeyboardFunc(self._controller.keyboard)
		glutMouseFunc(self._controller.mouse)
		glutMotionFunc(self._controller.motion)
		glutWMCloseFunc(self._controller.close)

		glEnable(GL_COLOR_MATERIAL)
		glEnable(GL_DEPTH_TEST)
		glDisable(GL_CULL_FACE)
		glEnable(GL_NORMALIZE)

		return

	def display(self):
		"""OpenGLで描画する。"""
		if TRACE: print __name__, self.display.__doc__

		projection = self._model._projection
		eye_point = projection.eye_point()
		sight_point = projection.sight_point()
		up_vector = projection.up_vector()
		fovy = projection.fovy()
		near = projection.near()
		far = projection.far()

		aspect = float(self._width) / float(self._height)

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(fovy, aspect, near, far)

		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		gluLookAt(eye_point[0], eye_point[1], eye_point[2],
				  sight_point[0], sight_point[1], sight_point[2],
				  up_vector[0], up_vector[1], up_vector[2])

		glClearColor(1.0, 1.0, 1.0, 1.0)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		glEnable(GL_LIGHTING)
		glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.5, 0.5, 0.5, 1.0])
		glLightModelf(GL_LIGHT_MODEL_LOCAL_VIEWER, 0.0)
		glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, 1.0)
		glEnable(GL_LIGHT0)
		glLightfv(GL_LIGHT0, GL_POSITION, [0.0, 0.0, 1.0, 0.0])
		glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [0.0, 0.0, -1.0])
		glLightfv(GL_LIGHT0, GL_SPOT_CUTOFF, 90.0)
		glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.5, 0.5, 0.5, 1.0])
		glLightfv(GL_LIGHT0, GL_SPECULAR, [0.5, 0.5, 0.5, 1.0])
		glLightfv(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.0)
		glLightfv(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, 0.0)
		glLightfv(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 1.0)

		self.display_axes()

		glRotated(self._angle_x, 1.0, 0.0, 0.0)
		glRotated(self._angle_y, 0.0, 1.0, 0.0)
		glRotated(self._angle_z, 0.0, 0.0, 1.0)

		self._model.rendering()

		glutSwapBuffers()

		return

	def display_axes(self):
		"""世界座標系を描画する。"""
		if TRACE: print __name__, self.display_axes.__doc__

		axes_scale = self._model._axes_scale
		scaled_by_n = (lambda vertex: map((lambda value: value * axes_scale), vertex))
		glBegin(GL_LINES)
		glColor([ 1.0, 0.0, 0.0, 1.0 ])
		glVertex(scaled_by_n([-1.00, 0.0, 0.0 ]))
		glVertex(scaled_by_n([ 1.68, 0.0, 0.0 ]))
		glColor([ 0.0, 1.0, 0.0, 1.0 ])
		glVertex(scaled_by_n([ 0.0,-1.00, 0.0 ]))
		glVertex(scaled_by_n([ 0.0, 1.68, 0.0 ]))
		glColor([ 0.0, 0.0, 1.0, 1.0 ])
		glVertex(scaled_by_n([ 0.0, 0.0,-1.00 ]))
		glVertex(scaled_by_n([ 0.0, 0.0, 1.68 ]))
		glEnd()

		return

	def reshape(self, width, height):
		"""OpenGLを再形成する。"""
		if TRACE: print __name__, self.reshape.__doc__

		self._width = width
		self._height = height

		glViewport(0, 0, width, height)

		return