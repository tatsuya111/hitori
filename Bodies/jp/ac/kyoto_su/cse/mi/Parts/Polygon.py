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

class OpenGLPolygon(OpenGLObject):
	"""OpenGL多角形。"""

	def __init__(self, vertexes):
		"""OpenGL多角形のコンストラクタ。"""
		if DEBUG: print __name__, self.__init__.__doc__

		super(OpenGLPolygon, self).__init__()
		self._vertexes = vertexes

		x = 0.0
		y = 0.0
		z = 0.0
		length = len(vertexes)
		for i in range(0, length):
			j = (i + 1) % length
			k = (i + 2) % length
			ux, uy, uz = map((lambda each1, each2: each1 - each2), vertexes[j], vertexes[i])
			vx, vy, vz = map((lambda each1, each2: each1 - each2), vertexes[k], vertexes[j])
			x = x + (uy * vz - uz * vy)
			y = y + (uz * vx - ux * vz)
			z = z + (ux * vy - uy * vx)
		normal_vector = [x, y, z]
		distance = sum(map((lambda each: each * each), normal_vector)) ** 0.5
		self._normal_unit_vector = map((lambda vector: vector / distance), normal_vector)

		return

	def rendering(self):
		"""OpenGL多角形をレンダリングする。"""
		if DEBUG: print __name__, self.rendering.__doc__

		super(OpenGLPolygon, self).rendering()
		glBegin(GL_POLYGON)
		glNormal3fv(self._normal_unit_vector)
		for vertex in self._vertexes:
			glVertex3fv(vertex)
		glEnd()

		return