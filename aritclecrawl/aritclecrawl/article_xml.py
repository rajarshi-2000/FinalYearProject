import xml.etree.ElementTree as ET
from xml.dom.minidom import parse
from .params import main_directory


def GenerateXml(id, day, month, year, time, timezone, title, synopsis, body):
    root = ET.Element("article")

    id_element = ET.SubElement(root, "Unique_article_id")
    id_element.text = id.encode("ascii", "ignore").decode()

    day_element = ET.SubElement(root, "day")
    day_element.text = day.encode("ascii", "ignore").decode()

    month_element = ET.SubElement(root, "month")
    month_element.text = month.encode("ascii", "ignore").decode()

    year_element = ET.SubElement(root, "year")
    year_element.text = year.encode("ascii", "ignore").decode()

    time_element = ET.SubElement(root, "time")
    time_element.text = time.encode("ascii", "ignore").decode()

    timezone_element = ET.SubElement(root, "timezone")
    timezone_element.text = timezone.encode("ascii", "ignore").decode()

    title_element = ET.SubElement(root, "title")
    title_element.text = title.encode("ascii", "ignore").decode()

    synopsis_element = ET.SubElement(root, "synopsis")
    synopsis_element.text = synopsis.encode("ascii", "ignore").decode()

    body_element = ET.SubElement(root, "body")
    body_element.text = body.encode("ascii", "ignore").decode()

    tree = ET.ElementTree(root)

    filename = f"{main_directory}/et_articles/{year}/{month}/{day}/{id}.xml"
    with open(filename, "wb") as file:
        tree.write(file)

    dom = parse(filename)
    with open(filename, "w") as file:
        file.write(dom.toprettyxml())
