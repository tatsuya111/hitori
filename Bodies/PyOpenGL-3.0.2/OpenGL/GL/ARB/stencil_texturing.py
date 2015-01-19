'''OpenGL extension ARB.stencil_texturing

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.stencil_texturing to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension allows texturing of the stencil component of a packed depth
	stencil texture. Stencil values are returned as unsigned integers. It is
	not possible to sample both depth and stencil values from the same
	texture, and this extension allows the app to select which is sampled for
	the bound texture.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/stencil_texturing.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.stencil_texturing import *
### END AUTOGENERATED SECTION