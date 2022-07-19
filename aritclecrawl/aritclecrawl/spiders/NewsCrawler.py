# import scrapy
# from ..et_link_gen import get_links
# from ..params import top_level_directory
#
# class NewsSpider(scrapy.Spider):
#     name = "news"
#     start_urls = get_links(2021)
#
#     def start_requests(self):
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0'}
#
#         for url in self.start_urls:
#             yield scrapy.Request(url, headers=headers)
#
#     def parse(self, response, **kwargs):
#         date = response.css('td.contentbox5 b::text')[1].get()
#         [day, month] = date.split(",")[0].split()
#
#         articles = response.css('ul.content a::attr(href)').getall()
#
#         with open(f"{top_level_directory}/2021/{month}/{day}_{month}.txt", "w") as f:
#             for article in articles:
#                 f.write("https://economictimes.indiatimes.com/"+article+"\n")
#
# #
# # process = CrawlerProcess(settings={
# #     "FEEDS": {
# #         "items.json": {"format": "json"},
# #     },
# # })
# #
# # process.crawl(NewsSpider)
# # process.start() # the script will block here until the crawling is finished
#
