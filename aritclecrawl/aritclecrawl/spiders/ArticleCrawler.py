import scrapy


class ArticleSpider(scrapy.Spider):
    name = "articles"
    start_urls = ["http://www.sciencedirect.com/science/article/pii/S0003687013000549",
                  "http://www.sciencedirect.com/science/article/pii/S0003687013000550"]

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)

    def parse(self, response, **kwargs):
        yield {
            'title': response.css("span.title-text::text").get(),
            'highlights': response.css("div.author-highlights dl.list dd.list-description p::text").getall(),
            'abstract': response.css("div.author p::text").get()
        }