# https://economictimes.indiatimes.com/archivelist/year-2018,month-1,starttime-43101.cms
import os
from datetime import date
from .params import top_level_directory, main_directory

months_dict = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

# Note: Please change the number of days in Feb for leap year [Dynamic check not implemented]
months = [(31, 'Jan'), (28, 'Feb'), (31, 'Mar'), (30, 'Apr'), (31, 'May'), (30, 'Jun'),
          (31, 'Jul'), (31, 'Aug'), (30, 'Sep'), (31, 'Oct'), (30, 'Nov'), (31, 'Dec')]


def get_links(year):
    """
        Given a year, this function will fetch all the article links for that year
        and store it in a systematic file structure.
        YEAR
         - Mon
           - Day_Month.txt
    """
    d0 = date(2018, 1, 1)
    d1 = date(year, 1, 1)
    starttime = 43101 + (d1-d0).days
    folder = f"{top_level_directory}/{year}/"
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


def create_file_struct(year):
    """
    Creates file structure for getting articles when provided with a directory consisting of the links
    :param year: int denoting the year
    """
    folder = f"{main_directory}/et_articles/{year}"
    month = 0

    while month < 12:
        days = months[month][0]
        monthkey = months[month][1]

        while days > 0:
            day = f"0{days}" if days < 10 else str(days)
            foldername = os.path.join(f"{folder}/{months_dict[monthkey]}/{day}")
            os.makedirs(foldername)
            days -= 1

        month += 1


# create_file_struct(2018)
