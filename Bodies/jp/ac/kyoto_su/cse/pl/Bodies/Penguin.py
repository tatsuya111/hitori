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

class PenguinModel(OpenGLModel):
	"""ペンギンのモデル。"""

	def __init__(self):
		"""ペンギンのモデルのコンストラクタ。"""
		if TRACE: print __name__, self.__init__.__doc__

		super(PenguinModel, self).__init__()
		self._projection.eye_point_([-6.6153435525924 , 3.5413918991617 , 27.440373330962])
		self._projection.sight_point_([0.070155 , 0.108575 , 0.056235])
		self._projection.up_vector_([0.03950581341181 , 0.99260439594225 , -0.11478590446043])
		self._projection.fovy_(13.527497808711)
		self._axes_scale = 2.0

		filename = os.path.join(os.getcwd(), 'penguin.txt')
		if os.path.exists(filename) and os.path.isfile(filename):
			pass
		else:
			url = 'http://www.cc.kyoto-su.ac.jp/~atsushi/Programs/Penguin/penguin.txt'
			urllib.urlretrieve(url, filename)

		with open(filename, "rU") as a_file:
			while True:
				a_string = a_file.readline()
				if len(a_string) == 0: break
				a_list = a_string.split()
				if len(a_list) == 0: continue
				first_string = a_list[0]
				if first_string == "number_of_vertexes":
					number_of_vertexes = int(a_list[1])
				if first_string == "number_of_polygons":
					number_of_polygons = int(a_list[1])
				if first_string == "end_header":
					get_tokens = (lambda file: file.readline().split())
					collection_of_vertexes = []
					for n_th in range(number_of_vertexes):
						a_list = get_tokens(a_file)
						a_vertex = map(float, a_list[0:3])
						collection_of_vertexes.append(a_vertex)
					index_to_vertex = (lambda index: collection_of_vertexes[index-1])
					for n_th in range(number_of_polygons):
						a_list = get_tokens(a_file)
						number_of_indexes = int(a_list[0])
						index = number_of_indexes + 1
						indexes = map(int, a_list[1:index])
						vertexes = map(index_to_vertex, indexes)
						a_polygon = OpenGLPolygon(vertexes)
						self._display_object.append(a_polygon)
					for n_th in range(number_of_polygons):
						a_list = get_tokens(a_file)
						rgb_color = map(float, a_list[0:3])
						a_polygon = self._display_object[n_th]
						a_polygon.rgb(*rgb_color)

		return

	def default_window_title(self):
		"""ペンギンのウィンドウのタイトル(ラベル)を応答する。"""
		if TRACE: print __name__, self.default_window_title.__doc__

		return "Penguin"