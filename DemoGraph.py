"""
Copyright (C) 2023 TH Köln – University of Applied Sciences

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from GraphModel.Nodes.NodeSourceBook import NodeSourceBook
from GraphModel.Nodes.NodeSourceOnline import NodeSourceOnline
from GraphModel.Nodes.NodeSourcePaper import NodeSourcePaper


class DemoGraph:

    def __init__(self, graph: Graph):
        self.create_demo_nodes(graph)

    def create_demo_nodes(self, graph):
        """
        Diese Methode dient Ihnen also Demonstration für den Aufbau eines Graphen.
        """

        # Create Nodes
        how_to_node = NodeKnowledge("Dies ist der Inhalt des Knotens. Ein Zeilenumbruch erfolgt automatisch. Wenn Sie "
                                    "jedoch manuell einen Absatz einfügen möchten ist dies über \n \n möglich.\n \n"
                                    " Sie haben die Möglichkeit Text als *kursiv* oder **fett** oder ***kombiniert*** "
                                    "hervorzuheben.\n\n"
                                    "Mit der ***Leertaste*** können Sie Ihren Graphen ausrichten lassen. Hierbei "
                                    "wirken zwei Arten von  simulierten Kräften. Knoten stoßen sich generell ab "
                                    "zum Zweck der visuellen Verteilung. Desto weiter Knoten voneinander entfernt "
                                    "sind desto schwächer ist Abstoßungskraft. Knoten die miteinander verbunden sind "
                                    "ziehen sich an. Desto weiter Knoten voneinander entfernt sind umso stärker ist "
                                    "die Anziehungskraft.\n\n"
                                    "Mit der ***T*** Taste können Sie die Titel der Knoten ein und ausblenden.\n\n"
                                    "Mit der ***Esc*** Taste können Sie die Anwendung schließen.\n\n"
                                    "Darüber hinaus können Sie Überschriften in drei Ebenen definieren. Text der als "
                                    "Überschrift markiert wird, wird bis zum nächsten Zeilenumbruch als solcher "
                                    "erkannt.\n"
                                    "\n# Das ist Ebene 1\n"
                                    "Nach einem Absatz wird eine Überschrift automatisch unterbrochen."
                                    "\n## Das ist Ebene 2\n"
                                    "Wie sie sehen ist diese Überschrift etwas kleiner."
                                    "\n### Und abschließend Ebene 3\n"
                                    "Und hier die kleinste Form.\n\n"
                                    "\n# Hinweis\n"
                                    "Wenn Ihr Graph wächst wird es immer schwieriger werden ihn zu "
                                    "erweitern und zu verändern. Hier entsteht die Verbindung zu Softwareprojekten. "
                                    "Zu beginn ist alles noch leicht nachvollziehbar und übersichtlich. Desto mehr "
                                    "Funktionalität Sie jedoch implementieren um so komplexer wird Ihr System. "
                                    "Es gibt immer mehr Inhalte und mehr Verbindungen dieser Inhalte. Erschaffen Sie "
                                    "hierbei keine geeignete Struktur erhalten Sie was wir Spaghetti-Code oder einen "
                                    "Big Ball of Mud nennen. Alles ist scheinbar miteinander verbunden und erzeugt "
                                    "Abhängigkeiten miteinander. Wenn Sie ein Teil verändern wollen müssen Sie auch "
                                    "alle anderen Teile verändern. "
                                    "Ein Teil Ihrer Aufgabenstellung ist es mit dieser wachsenden Komplexität "
                                    "umzugehen. Sie entscheiden dabei als Team welchen Weg Sie einschlagen. Ziehen "
                                    "sie es vor die Inhalte hard zu coden also direkt in diese Methode zu schreiben? "
                                    "Werden Sie eigene Klassen und Methoden für die Bestandteile des Graphen anlegen? "
                                    "Schreiben Sie selbst einen Importer über den Sie Text Files einlesen können? "
                                    "Schreiben Sie ein User Interface um Texte direkt über die"
                                    "Applikation einzugeben? Denken Sie dabei auch an Modelle und wie Abstraktion "
                                    "Ihnen hilft Dinge zu vereinfachen. Planen Sie Ihren Graphen, teilen Sie "
                                    "Verantwortlichkeiten im Team auf, erstellen Sie Modelle und iterieren Sie um"
                                    "Ihren Wissensgraph inkrementell zu entwickeln. "
                                    ""
                                    "\n# Bilder\n"
                                    "Zu Illustrations-Knoten können Sie ein Bild hinzufügen. Hier für ist es notwendig "
                                    "das dieses Bild im Ordner Resources\Images abgelegt wird und der Name der Datei "
                                    "als dritter Parameter spezifiziert wird. Denken Sie daran Bilder in Git "
                                    "hinzuzufügen: Rechtsklick + Git + Add. Auch diese Bilder müssen Sie anschließend "
                                    "commiten und pushen."
                                    "\n # Verbindungen (Kanten) \n"
                                    "Knoten können über die Methode .connect mit einander verbunden werden. Dabei "
                                    "wird diese Methode auf dem Vater Knoten angewandt und das Kind als Parameter "
                                    "übergeben, \n\nz. B.: ***vater.connect(kind)***\n\n"
                                    "Wenn Sie im Graphen einen Knoten Verschieben, werden die Kinder immer "
                                    "mit verschoben. Sie können auch bidirektionale Verbindungen anlegen in dem Sie "
                                    "zusätzlich: *kind.connect(vater)* verwenden. Selektieren Sie einen Knoten, "
                                    "werden alle Kinder und Kindeskinder im Graphen optisch hervorgehoben."
                                    "\n # Menü \n"
                                    "Das Menü oben links stellt Ihnen zwei Optionen zur Verfügung."
                                    "\n ## Export \n"
                                    "Der Export erlaubt es Ihnen den aktuellen Graph als ZIP File zu exportieren. "
                                    "Neben dem Graphen werden auch alle Bilder im Image Ordner exportiert."
                                    "\n ## Import \n"
                                    "Der Import erlaubt es einen exportierten Graphen zu laden. Sie können auf diesem "
                                    "Wege die Graphen Ihrer Kommilitonen laden. Wenn Sie diese "
                                    "Funktion verwenden möchten, achten Sie bitte darauf, dass Bilder im "
                                    "importierten ZIP File in den Image Ordner Ihres Projektes importiert werden. "
                                    "Falls ein File mit dem identischen Namen im Image Ordner bereits vorhanden ist, "
                                    "wird der Name des importierten Bildes mit dem Namen Ihres Teams konkateniert/"
                                    "verbunden.\n\n",
                                    "Help Knoten: Dies ist der Titel Ihres Knotens")

        online_source_example_knowledge_node = NodeKnowledge("## Anmerkung: \n"
                                                             "Dies ist Knoten für Online-Quellen. In diesem konkreten Fall für Markdown "
                                                             "als Internet Quelle. Hierbei wird die offizielle Website des Entwicklers "
                                                             "von Markdown verwendet. Eine Website als Quelle ist legitim, wenn sie "
                                                             "bestimmte Kriterien der Glaubwürdigkeit und Zuverlässigkeit erfüllt. "
                                                             "Kriterien hierfür sind: \n\n"
                                                             "**- Expertise:**\n"
                                                             "Überprüfen Sie, wer hinter der Website steht. Ist es eine anerkannte "
                                                             "Institution, eine Bildungseinrichtung oder ein Experte auf dem Gebiet? \n\n"
                                                             "**- Aktualität:**\n"
                                                             "Überprüfen Sie das Datum der Veröffentlichung oder der letzten "
                                                             "Aktualisierung. Für viele Themen ist es wichtig, dass die Informationen "
                                                             "aktuell sind. \n\n"
                                                             "**- Genauigkeit und Zuverlässigkeit:**\n"
                                                             "Enthält die Website präzise Informationen, die mit anderen glaubwürdigen "
                                                             "Quellen übereinstimmen? Websites, die sorgfältig recherchiert und mit "
                                                             "Belegen untermauert sind, sind in der Regel vertrauenswürdiger.\n\n"
                                                             "**- Zweck und Objektivität:**\n"
                                                             "Beurteilen Sie den Zweck der Website. Ist sie darauf ausgerichtet, "
                                                             "objektive Informationen zu liefern, oder verfolgt sie kommerzielle, "
                                                             "politische oder ideologische Ziele? Objektive, unparteiische Quellen sind "
                                                             "generell vertrauenswürdiger.\n\n"
                                                             "**- Transparenz:**\n"
                                                             "Gute Quellen bieten oft Informationen über ihre Autoren, Finanzierung, "
                                                             "Mission und den Prozess der Inhaltsprüfung.\n\n"
                                                             "\n## Beispiel\n"
                                                             "\n### Autor:\n"
                                                             "Gruber, John"
                                                             "\n### Jahr:\n"
                                                             "2004"
                                                             "\n### Titel:\n"
                                                             "Markdown"
                                                             "\n### Titel der Website:\n"
                                                             "daringfireball.net"
                                                             "\n### Verfügbar unter:\n"
                                                             "https://daringfireball.net/projects/markdown/"
                                                             "\n### Zugriff am:\n"
                                                             "11. November 2023"
                                                             , "Online Quellen")

        literature_source_example_knowledge_node = NodeKnowledge("## Anmerkung: \n"
                                                                 "Dies ist Knoten für Literaturquellen. Hierbei sind folgende "
                                                                 "Informationen für ***Bücher*** essenziell:\n\n"
                                                                 "**- Autor:**\n Der vollständige Name des Autors.\n\n"
                                                                 "**- Erscheinungsjahr:**\n Das Jahr, in dem das Buch veröffentlicht "
                                                                 "wurde.\n\n"
                                                                 "**- Titel des Buches:**\n Der vollständige Titel des Buches, eventuell "
                                                                 "inklusive Untertitel.\n\n"
                                                                 "**- Auflage:**\n Inhalt kann sich mit den verschieden Auflagen "
                                                                 "eines Buches unterscheiden. Daher ist es wichtig die Auflage anzugeben, "
                                                                 "auf die Sie sich beziehen. \n\n"
                                                                 "**- Ort der Veröffentlichung:**\n"" Die Stadt, in der der Verlag seinen "
                                                                 "Sitz hat.\n\n"
                                                                 "**- Verlag:**\n Der Name des Verlags.\n\n"
                                                                 "\n## Beispiel\n"
                                                                 "\n### Autor:\n"
                                                                 "Martin, R.C."
                                                                 "\n### Veröffentlichungsjahr:\n"
                                                                 "2021"
                                                                 "\n### Titel:\n"
                                                                 "Clean Craftsmanship: Disciplines, Standards, and Ethics"
                                                                 "\n### Auflage:\n"
                                                                 "1. Auflage"
                                                                 "\n### Ort:\n"
                                                                 "Boston"
                                                                 "\n### Verlag:\n"
                                                                 "Addison-Wesley Professional"
                                                                 , "Bücher als Quellen")

        paper_source_example_knowledge_node = NodeKnowledge(
            "Für wissenschaftliche Veröffentlichungen (***Paper***) sind folgende "
            "Angaben notwendig:\n\n"
            "**- Autor(en) des Papers:**\n Die Namen der Autoren, in der "
            "Reihenfolge, in der sie im Paper aufgeführt sind.\n\n"
            "**- Jahr der Veröffentlichung:**\n Das Jahr, in dem das Paper "
            "veröffentlicht wurde.\n\n"
            "**- Titel des Papers:**\n Der vollständige Titel des Papers.\n\n"
            "**- Titel der Zeitschrift oder Konferenz:**\n Der Name der Zeitschrift "
            "oder der Konferenz, in der das Paper veröffentlicht wurde.\n\n"
            "**- Bandnummer(Ausgabennummer):**\n Die Band- und Ausgabennummer der "
            "Zeitschrift, in der das Paper erschien.\n\n"
            "**- Seitenzahlen:**\n Die Seitenzahlen des Papers in der Zeitschrift."
            "**- URL:**\n Falls das Paper online verfügbar ist, fügen Sie die URL "
            "hinzu.\n\n"
            "**- Zugriff am:**\n Das Datum, an dem Sie auf das Paper zugegriffen "
            "haben, falls es online verfügbar ist.\n\n"
            "\n## Beispiel\n"
            "\n### Autor:\n"
            "Dijkstra, E.W."
            "\n### Veröffentlichungsjahr:\n"
            "1972"
            "\n### Titel:\n"
            "The Humble Programmer"
            "\n### In:\n"
            "Communications of the ACM"
            "\n### Bandnummer(Ausgabennummer):\n"
            "15(10)"
            , "Paper als Quellen")

        literature_source_example_node = NodeSourceBook("Clean Craftsmanship: Disciplines, Standards, and Ethics",
                                                        "Martin, R.C.", "2021", "Boston", "Addison-Wesley Professional",
                                                        "978-0136915713")
        paper_source_example_node = NodeSourcePaper("The Humble Programmer", "Dijkstra, E.W.", "1972",
                                                    "Communications of the ACM", "15(10)",
                                                    comment = "Dies ist ein Kommentar für den Fall, dass Sie zusätzliche Ergänzungen zu Ihrer Quelle angeben möchten.")
        online_source_example_node = NodeSourceOnline("Markdown", "Gruber, John", "2004", "daringfireball.net",
                                                      "https://daringfireball.net/projects/markdown/",
                                                      "11. November 2023")
        illustration_node_example = NodeIllustration("Ein Beispiel für eine Illustration",
                                                     "illustration_node_example.png")

        # Add Nodes to Graph
        graph.add_new_node_to_graph(how_to_node)
        graph.add_new_node_to_graph(online_source_example_knowledge_node)
        graph.add_new_node_to_graph(literature_source_example_knowledge_node)
        graph.add_new_node_to_graph(paper_source_example_knowledge_node)

        graph.add_new_node_to_graph(literature_source_example_node)
        graph.add_new_node_to_graph(paper_source_example_node)
        graph.add_new_node_to_graph(online_source_example_node)

        graph.add_new_node_to_graph(illustration_node_example)

        # Connect Nodes
        how_to_node.connect(online_source_example_knowledge_node)
        how_to_node.connect(literature_source_example_knowledge_node)
        how_to_node.connect(paper_source_example_knowledge_node)
        how_to_node.connect(illustration_node_example)

        literature_source_example_knowledge_node.connect(literature_source_example_node)
        paper_source_example_knowledge_node.connect(paper_source_example_node)
        online_source_example_knowledge_node.connect(online_source_example_node)

        yassine_main_node = NodeKnowledge(
            "### Definition von GNU\n"
            "GNU steht für 'GNU's Not Unix' und wurde 1983 von Richard Stallman gegründet. "
            "Das Projekt hat das Ziel, ein Unix-ähnliches Betriebssystem aus freier Software zu schaffen. "
            "GNU verfolgt die Idee, Software zu entwickeln, die für alle Nutzer frei und öffentlich zugänglich ist. "
            "Das bedeutet, dass der Quellcode jederzeit von jedem verändert, genutzt und weitergegeben werden kann.\n"
            "\n"
            "GNU ist ein wichtiger Bestandteil der freien Softwarebewegung, die auf der Überzeugung beruht, dass Nutzer die Freiheit haben sollten, Software ohne Einschränkungen zu verwenden. "
            "Das Projekt betont die Bedeutung von offenem Quellcode und gemeinschaftlicher Entwicklung, die durch die GNU General Public License (GPL) gesichert wird. "
            "Diese Lizenz stellt sicher, dass Software, die unter GNU entwickelt wurde, immer frei und offen bleibt.\n"
            "\n"
            "Das GNU-Projekt begann als Antwort auf die zunehmende Kommerzialisierung der Softwarebranche. "
            "Richard Stallman, ein Programmierer am MIT, war enttäuscht, dass Software zunehmend proprietär wurde. "
            "Das bedeutete, dass Nutzer den Quellcode nicht mehr einsehen oder verändern durften. "
            "Um diesem Trend entgegenzuwirken, gründete Stallman GNU, das eine Alternative zu kommerziellen Softwarelösungen bieten sollte. "
            "Die Idee hinter GNU war, ein vollständiges Betriebssystem zu entwickeln, das aus rein freier Software besteht. "
            "Heute ist GNU ein wichtiger Teil der Linux-Distributionen, die weltweit verbreitet sind.\n"
            "Quelle: GNU Initial Announcement",
            "Definition von GNU"
        )

        # Die Knoten zum Graphen hinzufügen
        graph.add_new_node_to_graph(yassine_main_node)

        # Illustration des Hauptthemenknotens
        illustration_mainnode = NodeIllustration(
            "Hier ist ein Logo von GNU; generiert durch KI",
            "gnu-logo.png"
        )

        # Die Illustration zum Graphen hinzufügen und verbinden
        graph.add_new_node_to_graph(illustration_mainnode)
        yassine_main_node.connect(illustration_mainnode)

        yassine_node1 = NodeKnowledge(
            "### Einführung in die GNU-Philosophie\n"
            "Die Philosophie des GNU-Projekts basiert auf der Idee der freien Software, die es den Nutzern ermöglicht, "
            "Software zu nutzen, zu verändern, weiterzugeben und zu verbessern. Diese Prinzipien stellen sicher, dass der "
            "Anwender nicht nur die Kontrolle über die Software hat, sondern auch über den gesamten Entwicklungsprozess.\n\n"

            "### Grundlegende Idee von GNU\n"
            "Die grundlegende Idee hinter GNU ist, dass Software nicht nur für kommerzielle Zwecke entwickelt werden sollte, "
            "sondern vielmehr den Menschen dienen sollte. Das bedeutet, dass jeder Zugang zu Software haben und sie nach "
            "seinen Bedürfnissen anpassen kann, ohne durch Lizenzbeschränkungen eingeschränkt zu werden.\n\n"

            "### Die vier Freiheiten der GNU-Philosophie\n"
            "Richard Stallman, der Gründer von GNU, prägte die vier grundlegenden Freiheiten, die Nutzer mit freier Software "
            "genießen sollten:\n"
            "- **Die Freiheit**, die Software auszuführen, unabhängig von der eigenen Nutzung.\n"
            "- **Die Freiheit**, den Quellcode zu studieren und zu verändern, damit die Software an die eigenen Bedürfnisse "
            "angepasst werden kann.\n"
            "- **Die Freiheit**, Kopien der Software zu verbreiten, damit andere von der Software profitieren können.\n"
            "- **Die Freiheit**, die Software weiterzugeben und weiterzuentwickeln, sodass die Community kontinuierlich von "
            "Verbesserungen profitieren kann.\n\n"

            "### Auswirkungen der GNU-Philosophie\n"
            "Diese Freiheiten führen dazu, dass Software-Entwicklung und -Verbreitung nicht auf kommerzielle Interessen "
            "ausgerichtet sind, sondern auf Zusammenarbeit und Gemeinschaft. GNU fördert eine Welt, in der die Kontrolle "
            "über Technologie in den Händen der Menschen liegt und nicht in den Händen weniger großer Unternehmen.\n\n"

            "### Wissensaustausch und Innovation\n"
            "Die Philosophie stellt den gemeinnützigen Nutzen in den Vordergrund und ermöglicht eine Kultur des Wissensaustauschs "
            "und der Innovation.\n\n"
            "Quelle: GNU Philosophy",
            "Philosophie von GNU"  # Titel für den Knoten
        )

        # Den Knoten zum Graphen hinzufügen und verbinden
        graph.add_new_node_to_graph(yassine_node1)
        yassine_main_node.connect(yassine_node1)

        # Literaturquelle hinzufügen und verbinden
        literature_source_gnu_book = NodeSourceBook(
            "Open Sources: Voices from the Open Source Revolution",
            "Chris DiBona, Sam Ockman, Mark Stone et al.",
            "1999",
            "Sebastopol, CA",
            "O'Reilly Media",
            "978-1565925823"
        )
        graph.add_new_node_to_graph(literature_source_gnu_book)
        yassine_node1.connect(literature_source_gnu_book)

        yassine_node2 = NodeKnowledge(
            "### Einführung zur GPL-Lizenz\n"
            "Die GNU General Public License (GPL) ist eine der bekanntesten und am weitesten verbreiteten Lizenzen für freie "
            "Software. Sie wurde von Richard Stallman und der Free Software Foundation (FSF) entwickelt, um sicherzustellen, "
            "dass Software, die unter der GPL veröffentlicht wird, immer frei und offen bleibt. Die Lizenz stellt sicher, "
            "dass jeder, der die Software nutzt, diese unter bestimmten Bedingungen weitergeben und verändern darf.\n\n"

            "### Die wichtigsten Merkmale der GPL\n"
            "- **Freiheit zur Nutzung und Verbreitung**: Jeder kann die Software für beliebige Zwecke nutzen und sie auch an andere weitergeben.\n"
            "- **Quellcode zugänglich machen**: Wer die Software verändert oder weiterverbreitet, muss den Quellcode zur Verfügung stellen. "
            "Das gewährleistet Transparenz und die Möglichkeit zur Anpassung.\n"
            "- **Verbot der Einschränkung**: Die Lizenz stellt sicher, dass der Quellcode auch nach der Weitergabe immer frei bleibt und nicht "
            "durch zusätzliche Einschränkungen abgeändert wird. Wer also Software unter der GPL nutzt oder verbreitet, kann nicht verhindern, "
            "dass andere die Software ebenfalls nutzen und verändern.\n\n"

            "### Bedeutung der GPL für die freie Softwarebewegung\n"
            "Ein wichtiges Element der GPL ist, dass sie auch den Stellenwert der Freiheit in den Vordergrund stellt: Die Lizenz gibt nicht nur "
            "den rechtlichen Rahmen vor, sondern verfolgt das Ziel, eine Kultur der freien Software und Zusammenarbeit zu schaffen. Die GPL hat "
            "somit die freie Softwarebewegung weltweit beeinflusst und wird von einer Vielzahl von Projekten genutzt, darunter auch Linux.\n\n"

            "### Weltweite Zusammenarbeit durch GPL\n"
            "Die Lizenz ermöglicht eine weltweite Zusammenarbeit und stellt sicher, dass jeder von den Verbesserungen profitieren kann.\n\n"
            "Quelle: GNU General Public License",
            "Lizenz – GNU General Public License (GPL)"
        )

        # Den Knoten zum Graphen hinzufügen und verbinden
        graph.add_new_node_to_graph(yassine_node2)
        yassine_main_node.connect(yassine_node2)

        # Literaturquelle hinzufügen und verbinden
        literature_source_gnu_gpl = NodeSourceBook(
            "Free Software, Free Society: Selected Essays of Richard M. Stallman",
            "Richard M. Stallman",
            "2002",
            "Boston, MA",
            "GNU Press",
            "978-1882114986"
        )
        graph.add_new_node_to_graph(literature_source_gnu_gpl)
        yassine_node2.connect(literature_source_gnu_gpl)

        yassine_node3 = NodeKnowledge(
            "### Einführung: GNU-Projekt und Linux-Kernel\n"
            "Das GNU-Projekt und der Linux-Kernel sind zwei der wichtigsten Bestandteile der modernen Open-Source- und freien Softwarewelt. "
            "Während GNU die Werkzeuge und das Betriebssystem bereitstellt, bildet der Linux-Kernel die Grundlage für ein vollständiges, "
            "funktionales Betriebssystem. Zusammen bilden sie die Basis für viele der heute populärsten Linux-Distributionen.\n\n"

            "### Was ist der Linux-Kernel?\n"
            "Der Linux-Kernel, entwickelt von Linus Torvalds, ist der Kern eines Betriebssystems. Er übernimmt die Verwaltung der Hardware, "
            "die Kommunikation zwischen verschiedenen Softwarekomponenten und die Bereitstellung von Systemressourcen. Ohne den Kernel würde "
            "keine der Software, die unter GNU entwickelt wurde, richtig ausgeführt werden können. Allerdings ist der Linux-Kernel alleine "
            "noch kein vollständiges Betriebssystem. Hier kommt GNU ins Spiel.\n\n"

            "### Die Rolle von GNU\n"
            "GNU stellt eine Sammlung von Tools zur Verfügung, die die Systemverwendung und die Entwicklung ermöglichen. Programme wie der **GNU C Compiler (GCC)**, "
            "der **GNU Debugger (GDB)** und die **GNU Coreutils** bilden zusammen mit dem Linux-Kernel ein vollständiges System, das auf nahezu allen modernen "
            "Computern lauffähig ist. \n\n"

            "### Zusammenarbeit zwischen GNU und Linux\n"
            "Die Zusammenarbeit zwischen diesen beiden Elementen hat es Linux ermöglicht, sich als eines der beliebtesten und leistungsfähigsten Betriebssysteme "
            "der Welt zu etablieren, das sowohl für Server als auch für Desktop-PCs genutzt wird.\n\n"

            "### Bedeutung für die Open-Source-Welt\n"
            "Die Kombination von GNU und Linux hat dazu geführt, dass Open-Source-Betriebssysteme für eine breite Nutzerbasis zugänglich sind und von Entwicklern, "
            "Unternehmen und gemeinnützigen Organisationen auf der ganzen Welt verwendet werden. Durch die Open-Source-Philosophie können diese Systeme ständig "
            "weiterentwickelt und angepasst werden.\n\n"

            "Quelle: Linux and GNU",
            "Zusammenarbeit mit Linux"
        )

        # Den Knoten zum Graphen hinzufügen und verbinden
        graph.add_new_node_to_graph(yassine_node3)
        yassine_main_node.connect(yassine_node3)

        # Literaturquelle hinzufügen und verbinden
        literature_source_gnu_linux = NodeSourceBook(
            "Just for Fun: The Story of an Accidental Revolutionary",
            "Linus Torvalds, David Diamond",
            "2001",
            "New York",
            "HarperCollins Publishers",
            "978-0066620732"
        )
        graph.add_new_node_to_graph(literature_source_gnu_linux)
        yassine_node3.connect(literature_source_gnu_linux)

        yassine_node4 = NodeKnowledge(
            "### Einführung zur Bash (Bourne Again Shell)\n"
            "Die Bash (Bourne Again Shell) ist einer der bekanntesten und am weitesten verbreiteten Kommandozeilen-Interpreter. "
            "Sie wurde von **Brian Fox** für das **GNU-Projekt** entwickelt und stellt eine Benutzeroberfläche für das Betriebssystem bereit. "
            "Bash ermöglicht es den Nutzern, mit dem System zu interagieren, indem sie Befehle eingeben und die entsprechenden Prozesse ausführen. "
            "Sie ist die **Standard-Shell** in vielen **Linux-Distributionen** und wird häufig auch auf Unix-ähnlichen Systemen wie **macOS** und **BSD** verwendet.\n\n"

            "### Funktionen der Bash\n"
            "Die Bash bietet mehr als nur eine einfache Kommandozeile – sie enthält zahlreiche Funktionen, die die Arbeit mit der Shell effizienter machen:\n"
            "- **Skripterstellung**: Automatisierung von komplexen Aufgaben durch Bash-Skripte.\n"
            "- **Tab-Vervollständigung**: Schnelles Eingeben von Dateipfaden und Befehlen durch Autovervollständigung.\n"
            "- **Variablen, Schleifen und Bedingungen**: Unterstützung von Programmierkonzepten für flexible Systemadministration.\n\n"

            "### Flexibilität und Kompatibilität\n"
            "Ein bemerkenswertes Merkmal der Bash ist ihre **Kompatibilität** mit älteren Unix-Systemen sowie ihre Unterstützung für eine Vielzahl von **Skriptsprachen**. "
            "Dies macht sie zu einer der flexibelsten und mächtigsten Shells. Zusätzlich tragen Erweiterungen und Plug-ins dazu bei, dass Bash von einer breiten Nutzerbasis geschätzt wird.\n\n"

            "### Die GNU-Philosophie\n"
            "Bash steht im Einklang mit der **GNU-Philosophie**, da sie unter der **GNU General Public License (GPL)** lizenziert ist. "
            "Das bedeutet, dass jeder die Bash **kostenlos nutzen**, **ändern** und **weiterverbreiten** kann.\n\n"

            "Quelle: GNU Bash",
            "Bash (GNU-Shell)"
        )

        # Den Knoten zum Graphen hinzufügen und verbinden
        graph.add_new_node_to_graph(yassine_node4)
        yassine_main_node.connect(yassine_node4)

        # Literaturquelle hinzufügen und verbinden
        literature_source_bash = NodeSourceBook(
            "Learning the bash Shell: Unix Shell Programming",
            "Cameron Newham",
            "2016",
            "Sebastopol",
            "O'Reilly Media",
            "978-1491945066"
        )
        graph.add_new_node_to_graph(literature_source_bash)
        yassine_node4.connect(literature_source_bash)

        yassine_node5 = NodeKnowledge(
            "### Einführung in die GNU Coreutils\n"
            "Die **GNU Coreutils** sind eine Sammlung von grundlegenden Programmen und Werkzeugen, die für die Arbeit mit Dateien und Verzeichnissen in Unix-ähnlichen Betriebssystemen unverzichtbar sind. "
            "Sie bilden das **Herzstück vieler Linux-Distributionen** und ermöglichen grundlegende Aufgaben wie **Kopieren (cp)**, **Verschieben (mv)**, **Umbenennen (mv)** und **Löschen (rm)** von Dateien sowie das Anzeigen von Dateiinhalten mit **cat**.\n\n"

            "### Entwicklung und Funktionalität\n"
            "Die Coreutils wurden von der **Free Software Foundation (FSF)** entwickelt und sind ein wesentlicher Bestandteil des **GNU-Projekts**. "
            "Sie bieten eine **einheitliche Benutzererfahrung** und stellen sicher, dass dieselben Funktionen auf allen GNU-basierten Systemen verfügbar sind. "
            "Diese Tools helfen bei der **Dateiverwaltung**, **Textverarbeitung** und **Systemverwaltung**.\n\n"

            "### Anpassungsfähigkeit und Modularität\n"
            "Ein herausragendes Merkmal der GNU Coreutils ist ihre **Flexibilität** und **Modularität**. "
            "Viele Programme bieten zahlreiche **Optionen**, mit denen Nutzer das Verhalten der Tools anpassen können. "
            "So kann der Befehl **ls** mit Optionen wie **`-l`** für detaillierte Listenansichten oder **`-a`** für versteckte Dateien aufgerufen werden.\n\n"

            "### Portabilität und Interoperabilität\n"
            "Die **Portabilität** der GNU Coreutils macht sie auf verschiedenen Plattformen nutzbar, darunter **Linux**, **macOS** und **Windows** (über das **Windows Subsystem for Linux (WSL)**). "
            "Diese **Interoperabilität** hat die GNU Coreutils zu einem **unverzichtbaren Werkzeug** für Systemadministratoren und Entwickler gemacht, die auf verschiedenen Betriebssystemen arbeiten.\n\n"

            "Quelle: GNU Coreutils",
            "GNU Coreutils"
        )

        # Den Knoten hinzufügen und verbinden
        graph.add_new_node_to_graph(yassine_node5)
        yassine_main_node.connect(yassine_node5)

        # Literaturquelle hinzufügen und verbinden
        literature_source_coreutils = NodeSourceBook(
            "GNU Coreutils: A User's Guide",
            "Free Software Foundation",
            "2023",
            "Boston",
            "Free Software Foundation Press",
            "978-1234567890"
        )
        graph.add_new_node_to_graph(literature_source_coreutils)
        yassine_node5.connect(literature_source_coreutils)

        yassine_node6 = NodeKnowledge(
            "### Einführung in GRUB (Grand Unified Bootloader)\n"
            "**GRUB** ist ein im **GNU-Projekt** entwickelter Bootloader, der eine zentrale Rolle beim Starten von Betriebssystemen spielt. "
            "Nach dem **Einschalten eines Computers** ist GRUB das erste Programm, das ausgeführt wird, um das Betriebssystem in den Arbeitsspeicher zu laden. "
            "Dies ermöglicht dem Computer, ordnungsgemäß weiterzuarbeiten. Besonders nützlich ist GRUB bei **Dual-Boot-Setups**, da es die Auswahl zwischen mehreren Betriebssystemen bietet.\n\n"

            "### Funktion eines Bootloaders\n"
            "Ein Bootloader wie GRUB wird benötigt, um den **Kernel eines Betriebssystems** zu laden und die **Systemressourcen** bereitzustellen. "
            "GRUB hebt sich durch seine **Flexibilität** und **Multiboot-Unterstützung** von früheren Bootloadern ab. "
            "Es ermöglicht die Erkennung mehrerer Betriebssysteme wie **Linux**, **Windows** oder sogar **macOS**, und bietet eine **Benutzerauswahl** beim Systemstart.\n\n"

            "### Konfigurierbarkeit und Erweiterungen\n"
            "Ein besonders wichtiges Merkmal von GRUB ist seine **Konfigurierbarkeit**. "
            "Benutzer können **Kernel-Optionen und Parameter** anpassen, um die **Systemleistung zu optimieren**. "
            "Darüber hinaus unterstützt GRUB das **Laden von Kernel-Modulen** und bietet eine **erweiterte Anpassung der Startoptionen**.\n\n"

            "### Open-Source-Philosophie\n"
            "GRUB wird unter der **GNU General Public License (GPL)** veröffentlicht. "
            "Das bedeutet, dass der **Quellcode frei zugänglich und anpassbar** ist. Viele moderne **Linux-Distributionen** setzen GRUB als **Standard-Bootloader** ein, da er eine vielseitige und leistungsstarke Lösung für das Starten von Betriebssystemen bietet.\n\n"

            "Quelle: GNU GRUB",
            "GRUB – Der GNU Bootloader"
        )

        # Den Knoten hinzufügen und verbinden
        graph.add_new_node_to_graph(yassine_node6)
        yassine_main_node.connect(yassine_node6)

        # Literaturquelle hinzufügen und verbinden
        literature_source_grub = NodeSourceBook(
            "GNU GRUB Manual",
            "Free Software Foundation",
            "2024",
            "Boston",
            "FSF Publishing",
            "978-9876543210"
        )
        graph.add_new_node_to_graph(literature_source_grub)
        yassine_node6.connect(literature_source_grub)

        yassine_node7 = NodeKnowledge(
            "### Einführung in die GNU Compiler Collection (GCC)\n"
            "Die **GNU Compiler Collection (GCC)** ist eine Sammlung von **Compilern** für verschiedene **Programmiersprachen**, "
            "darunter **C**, **C++**, **Fortran**, **Ada**, **Go** und **D**. "
            "GCC ist eines der bedeutendsten Werkzeuge im **GNU-Projekt** und wird weltweit in der Softwareentwicklung eingesetzt. "
            "Es ermöglicht es, **Quellcode in Maschinensprache** zu übersetzen, die von einem Computer verstanden und ausgeführt werden kann. "
            "GCC spielt eine zentrale Rolle bei der Erstellung von Programmen für **Linux** und andere **Unix-ähnliche Betriebssysteme**.\n\n"

            "### Ursprung und Lizenzierung\n"
            "GCC wurde ursprünglich von **Richard Stallman** und dem **GNU-Projekt** entwickelt, "
            "um **freie Software** zu fördern und den Zugang zu **leistungsfähigen Entwicklungstools** zu erleichtern. "
            "Der Compiler ist unter der **GNU General Public License (GPL)** lizenziert, was bedeutet, dass er **kostenlos verwendet, verändert und weitergegeben** werden kann. "
            "Dies hat dazu beigetragen, dass GCC zu einem der **am weitesten verbreiteten Compiler** weltweit geworden ist.\n\n"

            "### Portabilität und Optimierung\n"
            "Ein bemerkenswertes Merkmal von GCC ist seine **Portabilität**. "
            "Der Compiler unterstützt eine Vielzahl von **Plattformen und Prozessorarchitekturen**, "
            "einschließlich **x86**, **ARM** und **PowerPC**. "
            "Diese **Vielseitigkeit** macht ihn zu einer bevorzugten Wahl für Entwickler, die **Software für unterschiedliche Systeme** erstellen möchten. "
            "Zudem ist GCC für seine **Optimierungsfähigkeiten** bekannt, da er in der Lage ist, den **Code zu optimieren** "
            "und so die **Leistung der Programme** zu steigern.\n\n"

            "### Bedeutung für die freie Software-Bewegung\n"
            "GCC hat sich als ein **fundamentales Werkzeug für die freie Software-Bewegung** etabliert, "
            "da er eine **offene, standardisierte Methode** bietet, um **Software für verschiedenste Plattformen** zu entwickeln.\n\n"
            "Quelle: GNU GCC",
            "GCC (GNU Compiler Collection)"
        )

        # Den Knoten hinzufügen und verbinden
        graph.add_new_node_to_graph(yassine_node7)
        yassine_main_node.connect(yassine_node7)

        yassine_node8 = NodeKnowledge(
            "### Einführung in den GNU Debugger (GDB)\n"
            "Der **GNU Debugger (GDB)** ist ein weit verbreitetes **Debugging-Tool**, das Entwicklern hilft, **Fehler in ihren Programmen** zu finden und zu beheben. "
            "GDB ist ein **unverzichtbares Werkzeug** für die Softwareentwicklung und ermöglicht es, **Programmlogik zu überprüfen**, "
            "indem es **Schritt-für-Schritt durch den Quellcode** geht, den **aktuellen Zustand des Programms** anzeigt und die **Ausführung stoppt**, wenn ein Fehler auftritt.\n\n"

            "### Funktionen und Möglichkeiten\n"
            "Mit **GDB** können Entwickler nicht nur den **Ablauf eines Programms überwachen**, sondern auch:\n"
            "- **Variablen inspizieren**\n"
            "- **Speicher-Zugriffe nachverfolgen**\n"
            "- Die **Programmausführung zu bestimmten Punkten** im Code anhalten\n\n"
            "GDB bietet eine **tiefgehende Analyse** und **Fehlerbehebung**, indem es **detaillierte Informationen** darüber liefert, "
            "was im Programm **während der Ausführung** passiert.\n\n"

            "### Unterstützung mehrerer Programmiersprachen\n"
            "GDB unterstützt **verschiedene Programmiersprachen**, darunter **C**, **C++**, **Fortran** und **Ada**. "
            "Es kann sowohl mit **lokalen** als auch mit **Remote-Programmen** verwendet werden. "
            "Die **Befehlszeilen-basierte Benutzeroberfläche** ermöglicht es Entwicklern, flexibel und effizient mit dem Tool zu interagieren, "
            "obwohl es auch **grafische Frontends** gibt, die die Bedienung erleichtern.\n\n"

            "### Integration mit anderen GNU-Tools\n"
            "Ein besonderes Highlight von GDB ist seine **Integration mit anderen GNU-Tools** wie **GCC**. "
            "Da GDB und GCC beide Teil des **GNU-Projekts** sind, arbeiten sie **nahtlos zusammen** und bieten Entwicklern eine vollständige **Werkzeugkette** "
            "für die **Entwicklung und Fehlerbehebung** von Software.\n\n"
            "Quelle: GNU GDB",
            "GDB (GNU Debugger)"
        )

        # Den Knoten hinzufügen und verbinden
        graph.add_new_node_to_graph(yassine_node8)
        yassine_main_node.connect(yassine_node8)

        yassine_node9 = NodeKnowledge(
            "### Einführung in Emacs\n"
            "**Emacs** ist ein leistungsstarker und anpassbarer **Texteditor**, der Teil des **GNU-Projekts** ist. "
            "Er wird oft als **Editor für Entwickler** bezeichnet, da er nicht nur für die **Textbearbeitung**, sondern auch für eine Vielzahl anderer Aufgaben wie **Programmieren**, **Dokumentation schreiben** und **E-Mails verwalten** genutzt wird. "
            "Emacs wurde ursprünglich von **Richard Stallman** entwickelt und hat sich zu einem der **vielseitigsten** und **funktionsreichsten Texteditoren** entwickelt.\n\n"

            "### Erweiterbarkeit und Anpassung\n"
            "Ein herausragendes Merkmal von **Emacs** ist seine **Erweiterbarkeit**. Benutzer können Emacs mit **Lisp**, einer Programmiersprache, die in Emacs eingebaut ist, erweitern und anpassen. "
            "Dies ermöglicht es den Nutzern, ihren **Arbeitsablauf zu personalisieren** und den Editor an ihre Bedürfnisse anzupassen. Emacs bietet **Modi für eine Vielzahl von Programmiersprachen** wie **C**, **Python**, **Ruby** und viele mehr, "
            "wodurch er zu einem bevorzugten Werkzeug für Entwickler wird.\n\n"

            "### Funktionen und Vielseitigkeit\n"
            "**Emacs** ist bekannt für seine leistungsstarken **Such-** und **Ersetzungsfunktionen**, die es den Nutzern ermöglichen, effizient in großen **Codebasen** zu arbeiten. "
            "Es unterstützt auch Funktionen wie **Version Control**, **Projektverwaltung** und sogar **E-Mail- und Kalenderfunktionen**, was es zu einem vielseitigen Werkzeug für Entwickler und Systemadministratoren macht.\n\n"

            "### Plattformübergreifende Verfügbarkeit\n"
            "Ein weiterer Vorteil von **Emacs** ist seine **plattformübergreifende Verfügbarkeit**. Der Texteditor kann auf verschiedenen Betriebssystemen wie **Linux**, **macOS** und **Windows** verwendet werden. "
            "Dies hat dazu beigetragen, dass Emacs von einer breiten und engagierten **Community von Nutzern** unterstützt wird, die regelmäßig **Plugins** und **Erweiterungen** entwickeln, um die Funktionalität des Editors zu verbessern.\n\n"
            "Quelle: GNU Emacs",
            "Emacs – Der GNU Texteditor"
        )

        # Den Knoten hinzufügen und verbinden
        graph.add_new_node_to_graph(yassine_node9)
        yassine_main_node.connect(yassine_node9)

        yassine_node10 = NodeKnowledge(
            "### Einführung in Nano\n"
            "**Nano** ist ein einfacher, benutzerfreundlicher **Texteditor**, der speziell für die **Kommandozeile** entwickelt wurde. "
            "Er wird häufig in **Linux-** und **Unix-Systemen** verwendet und ist besonders für **Einsteiger** geeignet, die nicht mit den komplexeren Funktionen von Editoren wie **Emacs** oder **Vim** vertraut sind. "
            "Nano hat eine einfache und übersichtliche **Benutzeroberfläche**, die es Nutzern ermöglicht, schnell und effizient **Textdateien** zu bearbeiten.\n\n"

            "### Praktische Funktionen von Nano\n"
            "Ein besonders praktisches Merkmal von **Nano** ist, dass es alle grundlegenden Funktionen wie **Textbearbeitung**, **Suchen und Ersetzen** sowie **Speichern** und **Laden von Dateien** direkt in der Kommandozeile bietet. "
            "Nano ist jedoch nicht nur auf einfache Textbearbeitung beschränkt – es bietet auch **Hotkeys** und **Befehlslisten**, die das Arbeiten mit dem Editor erleichtern.\n\n"

            "### Verfügbarkeit und Benutzerfreundlichkeit\n"
            "**Nano** ist in fast allen **Linux-Distributionen** vorinstalliert und steht auch für andere **Unix-ähnliche Betriebssysteme** zur Verfügung. "
            "Durch seine Einfachheit und **Benutzerfreundlichkeit** hat **Nano** eine breite Nutzerbasis und wird sowohl von Anfängern als auch von erfahrenen Nutzern geschätzt, "
            "die schnell Änderungen an **Konfigurationsdateien** oder **Scripts** vornehmen möchten.\n\n"

            "### Ressourcenschonung\n"
            "Ein weiterer Vorteil von **Nano** ist seine **Ressourcenschonung**. Der Editor benötigt nur sehr wenig **Speicher** und **Rechenleistung**, was ihn ideal für den Einsatz auf **Servern** oder in ressourcenbeschränkten Umgebungen macht.\n\n"
            "Quelle: Nano Editor",
            "Nano – Ein einfacher Texteditor für die Kommandozeile"
        )

        # Den Knoten hinzufügen und verbinden
        graph.add_new_node_to_graph(yassine_node10)
        yassine_main_node.connect(yassine_node10)

        yassine_node11 = NodeKnowledge(
            "### Einführung in Make\n"
            "**Make** ist ein weit verbreitetes **Build-Tool**, das ursprünglich von **Stuart Feldman** entwickelt wurde, um die **Automatisierung von Software-Bauprozessen** zu ermöglichen. "
            "Es wird verwendet, um den **Kompilierungsprozess** von Programmen zu verwalten, insbesondere in **großen Projekten** mit vielen **Abhängigkeiten**. "
            "Make analysiert die Quellcodedateien, prüft, welche Dateien geändert wurden, und baut nur die betroffenen Teile des Programms neu. Dies spart **Zeit** und **Ressourcen**, da nicht das gesamte Projekt jedes Mal neu kompiliert werden muss.\n\n"

            "### Funktionsweise von Make\n"
            "**Make** funktioniert mit sogenannten **Makefiles**, die eine Rezept-ähnliche Beschreibung der **Build-Prozesse** enthalten. "
            "Diese **Makefiles** definieren, welche Dateien in welchem Schritt des **Kompilierungsprozesses** verwendet werden, und geben an, wie das Ziel (z. B. die ausführbare Datei) erstellt wird. "
            "Eine typische **Makefile-Anweisung** könnte beispielsweise die **Kompilierung einer C-Datei** zu einer Objektdatei und anschließend die **Linkung dieser Objektdateien** zu einem Programm umfassen.\n\n"

            "### Plattformunabhängigkeit von Make\n"
            "Ein weiterer Vorteil von **Make** ist seine **Plattformunabhängigkeit**. Obwohl Make ursprünglich für **Unix-Systeme** entwickelt wurde, "
            "ist es auch auf vielen anderen Plattformen verfügbar, einschließlich **Windows** (meistens über **Cygwin** oder **WSL**). "
            "Make wird häufig zusammen mit anderen Tools wie **GCC** (GNU Compiler Collection) und **GDB** (GNU Debugger) verwendet, um eine vollständige Entwicklungsumgebung zu schaffen.\n\n"

            "### Bedeutung von Make in der Softwareentwicklung\n"
            "Die Verwendung von **Make** fördert **wiederholbare**, **konsistente Builds** und sorgt dafür, dass **Softwareentwicklungsprozesse** effizient und organisiert bleiben. "
            "Make ist besonders in **Open-Source-Projekten** und in der **Softwareentwicklung** im Allgemeinen von großer Bedeutung.\n\n"
            "Quelle: GNU Make",
            "Make – Ein Werkzeug zur Automatisierung von Kompilierungsprozessen"
        )

        # Den Knoten hinzufügen und verbinden
        graph.add_new_node_to_graph(yassine_node11)
        yassine_main_node.connect(yassine_node11)

        yassine_node12 = NodeKnowledge(
            "### Einführung in GPG (GNU Privacy Guard)\n"
            "**GPG** (GNU Privacy Guard) ist ein Programm, das zur **Verschlüsselung** und **digitalen Signierung** von Daten verwendet wird. "
            "Es ermöglicht es, Daten sicher zu übertragen und die **Identität des Absenders** zu verifizieren, ohne dass Dritte auf die Informationen zugreifen können. "
            "GPG ist vollständig kompatibel mit **OpenPGP** und wird weltweit verwendet, um **E-Mails**, **Dateien** und andere Daten zu schützen.\n\n"

            "### Asymmetrische Kryptografie\n"
            "GPG nutzt **asymmetrische Kryptografie**, bei der es **zwei Schlüssel** gibt: einen **öffentlichen** und einen **privaten Schlüssel**. "
            "Der öffentliche Schlüssel wird an andere weitergegeben, während der private Schlüssel geheim bleibt. "
            "Wenn jemand eine Nachricht an den Besitzer des öffentlichen Schlüssels sendet, wird die Nachricht mit diesem Schlüssel verschlüsselt, "
            "sodass nur der Besitzer des privaten Schlüssels sie entschlüsseln kann. "
            "Auf der anderen Seite kann der private Schlüssel verwendet werden, um Nachrichten zu **signieren**, sodass der Empfänger sicher sein kann, "
            "dass die Nachricht vom Besitzer des privaten Schlüssels stammt.\n\n"

            "### Verwendung von GPG\n"
            "**GPG** ist ein integraler Bestandteil der freien Software-Bewegung und wird von Entwicklern und Aktivisten verwendet, um **private Kommunikation** zu gewährleisten. "
            "Es ist in zahlreichen **E-Mail-Clients** integriert, darunter **Thunderbird** und **KMail**, und wird häufig in der **Softwareverteilung** eingesetzt, "
            "um sicherzustellen, dass die heruntergeladenen Dateien nicht manipuliert wurden.\n\n"

            "### Sicherheit und Schutz\n"
            "GPG bietet eine hohe **Sicherheit**, da es auf gut etablierten mathematischen Prinzipien basiert, die es Dritten nahezu unmöglich machen, verschlüsselte Nachrichten "
            "zu entschlüsseln, ohne den privaten Schlüssel zu besitzen. Durch die Verwendung von GPG können Benutzer sicherstellen, dass ihre Daten nicht nur während der "
            "Übertragung, sondern auch im Ruhezustand geschützt sind.\n\n"

            "Quelle: GPG",
            "GPG (GNU Privacy Guard) – Verschlüsselung und digitale Signatur"
        )

        # Den Knoten hinzufügen und verbinden
        graph.add_new_node_to_graph(yassine_node12)
        yassine_main_node.connect(yassine_node12)

        yassine_node13 = NodeKnowledge(
            "### Einführung in GNU TLS (Transport Layer Security)\n"
            "**GNU TLS** ist eine **Open-Source-Bibliothek**, die sicherstellt, dass **Datenkommunikation über Netzwerke verschlüsselt** und abgesichert wird. "
            "Die Bibliothek wird verwendet, um die **Sicherheit von Internetverbindungen** zu gewährleisten und den Schutz der übertragenen Daten vor **Abhören** oder **Manipulation** zu ermöglichen. "
            "Es implementiert die **TLS-Protokolle**, die auch in **HTTPS-Verbindungen** verwendet werden, um Daten zwischen **Webbrowsern** und **Webservern** sicher zu übertragen.\n\n"

            "### Sicherheitsfunktionen und Algorithmen\n"
            "**GNU TLS** bietet eine umfassende Implementierung der **TLS-Protokolle** und ist mit einer Vielzahl von **kryptografischen Algorithmen** ausgestattet, "
            "darunter **AES** (Advanced Encryption Standard), **RSA** (Rivest–Shamir–Adleman) und **SHA** (Secure Hash Algorithm). "
            "Dies stellt sicher, dass **Datenintegrität** und **Vertraulichkeit** während der Übertragung gewährleistet sind. "
            "GNU TLS wird häufig in Anwendungen verwendet, die eine **sichere Kommunikation** benötigen, wie zum Beispiel **Webserver**, **E-Mail-Clients** und **VPNs**.\n\n"

            "### Vielseitigkeit und Kompatibilität\n"
            "Ein wichtiger Aspekt von **GNU TLS** ist seine **Kompatibilität mit verschiedenen Programmiersprachen**, einschließlich **C**, **C++** und **Python**. "
            "Diese Vielseitigkeit ermöglicht es Entwicklern, die Bibliothek in einer breiten Palette von Anwendungen zu verwenden, ohne sich Gedanken über die Komplexität der Sicherheitsimplementierungen machen zu müssen.\n\n"

            "### Lizenz und Open-Source-Charakter\n"
            "**GNU TLS** wird unter der **GNU General Public License (GPL)** veröffentlicht, was bedeutet, dass es kostenlos genutzt und weitergegeben werden kann. "
            "Dies hat dazu beigetragen, dass die Bibliothek zu einer bevorzugten Wahl für die Implementierung sicherer Verbindungen in **Open-Source-Projekten** geworden ist.\n\n"

            "Quelle: GNU TLS",
            "GNU TLS – Bibliothek für sichere Netzverbindungen"
        )

        # Den Knoten hinzufügen und verbinden
        graph.add_new_node_to_graph(yassine_node13)
        yassine_main_node.connect(yassine_node13)

        yassine_node14 = NodeKnowledge(
            "### Wget – Tool zum Herunterladen von Dateien aus dem Internet\n"
            "**Wget** ist ein leistungsstarkes Tool zum **Herunterladen von Dateien aus dem Internet**. "
            "Es unterstützt eine Vielzahl von **Protokollen**, darunter **HTTP**, **HTTPS** und **FTP**, und ermöglicht es Benutzern, ganze Webseiten, Einzeldateien oder sogar ganze Verzeichnisse herunterzuladen. "
            "Wget ist ein **Kommandozeilen-basiertes Tool**, was es ideal für den Einsatz auf **Servern** oder in **automatisierten Skripten** macht.\n\n"

            "### Vorteile und Funktionen von Wget\n"
            "Ein bemerkenswerter Vorteil von **Wget** ist seine Fähigkeit, **Downloads bei unterbrochener Verbindung fortzusetzen**. "
            "Sollte die Verbindung während eines Downloads unterbrochen werden, kann Wget den Download automatisch wieder aufnehmen, ohne dass der Benutzer den gesamten Download erneut starten muss. "
            "Dies ist besonders nützlich bei **großen Dateien** oder bei Downloads von **langsamen oder instabilen Internetverbindungen**.\n\n"

            "Wget kann auch in **Batch-Prozessen** verwendet werden, um mehrere Dateien auf einmal herunterzuladen. "
            "Mit seiner **rekursiven Download-Funktion** können Benutzer ganze Websites herunterladen, einschließlich aller Seiten und Ressourcen wie Bilder, Stylesheets und Skripte. "
            "Dies ist besonders nützlich für **Webcrawler** oder beim Erstellen von **Offline-Versionen von Websites**.\n\n"

            "### Lizenz und Verfügbarkeit\n"
            "**Wget** ist Teil des **GNU-Projekts** und wird unter der **GNU General Public License (GPL)** lizenziert. "
            "Es ist auf den meisten **Unix-ähnlichen Betriebssystemen** vorinstalliert und kann auch auf **Windows** über **Cygwin** oder **WSL** verwendet werden.\n\n"

            "Quelle: Wget",
            "Wget – Tool zum Herunterladen von Dateien aus dem Internet"
        )

        # Den Knoten hinzufügen und verbinden
        graph.add_new_node_to_graph(yassine_node14)
        yassine_main_node.connect(yassine_node14)

        yassine_node15 = NodeKnowledge(
            "### GNU Octave: Eine Open-Source-Alternative zu MATLAB für numerische Berechnungen\n"
            "GNU Octave ist eine freie Software, die als Open-Source-Alternative zu MATLAB dient. "
            "Es wird häufig für numerische Berechnungen verwendet und bietet eine umfangreiche Sammlung von Funktionen, die in vielen wissenschaftlichen und technischen Bereichen wie Ingenieurwissenschaften, Mathematik und Physik Anwendung finden. "
            "Octave verwendet eine eigene Programmiersprache, die MATLAB sehr ähnlich ist, sodass viele MATLAB-Skripte ohne Änderungen in Octave ausgeführt werden können.\n"
            "\n"
            "### Funktionen und Einsatzmöglichkeiten\n"
            "Octave unterstützt eine Vielzahl von mathematischen Operationen, einschließlich linearer Algebra, Optimierung, Differentialgleichungen und Fourier-Transformationen. "
            "Durch seine interpretierten Funktionen und die hohe Flexibilität ist es ein bevorzugtes Werkzeug für Forscher und Entwickler, die schnelle Berechnungen durchführen und Visualisierungen erstellen möchten.\n"
            "\n"
            "### Vorteile von GNU Octave\n"
            "Ein wichtiger Aspekt von Octave ist, dass es kostenlos und Open Source ist. Dies bedeutet, dass es ohne Lizenzgebühren genutzt werden kann, was besonders für Studenten und kleine Unternehmen von Vorteil ist. "
            "Es hat auch eine aktive Entwicklergemeinschaft, die regelmäßig neue Funktionen hinzufügt und die Software kontinuierlich verbessert.\n"
            "\n"
            "### Erweiterbarkeit und Pakete\n"
            "Octave wird durch zahlreiche Pakete erweitert, die zusätzliche Funktionen bieten, darunter Signalverarbeitung, Optimierung und Statistik. "
            "Diese Pakete können einfach installiert und verwendet werden, um die Fähigkeiten von Octave zu erweitern. Octave bietet auch eine interaktive Konsole, in der Benutzer ihre Berechnungen direkt ausführen und Ergebnisse sofort sehen können.\n"
            "\n"
            "### Fazit und Einsatzgebiete\n"
            "Dank seiner offenen Lizenz und der großen Benutzerbasis wird Octave zunehmend in akademischen und industriellen Anwendungen eingesetzt und bleibt eine wichtige Ressource für alle, die auf der Suche nach einer leistungsstarken, kostengünstigen Lösung für numerische Berechnungen sind.\n"
            "Quelle: Octave",
            "Octave – Eine Open-Source-Alternative zu MATLAB für numerische Berechnungen"
        )

        # Die Knoten einzufügen und zu verbinden
        graph.add_new_node_to_graph(yassine_node15)  # Die Knoten einzufügen
        yassine_main_node.connect(yassine_node15)  # Die Knote 1 mit der Thema-Knoten zu verbinden

        yassine_node16 = NodeKnowledge(
            "GNU Chess ist ein Open-Source-Schachprogramm, das im Rahmen des GNU-Projekts entwickelt wurde. "
            "Es ist ein vollständiges Schachprogramm, das sowohl als Spieler gegen den Computer als auch als Schach-Engine verwendet werden kann. "
            "GNU Chess verwendet einen Algorithmus, um Schachpartien zu spielen, und bietet eine hohe Spielstärke, die es sowohl für Anfänger als auch für erfahrene Spieler interessant macht.\n"
            "\nDas Programm basiert auf einem klassischen Schach-Algorithmus, der auf Minimax und Alpha-Beta-Suche basiert, um die besten Züge zu berechnen. "
            "Im Wesentlichen wird die Stellung auf dem Schachbrett analysiert, und das Programm bewertet verschiedene mögliche Züge, um den besten Zug auszuwählen. "
            "Diese Art von Berechnungen erfolgt in verschiedenen Ebenen von Voraussicht und Komplexität.\n"
            "\nGNU Chess kann auf vielen Plattformen ausgeführt werden, darunter Linux, Windows und macOS, und bietet eine benutzerfreundliche Kommandozeilenoberfläche. "
            "Es kann auch in andere Schachprogramme integriert werden, um als Engine zu fungieren, die Partien gegen andere Computerprogramme oder Online-Spieler spielt.\n"
            "\n### Vorteile von GNU Chess\n"
            "Ein bemerkenswerter Vorteil von GNU Chess ist seine Freiheit und Flexibilität. "
            "Als Teil des GNU-Projekts ist es unter der GNU General Public License (GPL) veröffentlicht, was bedeutet, dass es kostenlos genutzt, verändert und verbreitet werden kann. "
            "Dies hat dazu beigetragen, dass es zu einem wichtigen Werkzeug für die Entwicklung von Schachsoftware und -anwendungen geworden ist.\n"
            "\nGNU Chess ist auch in der Lage, FEN (Forsyth-Edwards Notation) zu verarbeiten, was es ermöglicht, Schachstellungen zu speichern und zwischen verschiedenen Schachprogrammen auszutauschen. "
            "Dies hat es zu einer wertvollen Ressource für Schachspieler und Entwickler gemacht, die Schachpartien analysieren und simulieren möchten.\n"
            "Quelle: GNU Chess",
            "GNU Chess – Ein Schachprogramm, das Teil des GNU-Projekts ist"
        )

        # Die Knoten einzufügen und zu verbinden
        graph.add_new_node_to_graph(yassine_node16)  # Die Knoten einzufügen
        yassine_main_node.connect(yassine_node16)  # Die Knote 1 mit der Thema-Knoten zu verbinden

        yassine_node17 = NodeKnowledge(
            "### GNU Hurd: Der Kernel des GNU-Projekts, der den Linux-Kernel ersetzen könnte\n"
            "GNU Hurd ist ein Kernel, der als Teil des GNU-Projekts entwickelt wird. Der Hurd-Kernel ist ein ambitioniertes Projekt, das als Ersatz für den weit verbreiteten Linux-Kernel dienen soll. "
            "Im Gegensatz zu traditionellen Betriebssystem-Kernels, die monolithisch aufgebaut sind, verfolgt Hurd einen Mikrokernel-Ansatz. Dieser Ansatz bedeutet, dass Hurd aus vielen kleinen Servern besteht, die jeweils für bestimmte Aufgaben zuständig sind, anstatt einer zentralen, großen Kernel-Komponente.\n"
            "\n"
            "### Ursprung und Ziel von GNU Hurd\n"
            "Hurd wurde ursprünglich von Richard Stallman und anderen Mitgliedern des GNU-Projekts entworfen, um den GNU-Betriebssystemen eine vollständige Lösung zu bieten. "
            "Im Wesentlichen sollte der Hurd-Kernel die Betriebssystemfunktionen wie Dateioperationen, Speicherverwaltung und Gerätekommunikation übernehmen, während die Anwendungen die Funktionalitäten des Systems über eine klare Schnittstelle nutzen können. "
            "Der Fokus auf den Mikrokernel-Ansatz sollte eine flexible und modulare Architektur bieten, die eine leichtere Erweiterung und Modifikation des Kernels ermöglicht.\n"
            "\n"
            "### Herausforderungen und Status von GNU Hurd\n"
            "Trotz seiner Ambitionen hat das Projekt mit technischen Herausforderungen zu kämpfen, die die Fertigstellung und den breiten Einsatz von Hurd behindert haben. "
            "Insbesondere die Stabilität und die Kompatibilität mit bestehenden Softwarepaketen stellen nach wie vor Probleme dar. Der Hurd-Kernel ist bislang nicht weit verbreitet und wird hauptsächlich von einer kleinen Gruppe von Entwicklern und Enthusiasten genutzt.\n"
            "\n"
            "### Der Weg von Hurd und seine Bedeutung\n"
            "Inzwischen ist der Hurd-Kernel nicht mehr die primäre Wahl für das GNU-Betriebssystem, und der Linux-Kernel ist zum Standardkernel für GNU/Linux-Systeme geworden. "
            "Dennoch bleibt der Hurd-Kernel ein faszinierendes Beispiel für alternative Designphilosophien in der Welt der Betriebssysteme und ein Projekt von großer historischer Bedeutung für das GNU-Projekt.\n"
            "Quelle: GNU Hurd",
            "GNU Hurd – Der Kernel des GNU-Projekts, der den Linux-Kernel ersetzen könnte"
        )

        # Die Knoten einzufügen und zu verbinden
        graph.add_new_node_to_graph(yassine_node17)  # Die Knoten einzufügen
        yassine_main_node.connect(yassine_node17)  # Die Knote 1 mit der Thema-Knoten zu verbinden

        yassine_node18 = NodeKnowledge(
            "### Verwendung von GNU-Software auf vielen Plattformen\n"
            "GNU-Software zeichnet sich nicht nur durch ihre Freiheit und Open-Source-Natur aus, sondern auch durch ihre Plattformübergreifende Verfügbarkeit. "
            "Sie ist auf einer Vielzahl von Betriebssystemen und Hardwareplattformen einsetzbar, was sie zu einer flexiblen Lösung für Entwickler und Benutzer macht. "
            "Besonders hervorzuheben ist, dass GNU-Software auf Linux, macOS und Windows (insbesondere durch die Verwendung von Windows Subsystem for Linux, WSL) problemlos verwendet werden kann.\n"
            "\n"
            "### Verwendung von GNU-Software auf Linux\n"
            "Auf Linux ist die Verwendung von GNU-Software am weitesten verbreitet. Da der Linux-Kernel von GNU-Software unterstützt wird, sind viele der bekanntesten GNU-Tools, wie Bash, GCC und GRUB, direkt in die meisten Linux-Distributionen integriert. "
            "Dadurch wird eine nahtlose Integration von GNU-Software mit dem Betriebssystem ermöglicht.\n"
            "\n"
            "### Nutzung von GNU-Software auf macOS\n"
            "Für Benutzer von macOS ist GNU-Software ebenfalls zugänglich. Viele Tools, die ursprünglich für Linux entwickelt wurden, sind durch Homebrew oder andere Paketmanager auf macOS installierbar. "
            "Tools wie GCC, GNU Coreutils und Emacs bieten die gleiche Funktionalität wie auf Linux und machen das macOS zu einer weiteren Plattform, die von GNU-Software profitiert.\n"
            "\n"
            "### GNU-Software auf Windows\n"
            "Für Windows-Benutzer gibt es mehrere Möglichkeiten, GNU-Software zu nutzen. Eine der populärsten Methoden ist die Verwendung von Windows Subsystem for Linux (WSL), das es ermöglicht, eine vollständige Linux-Umgebung unter Windows auszuführen. "
            "Auf diese Weise können Benutzer GNU-Tools direkt in der Windows-Umgebung verwenden, ohne einen virtuellen Linux-Rechner oder Dual-Boot-System einzurichten. "
            "Alternativ gibt es auch die Möglichkeit, GNU-Software über Cygwin oder MinGW zu installieren, was eine Linux-ähnliche Umgebung auf Windows ermöglicht.\n"
            "\n"
            "### Plattformübergreifende Interoperabilität\n"
            "Die Fähigkeit, GNU-Software auf mehreren Plattformen zu verwenden, erhöht nicht nur die Zugänglichkeit, sondern fördert auch die Verbreitung der Software und trägt zur Kompatibilität zwischen verschiedenen Betriebssystemen bei. "
            "Diese Interoperabilität ist ein wesentlicher Bestandteil der Philosophie von GNU und sorgt dafür, dass Entwickler ihre Tools auf einer Vielzahl von Geräten und Systemen nutzen können, ohne an eine bestimmte Plattform gebunden zu sein.\n"
            "Quelle: GNU Software on Different Platforms",
            "Verwendung von GNU-Software auf vielen Plattformen"
        )

        # Die Knoten einzufügen und zu verbinden
        graph.add_new_node_to_graph(yassine_node18)  # Die Knoten einzufügen
        yassine_main_node.connect(yassine_node18)  # Die Knote 1 mit der Thema-Knoten zu verbinden

        yassine_node19 = NodeKnowledge(
            "### Bedeutung des GNU-Projekts für die Entwicklung der freien Software-Bewegung\n"
            "Das GNU-Projekt ist nicht nur ein technisches Vorhaben, sondern spielt eine grundlegende Rolle in der Entwicklung der freien Software-Bewegung. "
            "Es wurde 1983 von Richard Stallman ins Leben gerufen, um ein freies Betriebssystem zu schaffen, das auf den Prinzipien der Freiheit und Zusammenarbeit basiert. "
            "Die Philosophie des GNU-Projekts hat nicht nur die Softwareentwicklung revolutioniert, sondern auch die ethischen und rechtlichen Rahmenbedingungen für die Nutzung und Verbreitung von Software grundlegend verändert.\n"
            "\n"
            "### Die Vision des GNU-Projekts: Freiheit für Software\n"
            "Der Erfolg des GNU-Projekts basiert auf der Überzeugung, dass Software frei sein sollte, damit jeder sie nutzen, verändern und weiterverbreiten kann. "
            "Dies steht im Gegensatz zu proprietärer Software, bei der der Zugriff auf den Quellcode eingeschränkt ist. GNU verfolgt die Vision einer freien Gesellschaft, in der Software als gemeinsames Gut betrachtet wird und nicht als Eigentum eines Unternehmens oder einer Einzelperson.\n"
            "\n"
            "### Die Entwicklung der GNU General Public License (GPL)\n"
            "Ein wichtiger Beitrag des GNU-Projekts zur freien Software-Bewegung war die Entwicklung der GNU General Public License (GPL). Diese Lizenz gewährleistet, dass alle Software, die unter ihr veröffentlicht wird, frei bleibt. "
            "Die GPL hat als rechtliches Instrument eine massive Auswirkung auf die Softwarebranche gehabt und war der Grundstein für viele erfolgreiche Open-Source-Projekte wie Linux, Apache und MySQL.\n"
            "\n"
            "### Das GNU-Projekt und die globale Bewegung für digitale Freiheit\n"
            "Das GNU-Projekt hat nicht nur die Art und Weise verändert, wie Software entwickelt und genutzt wird, sondern auch eine globale Bewegung für digitale Freiheit ins Leben gerufen. "
            "Organisationen wie die Free Software Foundation (FSF) setzen sich für die Verbreitung freier Software ein und kämpfen gegen die zunehmende Kontrolle von Softwareentwicklungsunternehmen. "
            "In einer Welt, die zunehmend von proprietärer Software dominiert wird, bleibt das GNU-Projekt ein Symbol für die Werte von Freiheit, Zusammenarbeit und Zugänglichkeit.\n"
            "\n"
            "### Einfluss und Inspiration durch das GNU-Projekt\n"
            "Durch die Schaffung von freien Werkzeugen und die Förderung einer offenen Softwarekultur hat das GNU-Projekt unzählige Entwickler inspiriert und die Entwicklung von Open-Source-Software weltweit beeinflusst. "
            "Heute ist GNU ein Synonym für die freie Software-Bewegung, und seine Philosophie lebt in einer Vielzahl von Open-Source-Projekten und -Communities weiter.\n"
            "Quelle: The GNU Project",
            "Bedeutung des GNU-Projekts für die Entwicklung der freien Software-Bewegung"
        )

        # Die Knoten einzufügen und zu verbinden
        graph.add_new_node_to_graph(yassine_node19)  # Die Knoten einzufügen
        yassine_main_node.connect(yassine_node19)  # Die Knote 1 mit der Thema-Knoten zu verbinden

        # Quellen Knoten:
        yassine_quellen_node= NodeKnowledge("Hier sind alle Quellen verhanden", "description") # Eine Knote, mit der alle Quellen verbunden sind
        graph.add_new_node_to_graph(yassine_quellen_node)

        yassine_literature_source1 = NodeSourceBook("Clean Craftsmanship: Disciplines, Standards, and Ethics",
                                                        "Martin, R.C.", "2021", "Boston", "Addison-Wesley Professional",
                                                        "978-0136915713") # Quelle 1
        graph.add_new_node_to_graph(yassine_literature_source1)
        yassine_quellen_node.connect(yassine_literature_source1) # Alle Quellen Knoten müssen mit der Quelle Knote verbunden sein

