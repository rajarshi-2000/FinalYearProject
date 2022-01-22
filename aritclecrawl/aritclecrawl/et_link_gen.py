# https://economictimes.indiatimes.com/archivelist/year-2018,month-1,starttime-43101.cms
import os
from datetime import date
months = [(31, 'Jan'), (28, 'Feb'), (31, 'Mar'), (30, 'Apr'), (31, 'May'), (30, 'Jun'),
          (31, 'Jul'), (31, 'Aug'), (30, 'Sep'), (31, 'Oct'), (30, 'Nov'), (31, 'Dec')]


def get_links(year):
    d0 = date(2018, 1, 1)
    d1 = date(year, 1, 1)
    starttime = 43101 + (d1-d0).days
    folder = f"E:/FinalYearProject/aritclecrawl/{year}/"
    str_domain = "https://economictimes.indiatimes.com/archivelist/"
    str_end = ".cms"

    links = []
    month = 0

    while month < 12:
        days = months[month][0]
        monthkey = months[month][1]
        foldername = os.path.join(folder+monthkey)
        os.makedirs(foldername)

        while days > 0:
            links.append(f"{str_domain}year-{year},month-{month + 1},starttime-{starttime}{str_end}")
            starttime = starttime + 1
            days -= 1

        month += 1

    return links
