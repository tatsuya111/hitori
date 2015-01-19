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

class OpenGLProjection(object):
	"""OpenGLプロジェクション。"""

	def __init__(self):
		"""OpenGLプロジェクションのコンストラクタ。"""
		if TRACE: print __name__, self.__init__.__doc__

		self._eye_point   = self._default_eye_point   = None
		self._sight_point = self._default_sight_point = None
		self._up_vector   = self._default_up_vector   = None
		self._fovy        = self._default_fovy        = None
		self._near        = self._default_near        = None
		self._far         = self._default_far         = None

		return

	def eye_point(self):
		"""視点を応答する。"""
		if TRACE: print __name__, self.eye_point.__doc__

		if self._eye_point == None: self.eye_point_([0.0, 0.0, 10.0])
		return self._eye_point

	def eye_point_(self, a_point):
		"""視点を設定する。"""
		if TRACE: print __name__, self.eye_point_.__doc__

		self._eye_point = a_point
		if self._default_eye_point == None: self._default_eye_point = a_point

		return

	def sight_point(self):
		"""注視点を応答する。"""
		if TRACE: print __name__, self.sight_point.__doc__

		if self._sight_point == None: self.sight_point_([0.0, 0.0, 0.0])
		return self._sight_point

	def sight_point_(self, a_point):
		"""注視点を設定する。"""
		if TRACE: print __name__, self.sight_point_.__doc__

		self._sight_point = a_point
		if self._default_sight_point == None: self._default_sight_point = a_point

		return

	def up_vector(self):
		"""上方向ベクトルを応答する。"""
		if TRACE: print __name__, self.up_vector.__doc__

		if self._up_vector == None: self.up_vector_([0.0, 1.0, 0.0])
		return self._up_vector

	def up_vector_(self, a_point):
		"""上方向ベクトルを設定する。"""
		if TRACE: print __name__, self.up_vector_.__doc__

		self._up_vector = a_point
		if self._default_up_vector == None: self._default_up_vector = a_point

		return

	def fovy(self):
		"""視界角を応答する。"""
		if TRACE: print __name__, self.fovy.__doc__

		if self._fovy == None: self.fovy_(30.0)
		return self._fovy

	def fovy_(self, a_float):
		"""視界角を設定する。"""
		if TRACE: print __name__, self.fovy_.__doc__

		self._fovy = a_float
		if self._default_fovy == None: self._default_fovy = a_float

		return

	def near(self):
		"""近を応答する。"""
		if TRACE: print __name__, self.near.__doc__

		if self._near == None: self.near_(0.01)
		return self._near

	def near_(self, a_float):
		"""近を設定する。"""
		if TRACE: print __name__, self.near_.__doc__

		self._near = a_float
		if self._default_near == None: self._default_near = a_float

		return

	def far(self):
		"""遠を応答する。"""
		if TRACE: print __name__, self.far.__doc__

		if self._far == None: self.far_(100)
		return self._far

	def far_(self, a_float):
		"""遠を設定する。"""
		if TRACE: print __name__, self.far_.__doc__

		self._far = a_float
		if self._default_far == None: self._default_far = a_float

		return

	def reset(self):
		"""プロジェクション情報をデフォルト(最初に設定されたパラメータ)に設定し直す。"""
		if TRACE: print __name__, self.reset.__doc__

		if self._default_eye_point != None:
			self._eye_point = self._default_eye_point

		if self._default_fovy != None:
			self._fovy = self._default_fovy

		return