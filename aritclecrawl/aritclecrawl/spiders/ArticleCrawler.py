import scrapy
from scrapy.http import HtmlResponse
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
    start_urls = ["https://www.sciencedirect.com/science/article/pii/S0142694X1500054X"]

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)

    def parse(self, response, **kwargs):
        authors = response.css('a.author').getall()
        author_names = []
        for author in authors:
            html_resp = HtmlResponse(url="author html", body=author, encoding='utf-8')
            author_names.append(html_resp.css('span.content span.given-name::text').get() + ", " +
                                html_resp.css('span.content span.surname::text').get())

        abstracts = response.css('div.author div').getall()
        sub = []
        for abstract in abstracts:
            html_resp = HtmlResponse(url="abstract html", body=abstract, encoding='utf-8')
            point = {
                'heading': html_resp.css('h3::text').get(),
                'content': html_resp.css('p::text').get()
            }
            sub.append(point)

        yield {
            'publication-title': response.css('div.Publication div.publication-volume h2.publication-title a::text').get(),
            'title': response.css('span.title-text::text').get(),
            'authors': author_names,
            'highlights': response.css("div.author-highlights dd.list-description p::text").getall(),
            'abstract': sub,
            'keywords': response.css('div.keyword span::text').getall()
        }