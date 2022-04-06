plantuml.jar:
	wget -O plantuml.jar http://sourceforge.net/projects/plantuml/files/plantuml.jar/download

%.png: %.uml plantuml.jar
	java -jar plantuml.jar $<

%.pdf: %.md tool-discovery-components.png checkdeps
	cat $< | ../helpers/yaml2markdown.py | pandoc -s -F pantable -f gfm+yaml_metadata_block -H ../helpers/header.sty -o $@

.PHONY: checkdeps
checkdeps:
	@which pandoc > /dev/null || (echo "Dependency pandoc not found">&2 && false)
	@which pantable > /dev/null || (echo "Dependency pantable not found (pip install pantable)">&2 && false)
	@which pdflatex > /dev/null || (echo "Dependency pdflatex not found">&2 && false)
