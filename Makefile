all: SRS.pdf

SRS.pdf: __generated_requirements.tex src/SRS.tex
	pdflatex src/SRS.tex

__generated_requirements.tex: src/requirements_tex_generator.py src/requirements.json
	python3 src/requirements_tex_generator.py

open:
	xdg-open SRS.pdf

clear:
	rm __generated_requirements.tex SRS.aux SRS.log


.PHONY: all clear open
