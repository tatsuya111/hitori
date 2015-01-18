#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import urllib

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Bodies import Dragon
from Bodies import Baby
from Bodies import Bunny
from Bodies import Oni
from Bodies import Penguin
from Bodies import Wasp



TRACE = True
DEBUG = False
def main():
	"""OpenGL立体データを読み込んで描画する。"""
	if TRACE: print __name__, main.__doc__

	a_model = DragonModel()
	a_model.open()

	a_model = WaspModel()
	a_model.open()

	a_model = BunnyModel()
	a_model.open()

	a_model = PenguinModel()
	a_model.open()

	a_model = OniModel()
	a_model.open()

	a_model = BabyModel()
	a_model.open()

	glutMainLoop()

	return 0

if __name__ == '__main__':
	sys.exit(main())