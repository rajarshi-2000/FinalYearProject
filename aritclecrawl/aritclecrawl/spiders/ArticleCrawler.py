import scrapy
import json


def readDataFile(path: str) -> list:
    links = []
    with open(path, "r") as readFile:
        while True:
            line = readFile.readline()
            if not line:
                break
            links.append(line[1:])
    return links


class ArticleSpider(scrapy.Spider):
    name = "articles"
    start_urls = readDataFile("./data/cspubsum_ids.txt")

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)

    def parse(self, response, **kwargs):
        yield {
            'title': response.css("span.title-text::text").get(),
            'highlights': response.css("div.author-highlights dl.list dd.list-description p::text").getall(),
            'abstract': response.css("div.author p::text").getall()
        }



