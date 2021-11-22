plantuml.jar:
	wget -O plantuml.jar http://sourceforge.net/projects/plantuml/files/plantuml.jar/download

sdr_datamodel.png: sdr_datamodel.uml plantuml.jar
	java -jar plantuml.jar sdr_datamodel.uml
