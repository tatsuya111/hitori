#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import urllib

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from ..MVC.Model import OpenGLModel
from ..Parts.Polygon import OpenGLPolygon

TRACE = True
DEBUG = False

class OniModel(OpenGLModel):
	"""鬼のモデル。"""

	def __init__(self):
		"""鬼のモデルのコンストラクタ。"""
		if TRACE: print __name__, self.__init__.__doc__

		super(OniModel, self).__init__()
		self._projection.eye_point_([-6.6153435525924 , 3.5413918991617 , 27.440373330962])
		self._projection.sight_point_([-0.056150078773499 , 0.022249937057495 , -2.1525999903679])
		self._projection.up_vector_([0.03835909829153 , 0.99323407243554 , -0.10961139051838])
		self._projection.fovy_(19.221287002173)
		self._axes_scale = 2.7

		filename = os.path.join(os.getcwd(), 'oni.txt')
		if os.path.exists(filename) and os.path.isfile(filename):
			pass
		else:
			url = 'http://www.cc.kyoto-su.ac.jp/~atsushi/Programs/Oni/oni.txt'
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
				if first_string == "number_of_colors":
					number_of_colors = int(a_list[1])
				if first_string == "end_header":
					get_tokens = (lambda file: file.readline().split())
					collection_of_vertexes = []
					for n_th in range(number_of_vertexes):
						a_list = get_tokens(a_file)
						a_vertex = map(float, a_list[0:3])
						collection_of_vertexes.append(a_vertex)
					index_to_vertex = (lambda index: collection_of_vertexes[index-1])
					collection_of_indexes = []
					for n_th in range(number_of_polygons):
						a_list = get_tokens(a_file)
						number_of_indexes = int(a_list[0])
						index = number_of_indexes + 1
						indexes = map(int, a_list[1:index])
						vertexes = map(index_to_vertex, indexes)
						index = int(a_list[index])
						collection_of_indexes.append(index)
						a_polygon = OpenGLPolygon(vertexes)
						self._display_object.append(a_polygon)
					collection_of_colors = []
					for n_th in range(number_of_colors):
						a_list = get_tokens(a_file)
						rgb_color = map(float, a_list[0:3])
						collection_of_colors.append(rgb_color)
					for n_th in range(number_of_polygons):
						index = collection_of_indexes[n_th]
						rgb_color = collection_of_colors[index-1]
						a_polygon = self._display_object[n_th]
						a_polygon.rgb(*rgb_color)

		return

	def default_window_title(self):
		"""鬼のウィンドウのタイトル(ラベル)を応答する。"""
		if TRACE: print __name__, self.default_window_title.__doc__

		return "Oni"