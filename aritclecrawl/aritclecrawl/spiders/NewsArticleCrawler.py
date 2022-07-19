import scrapy
from ..read_news_links import get_links, months_dict
from ..et_link_gen import create_file_struct
from ..article_xml import GenerateXml
from ..params import top_level_directory

import re

links_folder = top_level_directory + "/2021/"


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
    start_urls = get_links(2021)
    create_file_struct(2021)

    # start_urls = [
    # "https://economictimes.indiatimes.com/industry/media/entertainment/media/rajinikanths-film-kaala-yet-to-stir-up-fans/articleshow/64487227.cms",
    # "https://economictimes.indiatimes.com//news/sports/south-africa-attack-the-best-in-the-world-rohit-sharma/articleshow/62323170.cms",
    # "https://economictimes.indiatimes.com//news/economy/policy/government-suspects-gst-leakage-via-sme-scheme/articleshow/62322261.cms",
    # "https://economictimes.indiatimes.com/mf/analysis/mirae-asset-emerging-bluechip-fund-consistent-outperformer/articleshow/62334364.cms"
    # ]

    # start_urls = ["https://economictimes.indiatimes.com/mf/analysis/mirae-asset-emerging-bluechip-fund-consistent-outperformer/articleshow/62334364.cms"]

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0'}

        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)

    def parse(self, response, **kwargs):
        id = response.url.split("/")[-1][:-4]

        try:
            dt = response.css('div[data-artitype="ET Free"] time::text').get()
            dt = dt.split(": ")[1].split(", ")
            [month, day] = dt[0].split()
            month = months_dict[str(month)]
            year = dt[1]
            time = dt[2].split(" ", 2)
            timezone = time[-1]
            time = " ".join(time[:2])
            # print(time, timezone)
            title = response.css('div[data-artitype="ET Free"]::attr(data-arttitle)').get()
            synopsis = response.css('div[data-artitype="ET Free"] h2.summary::text').get()
            if synopsis is None:
                synopsis_content = response.css('div[data-artitype="ET Free"] ul.hsummary li::text').getall()
                synopsis = re.sub(' +', ' ', ' '.join([sent.replace('\n', '') for sent in synopsis_content]))
            body_content = response.css('div[data-artitype="ET Free"] div.artText *::text').getall()
            body = re.sub(' +', ' ', ' '.join([sent.replace('\n', '') for sent in body_content]))
            GenerateXml(id, day, month, year, time, timezone, title, synopsis, body)

        except (AttributeError, Exception):
            print("Skip Website")

        # print(title)

# process = CrawlerProcess(settings={
#     "FEEDS": {
#         "items.json": {"format": "json"},
#     },
# })
#
# process.crawl(NewsSpider)
# process.start() # the script will block here until the crawling is finished
