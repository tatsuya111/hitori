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

class WaspModel(OpenGLModel):
	"""スズメバチのモデル。"""

	def __init__(self):
		"""スズメバチのモデルのコンストラクタ。"""
		if TRACE: print __name__, self.__init__.__doc__

		super(WaspModel, self).__init__()
		self._projection.eye_point_([-5.5852450791872 , 3.07847342734 , 15.794105252496])
		self._projection.sight_point_([0.19825005531311 , 1.8530999422073 , -0.63795006275177])
		self._projection.up_vector_([0.070077999093727 , 0.99630606032682 , -0.049631725731267])
		self._projection.fovy_(41.480099231656)
		self._axes_scale = 4.0

		filename = os.path.join(os.getcwd(), 'wasp.txt')
		if os.path.exists(filename) and os.path.isfile(filename):
			pass
		else:
			url = 'http://www.cc.kyoto-su.ac.jp/~atsushi/Programs/Wasp/wasp.txt'
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
						rgb_color = map(float, a_list[index:index+3])
						a_polygon = OpenGLPolygon(vertexes)
						a_polygon.rgb(*rgb_color)
						self._display_object.append(a_polygon)

		return

	def default_window_title(self):
		"""スズメバチのウィンドウのタイトル(ラベル)を応答する。"""
		if TRACE: print __name__, self.default_window_title.__doc__

		return "Wasp"