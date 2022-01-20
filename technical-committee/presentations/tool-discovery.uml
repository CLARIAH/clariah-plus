@startuml


cloud "Software X" as X {
    component "source code repository\n(git)" as sourcerepo {
    }
    interface "git+https" as git

    sourcerepo - git
}

cloud {
    component "Software Service Y" as Y {
    }
    interface "metadata\nendpoint\n(https)" as metaendpoint
    Y -right- metaendpoint
}


component "Tool Store" {
    component "Tool Store" as ToolStore
    interface "Tool Store API" as ToolStoreAPI
    ToolStore -right- ToolStoreAPI
    component "Metadata Export B" as Exporter
}

cloud "Tool Portal A"  as CloudA {
    component "Tool Portal A\n(e.g. Ineo)" as ToolPortalA {
    }
    ToolPortalA .left.> ToolStoreAPI : queries
}



cloud "Tool Portal B" as CloudB {
    component "Tool Portal B\n(e.g. CLARIN Switchboard)" as ToolPortalB {
    }
    interface "Portal API/Registry" as InterfaceB
    ToolPortalB -left- InterfaceB
}

CloudA -[hidden]up- CloudB

component Harvester {

    component "Tool Source Registry" as SourceRegistry

    component "//codemeta-harvester//" as CH {
    }

    component "conversion to codemeta+" as conversion {
        [//codemetapy//]

        [//codemetar//]

        [//cffconvert//]

        [//somef//]
    }

    CH ..> conversion : invokes
    CH .up.> SourceRegistry : reads
    CH .right.> git : git clone/pull
    CH .right.> metaendpoint : HTTP GET
    CH .down.> ToolStoreAPI : publishes
}



Exporter .left.> ToolStoreAPI : queries
Exporter .right.> InterfaceB : updates

ToolStore .right.> Exporter : invokes


Harvester -[hidden]right- CloudA
Harvester -[hidden]right- CloudB

@enduml








