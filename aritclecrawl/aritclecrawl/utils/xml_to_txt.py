import xml.etree.ElementTree as ET


def parse(filename: str):
    tree = ET.parse(filename)
    root = tree.getroot()

    txtfile = filename.replace("xml", "txt")
    with open(txtfile, "w") as file:
        for child in root:
            if child.tag == "title":
                file.write("@&#MAIN-TITLE@&#" + child.text + "\n")
            if child.tag == "highlights":
                file.write("@&#HIGHLIGHTS@&#\n")
                for highlight in child:
                    file.write(f"\t\t\t{highlight.text}\n\n")

            if child.tag == "abstract":
                file.write("@&#ABSTRACT@&#\n\n")
                for point in child:
                    if point.tag == "content":
                        file.write(point.text.strip() + "\n\n")

