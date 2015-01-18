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

class DragonModel(OpenGLModel):
	"""ドラゴンのモデル。"""

	def __init__(self):
		"""ドラゴンのモデルのコンストラクタ。"""
		if TRACE: print __name__, self.__init__.__doc__

		super(DragonModel, self).__init__()
		self._projection.eye_point_([-5.5852450791872 , 3.07847342734 , 15.794105252496])
		self._projection.sight_point_([0.27455347776413 , 0.20096999406815 , -0.11261999607086])
		self._projection.up_vector_([0.1018574904194 , 0.98480906061847 , -0.14062775604137])
		self._projection.fovy_(12.642721790235)

		filename = os.path.join(os.getcwd(), 'dragon.txt')
		if os.path.exists(filename) and os.path.isfile(filename):
			pass
		else:
			url = 'http://www.cc.kyoto-su.ac.jp/~atsushi/Programs/Dragon/dragon.txt'
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
				if first_string == "number_of_triangles":
					number_of_triangles = int(a_list[1])
				if first_string == "end_header":
					get_tokens = (lambda file: file.readline().split())
					collection_of_vertexes = []
					for n_th in range(number_of_vertexes):
						a_list = get_tokens(a_file)
						a_vertex = map(float, a_list[0:3])
						collection_of_vertexes.append(a_vertex)
					index_to_vertex = (lambda index: collection_of_vertexes[index-1])
					for n_th in range(number_of_triangles):
						a_list = get_tokens(a_file)
						indexes = map(int, a_list[0:3])
						vertexes = map(index_to_vertex, indexes)
						a_tringle = OpenGLTriangle(*vertexes)
						a_tringle.rgb(0.5, 0.5, 1.0)
						self._display_object.append(a_tringle)

		return

	def default_window_title(self):
		"""ドラゴンのウィンドウのタイトル(ラベル)を応答する。"""
		if TRACE: print __name__, self.default_window_title.__doc__

		return "Dragon"