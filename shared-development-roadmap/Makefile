plantuml.jar:
	wget -O plantuml.jar http://sourceforge.net/projects/plantuml/files/plantuml.jar/download

%.png: %.uml plantuml.jar
	java -jar plantuml.jar $<

shared-development-roadmap.md: introduction.md epics/[-a-z]*.md sdr_datamodel.png epics/tool-discovery-components.png
	echo -e "---\ntitle: CLARIAH Shared Development Roadmap 2022-2023\n---\n" > shared-development-roadmap.md
	cat introduction.md >> shared-development-roadmap.md
	echo -e "# Shared Epics\n\n" >> shared-development-roadmap.md
	cat epics/README.md | grep -ve "^#" | grep -ve "^\*" >> shared-development-roadmap.md
	cat epics/[-a-z]*.md | helpers/yaml2markdown.py >> shared-development-roadmap.md
	echo -e "# Appendix: Evaluation Metrics\n\n" >> shared-development-roadmap.md
	cat technology-readiness-level.md compliance-level.md stakeholder-readiness-level.md >> shared-development-roadmap.md

shared-development-roadmap.pdf: checkdeps shared-development-roadmap.md helpers/header.sty
	pandoc -F pantable --number-sections --table-of-contents --top-level-division chapter -s -f gfm+yaml_metadata_block -H helpers/header.sty -o shared-development-roadmap.pdf $<


.PHONY: checkdeps
checkdeps:
	@which pandoc > /dev/null || (echo "Dependency pandoc not found">&2 && false)
	@which pantable > /dev/null || (echo "Dependency pantable not found (pip install pantable)">&2 && false)
	@which pdflatex > /dev/null || (echo "Dependency pdflatex not found">&2 && false)






