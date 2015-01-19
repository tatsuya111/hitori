#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import urllib

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Projection import OpenGLProjection
from View import OpenGLView
from Controlle import OpenGLController

TRACE = True
DEBUG = False

class OpenGLModel(object):
	"""OpenGLモデル。"""

	def __init__(self):
		"""OpenGLモデルのコンストラクタ。"""
		if TRACE: print __name__, self.__init__.__doc__

		self._display_object = []
		self._projection = OpenGLProjection()
		self._display_list = None
		self._view = None
		self._axes_scale = 1.0

		return

	def default_controllerew_class(self):
		"""OpenGLモデルを表示するデフォルトのビューのクラスを応答する。"""
		if TRACE: print __name__, self.default_controllerew_class.__doc__

		return OpenGLController

	def default_view_class(self):
		"""OpenGLモデルを表示するデフォルトのビューのクラスを応答する。"""
		if TRACE: print __name__, self.default_view_class.__doc__

		return OpenGLView

	def default_window_title(self):
		"""OpenGLウィンドウのタイトル(ラベル)を応答する。"""
		if TRACE: print __name__, self.default_window_title.__doc__

		return "Untitled"

	def display_list(self):
		"""OpenGLモデルのディスプレイリスト(表示物をコンパイルしたOpenGLコマンド列)を応答する。"""
		if TRACE: print __name__, self.display_list.__doc__

		if self._display_list == None:
			self._display_list = glGenLists(1)
			glNewList(self._display_list, GL_COMPILE)
			glColor4d(0.5, 0.5, 1.0, 1.0)
			for index, each in enumerate(self._display_object):
				if DEBUG: print index,
				each.rendering()
			glEndList()

		return self._display_list

	def open(self):
		"""OpenGLモデルを描画するためのOpenGLのウィンドウを開く。"""
		if TRACE: print __name__, self.open.__doc__

		view_class = self.default_view_class()
		self._view = view_class(self)

		return

	def rendering(self):
		"""OpenGLモデルをレンダリングする。"""
		if TRACE: print __name__, self.rendering.__doc__

		glCallList(self.display_list())

		return
