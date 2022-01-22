import scrapy
from ..et_link_gen import get_links
from scrapy.crawler import CrawlerProcess


def readDataFile(path: str) -> list:
    links = []
    with open(path, "r") as readFile:
        while True:
            line = readFile.readline()
            if not line:
                break
            links.append(line[1:])
    return links


class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = get_links(2018)

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0'}

        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)

    def parse(self, response, **kwargs):
        date = response.css('td.contentbox5 b::text')[1].get()
        [day, month] = date.split(",")[0].split()

        articles = response.css('ul.content a::attr(href)').getall()

        with open(f"E:/FinalYearProject/aritclecrawl/2018/{month}/{day}_{month}.txt", "w") as f:
            for article in articles:
                f.write("https://economictimes.indiatimes.com/"+article+"\n")


# process = CrawlerProcess(settings={
#     "FEEDS": {
#         "items.json": {"format": "json"},
#     },
# })
#
# process.crawl(NewsSpider)
# process.start() # the script will block here until the crawling is finished

