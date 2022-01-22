import scrapy
from ..read_news_links import get_links
from ..article_xml import GenerateXml

import re
links_folder = "E:/FinalYearProject/aritclecrawl/2018/"


def readDataFile(path: str) -> list:
    links = []
    with open(path, "r") as readFile:
        while True:
            line = readFile.readline()
            if not line:
                break
            links.append(line)
    return links


class NewsArticleSpider(scrapy.Spider):
    name = "news_article"
    start_urls = get_links(2018)

    # start_urls = ["https://economictimes.indiatimes.com/industry/media/entertainment/media/rajinikanths-film-kaala-yet-to-stir-up-fans/articleshow/64487227.cms"]

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0'}

        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)

    def parse(self, response, **kwargs):
        id = response.url.split("/")[-1][:-4]
        dt = response.css('div[data-artitype="ET Free"] time::text').get()
        dt = dt.split(": ")[1].split(", ")
        [month, day] = dt[0].split()
        year = dt[1]

        title = response.css('div[data-artitype="ET Free"] h1::text').get()
        synopsis = response.css('div[data-artitype="ET Free"] h2.summary::text').get()
        body_content = response.css('div[data-artitype="ET Free"] div.artText::text').getall()
        body = re.sub(' +', ' ', ' '.join([sent.replace('\n', '') for sent in body_content]))

        GenerateXml(id, day, month, year, title, synopsis, body)

# process = CrawlerProcess(settings={
#     "FEEDS": {
#         "items.json": {"format": "json"},
#     },
# })
#
# process.crawl(NewsSpider)
# process.start() # the script will block here until the crawling is finished

