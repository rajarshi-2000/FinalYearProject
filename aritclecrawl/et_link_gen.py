# https://economictimes.indiatimes.com/archivelist/year-2018,month-1,starttime-43101.cms
import os

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def get_links(year):
    starttime = 43101
    folder = f"E:/FinalYearProject/aritclecrawl/{year}/"
    str_domain = "https://economictimes.indiatimes.com/archivelist/"
    str_end = ".cms"

    links = []
    month = 0

    while month < 12:
        foldername = os.path.join(folder+str(month+1))
        os.makedirs(foldername)
        days = months[month]

        while days > 0:
            links.append(f"{str_domain}year-{year},month-{month + 1},starttime-{starttime}{str_end}")
            starttime = starttime + 1
            days -= 1

        month += 1

    return links


# get_links(2018)
