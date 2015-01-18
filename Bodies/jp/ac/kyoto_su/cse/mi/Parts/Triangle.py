#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import urllib

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Object import OpenGLObject

TRACE = True
DEBUG = False

class OpenGLTriangle(OpenGLObject):
	"""OpenGL三角形。"""

	def __init__(self, vertex1, vertex2, vertex3):
		"""OpenGL三角形のコンストラクタ。"""
		if DEBUG: print __name__, self.__init__.__doc__

		super(OpenGLTriangle, self).__init__()
		self._vertex1 = vertex1
		self._vertex2 = vertex2
		self._vertex3 = vertex3

		ux, uy, uz = map((lambda value1, value0: value1 - value0), vertex2, vertex1)
		vx, vy, vz = map((lambda value1, value0: value1 - value0), vertex3, vertex1)
		normal_vector = [(uy * vz - uz * vy), (uz * vx - ux * vz), (ux * vy - uy * vx)]
		distance = sum(map((lambda value: value * value), normal_vector)) ** 0.5
		self._normal_unit_vector = map((lambda vector: vector / distance), normal_vector)

		return

	def rendering(self):
		"""OpenGL三角形をレンダリングする。"""
		if DEBUG: print __name__, self.rendering.__doc__

		super(OpenGLTriangle, self).rendering()
		glBegin(GL_TRIANGLES)
		glNormal3fv(self._normal_unit_vector)
		glVertex3fv(self._vertex1)
		glVertex3fv(self._vertex2)
		glVertex3fv(self._vertex3)
		glEnd()

		return