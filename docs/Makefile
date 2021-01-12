initial_presentation.pdf: initial_presentation.md
	pandoc -t beamer initial_presentation.md -o initial_presentation.pdf

webservices_forwarding.png: webservices_forwarding.uml
	java -jar plantuml.jar webservices_forwarding.uml
	#requires plantuml, see: https://plantuml.com/
