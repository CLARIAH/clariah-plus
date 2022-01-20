plantuml.jar:
	wget -O plantuml.jar http://sourceforge.net/projects/plantuml/files/plantuml.jar/download

%.png: %.uml plantuml.jar
	java -jar plantuml.jar $<

shared-development-roadmap.md: introduction.md epics/shared/[-a-z]*.md sdr_datamodel.png
	echo -e "---\ntitle: CLARIAH Shared Development Roadmap 2022-2023\n---\n" > shared-development-roadmap.md
	cat introduction.md >> shared-development-roadmap.md
	echo -e "# Shared Epics\n\n" >> shared-development-roadmap.md
	cat epics/shared/README.md | grep -ve "^#" | grep -ve "^\*" >> shared-development-roadmap.md
	cat epics/shared/[-a-z]*.md | helpers/yaml2markdown.py >> shared-development-roadmap.md
	echo -e "# Domain-specific Epics\n\n" >> shared-development-roadmap.md
	cat epics/specific/README.md | grep -ve "^#" | grep -ve "^\*" >> shared-development-roadmap.md
	echo -e "# Appendix: Evaluation Metrics\n\n" >> shared-development-roadmap.md
	cat technology-readiness-level.md compliance-level.md stakeholder-readiness-level.md >> shared-development-roadmap.md

shared-development-roadmap.pdf: shared-development-roadmap.md helpers/header.sty
	pandoc --number-sections --table-of-contents --top-level-division chapter -s -f gfm+yaml_metadata_block -H helpers/header.sty -o shared-development-roadmap.pdf $<
