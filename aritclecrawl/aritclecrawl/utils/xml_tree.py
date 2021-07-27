import xml.etree.ElementTree as ET
from xml.dom.minidom import parse


def GenerateXml(filename, title, highlights, abstract):
    root = ET.Element("article")

    title_element = ET.SubElement(root, "title")
    title_element.text = title

    highlights_element = ET.Element("highlights")
    root.append(highlights_element)

    for h in highlights:
        b = ET.SubElement(highlights_element, "highlight")
        b.text = h

    abstract_element = ET.Element("abstract")
    root.append(abstract_element)

    for a in abstract:
        if a["heading"] is None:
            b = ET.SubElement(abstract_element, "content")
            b.text = a["content"]
        else:
            b = ET.SubElement(abstract_element, "heading")
            b.text = a["heading"]
            b = ET.SubElement(abstract_element, "content")
            b.text = a["content"]

    tree = ET.ElementTree(root)

    with open(filename, "wb") as file:
        tree.write(file)

    dom = parse(filename)
    with open(filename, "w") as file:
        file.write(dom.toprettyxml())
