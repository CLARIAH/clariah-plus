%.pdf: %.md
	pandoc $< -s -f gfm+yaml_metadata_block --toc --shift-heading-level-by -1 --pdf-engine=xelatex -H ../shared-development-roadmap/helpers/header.sty -o $@

all: infrastructure-requirements.pdf software-metadata-requirements.pdf software-requirements.pdf

