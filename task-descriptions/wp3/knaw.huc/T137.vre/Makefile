services.pdf:
	circo -Tpdf -Goverlap=false -Gsplines=true -o services.pdf services.dot

services.png:
	circo -Tpng -Goverlap=false -Gsplines=true -o services.png services.dot

plan.pdf:
	pandoc -s -f gfm -H ../../style/header.sty -o plan.pdf plan.md

pres.pdf:
	pandoc -t beamer pres.md -o pres.pdf

clean:
	rm services.pdf services.png plan.pdf pres.pdf

all: services.pdf services.png plan.pdf pres.pdf
