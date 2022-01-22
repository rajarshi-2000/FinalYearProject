# https://economictimes.indiatimes.com/archivelist/year-2018,month-1,starttime-43101.cms
import os

months = [(31, 'Jan'), (28, 'Feb'), (31, 'Mar'), (30, 'Apr'), (31, 'May'), (30, 'Jun'),
          (31, 'Jul'), (31, 'Aug'), (30, 'Sep'), (31, 'Oct'), (30, 'Nov'), (31, 'Dec')]


def get_links(year):
    starttime = 43101
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
