import xml.etree.ElementTree as ET


def parse(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    txtfile = filename[:-4] + ".txt"
    with open(txtfile, "w") as file:
        for child in root:
            if child.tag == "title":
                file.write("@&#MAIN-TITLE@&#" + child.text + "\n")
            if child.tag == "highlights":
                file.write("@&#HIGHLIGHTS@&#\n")
                for highlight in child:
                    file.write(f"\t\t\t{highlight.text}\n\n")

            if child.tag == "abstract":
                file.write("@&#ABSTRACT@&#\n")
                for point in child:
                    if point.tag == "heading":
                        file.write(f"@&#{point.text.upper()}@&#\n")
                    else:
                        file.write(point.text.strip() + "\n")

parse("S0897189719301089.xml")
