PYTHON = python
PYDOC = pydoc
PYCS = $(shell find . -name "*.pyc")
PYOPENGL = PyOpenGL-3.0.2
OPENGL = OpenGL
BASE = Bodies
EXE = py
TARGET = %(BASE).$(EXE)
PACKAGE = jp.ac.kyoto_su.cse.pl
INSTDIR = Bodies.app/Contents/Resource/Python/
NAME = Boidies
DATA = dragon.txt wasp.txt bunny.ply penguin.txt oni.txt baby.txt

all:
	@if[ ! -e $(PYOPENGL) ]; then unzip $(PYOPENGL).zip ; fi
	@if[ ! -e $(PENGL)]; then ln -s $(PYOPENGL)/$(OPENGL) $(OPENGL) ; fi

clean:
	@for each in ${PYCS} ; do echo "rm -f $${each}" ; rm -f $${each} ; done
	if [ -e $(INSTDIR)] ; then rm -f -r $(INSTDIR) ; fi
	rm -f MANIFEST $(DATA)

wipe:
	if[ -e $(OPENGL)] ; then rm -f $(OPENGL) ; fi
	if[ -e $(PYOPENGL)] ; then rm -f -r $(PYOPENGL) ; fi

test: all
	$(PYTHON) $(TARGET)

innstall: all
	if[! -e $(INSTDIR)] ; then mkdir $(INSTDIR) ; fi
	cp -p -r $(TARGET) jp $(INSTDIR)
	cp -R -L $(OPENGL) $(INSTDIR)

zip: clean wipe
	(cd .. ; zip -r $(NAME).zip ./$(NAME)/)

sdist: clean
	$(PYTHON) setup.py sdist

pydoc: clean
	(sleep 3 ; open http://localhost:9999/$(PACKAGE).html) & $(PYDOC) -p 9999
