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

class OpenGLObject(object):
	"""OpenGLオブジェクト。"""

	def __init__(self):
		"""OpenGLオブジェクトのコンストラクタ。"""
		if DEBUG: print __name__, self.__init__.__doc__

		self._rgb = [1.0, 1.0, 1.0]

		return

	def rendering(self):
		"""OpenGLオブジェクトをレンダリングする。"""
		if DEBUG: print __name__, self.rendering.__doc__

		glColor4d(self._rgb[0], self._rgb[1], self._rgb[2], 1.0)

		return

	def rgb(self, red, green, blue):
		"""OpenGLオブジェクトの色を設定する。"""
		if DEBUG: print __name__, self.rgb.__doc__

		self._rgb = [red, green, blue]

		return