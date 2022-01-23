from .params import top_level_directory

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

months = [(31, 'Jan'), (28, 'Feb'), (31, 'Mar'), (30, 'Apr'), (31, 'May'), (30, 'Jun'),
          (31, 'Jul'), (31, 'Aug'), (30, 'Sep'), (31, 'Oct'), (30, 'Nov'), (31, 'Dec')]


def readDataFile(path: str) -> list:
    links = []
    with open(path, "r") as readFile:
        while True:
            line = readFile.readline()
            if not line:
                break
            links.append(line[:-1])
    return links


def get_links(year):
    links_folder = f"{top_level_directory}/{year}"
    all_links = []
    for (days, month) in months:
        for i in range(1, days + 1):
            filename = f"{links_folder}/{month}/{i}_{month}.txt"
            links = readDataFile(filename)
            all_links.extend(links)

    return all_links
