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

class BunnyModel(OpenGLModel):
	"""うさぎのモデル。"""

	def __init__(self):
		"""うさぎのモデルのコンストラクタ。"""
		if TRACE: print __name__, self.__init__.__doc__

		super(BunnyModel, self).__init__()
		self._axes_scale = 0.1

		filename = os.path.join(os.getcwd(), 'bunny.ply')
		if os.path.exists(filename) and os.path.isfile(filename):
			pass
		else:
			url = 'http://www.cc.kyoto-su.ac.jp/~atsushi/Programs/Bunny/bunny.ply'
			urllib.urlretrieve(url, filename)

		with open(filename, "rU") as a_file:
			while True:
				a_string = a_file.readline()
				if len(a_string) == 0: break
				a_list = a_string.split()
				if len(a_list) == 0: continue
				first_string = a_list[0]
				if first_string == "element":
					second_string = a_list[1]
					if second_string == "vertex":
						number_of_vertexes = int(a_list[2])
					if second_string == "face":
						number_of_faces = int(a_list[2])
				if first_string == "end_header":
					get_tokens = (lambda file: file.readline().split())
					collection_of_vertexes = []
					for n_th in range(number_of_vertexes):
						a_list = get_tokens(a_file)
						a_vertex = map(float, a_list[0:3])
						collection_of_vertexes.append(a_vertex)
					index_to_vertex = (lambda index: collection_of_vertexes[index])
					for n_th in range(number_of_faces):
						a_list = get_tokens(a_file)
						indexes = map(int, a_list[1:4])
						vertexes = map(index_to_vertex, indexes)
						a_tringle = OpenGLTriangle(*vertexes)
						a_tringle.rgb(1.0, 1.0, 1.0)
						self._display_object.append(a_tringle)
				if first_string == "comment":
					second_string = a_list[1]
					if second_string == "eye_point_xyz":
						self._projection.eye_point_(map(float, a_list[2:5]))
					if second_string == "sight_point_xyz":
						self._projection.sight_point_(map(float, a_list[2:5]))
					if second_string == "up_vector_xyz":
						self._projection.up_vector_(map(float, a_list[2:5]))
					if second_string == "zoom_height" and a_list[3] == "fovy":
						self._projection.fovy_(float(a_list[4]))

		return

	def default_window_title(self):
		"""うさぎのウィンドウのタイトル(ラベル)を応答する。"""
		if TRACE: print __name__, self.default_window_title.__doc__

		return "Stanford Bunny"