import os
import scrapy
from scrapy.http import HtmlResponse
from ..utils.xml_tree import GenerateXml
from ..utils.xml_to_txt import parse


def readDataFile(path: str) -> list:
    links = []
    with open(path, "r") as readFile:
        while True:
            line = readFile.readline()
            if not line:
                break
            links.append(line[1:])
    return links


# txt_folder = Path('D:/COLLEGE/FinalYearProject/FinalYearProject/aritclecrawl/data/').rglob('*.txt')
# files = [x for x in txt_folder]

filename = "E:/FinalYearProject/aritclecrawl/data/CE1.txt"

file = filename[:-4].rpartition('/')[2]
xml_folder = os.path.join("E:/FinalYearProject/aritclecrawl/extracted/", file + "/xml")
txt_folder = os.path.join("E:/FinalYearProject/aritclecrawl/extracted/", file + "/txt")
os.makedirs(xml_folder)
os.makedirs(txt_folder)


class ArticleSpider(scrapy.Spider):
    name = "articles"
    start_urls = readDataFile(filename)

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0'}

        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)

    def parse(self, response, **kwargs):
        abstracts = response.css('div.author div').getall()
        sub = []
        for abstract in abstracts:
            html_resp = HtmlResponse(url="abstract html", body=abstract, encoding='utf-8')
            point = {
                'heading': html_resp.css('h3::text').get(),
                'content': html_resp.css('p::text').get()
            }
            sub.append(point)

        highlights = response.css("div.author-highlights dd.list-description p::text").getall()

        xml_filename = os.path.join(xml_folder, response.url.split("/")[-1] + '.xml')

        GenerateXml(xml_filename, response.css('span.title-text::text').get(), highlights, sub)
        parse(xml_filename)
