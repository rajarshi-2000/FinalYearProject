import scrapy
from aritclecrawl.et_link_gen import get_links


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

# filename = "E:/FinalYearProject/aritclecrawl/data/CE1.txt"
#
# file = filename[:-4].rpartition('/')[2]
# xml_folder = os.path.join("E:/FinalYearProject/aritclecrawl/extracted/", file + "/xml")
# txt_folder = os.path.join("E:/FinalYearProject/aritclecrawl/extracted/", file + "/txt")
# os.makedirs(xml_folder)
# os.makedirs(txt_folder)

class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = get_links(2018)

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0'}

        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)

    def parse(self, response, **kwargs):
        articles = response.css('ul.content a::attr(href)').getall()
        print(articles)
