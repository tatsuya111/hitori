'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_vertex_blend'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_vertex_blend',False)
_p.unpack_constants( """GL_MAX_VERTEX_UNITS_ARB 0x86A4
GL_ACTIVE_VERTEX_UNITS_ARB 0x86A5
GL_WEIGHT_SUM_UNITY_ARB 0x86A6
GL_VERTEX_BLEND_ARB 0x86A7
GL_CURRENT_WEIGHT_ARB 0x86A8
GL_WEIGHT_ARRAY_TYPE_ARB 0x86A9
GL_WEIGHT_ARRAY_STRIDE_ARB 0x86AA
GL_WEIGHT_ARRAY_SIZE_ARB 0x86AB
GL_WEIGHT_ARRAY_POINTER_ARB 0x86AC
GL_WEIGHT_ARRAY_ARB 0x86AD
GL_MODELVIEW0_ARB 0x1700
GL_MODELVIEW1_ARB 0x850A
GL_MODELVIEW2_ARB 0x8722
GL_MODELVIEW3_ARB 0x8723
GL_MODELVIEW4_ARB 0x8724
GL_MODELVIEW5_ARB 0x8725
GL_MODELVIEW6_ARB 0x8726
GL_MODELVIEW7_ARB 0x8727
GL_MODELVIEW8_ARB 0x8728
GL_MODELVIEW9_ARB 0x8729
GL_MODELVIEW10_ARB 0x872A
GL_MODELVIEW11_ARB 0x872B
GL_MODELVIEW12_ARB 0x872C
GL_MODELVIEW13_ARB 0x872D
GL_MODELVIEW14_ARB 0x872E
GL_MODELVIEW15_ARB 0x872F
GL_MODELVIEW16_ARB 0x8730
GL_MODELVIEW17_ARB 0x8731
GL_MODELVIEW18_ARB 0x8732
GL_MODELVIEW19_ARB 0x8733
GL_MODELVIEW20_ARB 0x8734
GL_MODELVIEW21_ARB 0x8735
GL_MODELVIEW22_ARB 0x8736
GL_MODELVIEW23_ARB 0x8737
GL_MODELVIEW24_ARB 0x8738
GL_MODELVIEW25_ARB 0x8739
GL_MODELVIEW26_ARB 0x873A
GL_MODELVIEW27_ARB 0x873B
GL_MODELVIEW28_ARB 0x873C
GL_MODELVIEW29_ARB 0x873D
GL_MODELVIEW30_ARB 0x873E
GL_MODELVIEW31_ARB 0x873F""", globals())
glget.addGLGetConstant( GL_MAX_VERTEX_UNITS_ARB, (1,) )
glget.addGLGetConstant( GL_ACTIVE_VERTEX_UNITS_ARB, (1,) )
glget.addGLGetConstant( GL_WEIGHT_SUM_UNITY_ARB, (1,) )
glget.addGLGetConstant( GL_VERTEX_BLEND_ARB, (1,) )
glget.addGLGetConstant( GL_CURRENT_WEIGHT_ARB, (1,) )
glget.addGLGetConstant( GL_WEIGHT_ARRAY_TYPE_ARB, (1,) )
glget.addGLGetConstant( GL_WEIGHT_ARRAY_STRIDE_ARB, (1,) )
glget.addGLGetConstant( GL_WEIGHT_ARRAY_SIZE_ARB, (1,) )
@_f
@_p.types(None,_cs.GLint,arrays.GLbyteArray)
def glWeightbvARB( size,weights ):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLshortArray)
def glWeightsvARB( size,weights ):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLintArray)
def glWeightivARB( size,weights ):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLfloatArray)
def glWeightfvARB( size,weights ):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLdoubleArray)
def glWeightdvARB( size,weights ):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLubyteArray)
def glWeightubvARB( size,weights ):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLushortArray)
def glWeightusvARB( size,weights ):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLuintArray)
def glWeightuivARB( size,weights ):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glWeightPointerARB( size,type,stride,pointer ):pass
@_f
@_p.types(None,_cs.GLint)
def glVertexBlendARB( count ):pass


def glInitVertexBlendARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
