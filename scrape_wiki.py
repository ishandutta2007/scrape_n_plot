import csv
import urllib.request as urllibreq
from bs4 import BeautifulSoup
import re

def RepresentsInt(s):
    try: 
        s = s.replace(',','')
        int(s)
        return True
    except ValueError:
        return False

def RepresentsADYear(s):
    try:
        s = s.replace(',','')
        s = str(s)
        if re.search(r"\d{1}.*(ad|Ad|AD)", s):
            return True
        s = int(s)
        if re.search(r"\d{1}", str(s)):
            return True
        return False
    except ValueError:
        return False

def RepresentsBCYear(s):
    try:
        s = s.replace(',','')
        s = str(s)
        if re.search(r"\d{1}.*(bc|Bc|BC)", s):
            return True
        s = int(s)
        if re.search(r"\d{1}", str(s)):
            return True
        return False
    except ValueError:
        return False

def RepresentsFloat(s):
    try:
        s = s.replace(',','')
        float(s)
        return True
    except ValueError:
        return False

def RepresentsStr(s):
    try: 
        str(s)
        return True
    except ValueError:
        return False

wiki_page = 'https://en.wikipedia.org/wiki/Gross_world_product'
html = urllibreq.urlopen(wiki_page)

tree = BeautifulSoup(html,"lxml")
tables = tree.find_all("table")
print(len(tables))

for i in range(len(tables)):
    outfile = open("table_data" + str(i) + ".csv","w",newline='')
    writer = csv.writer(outfile, delimiter =';')

    table_tag = tree.select("table")[i]
    tab_data = [[item.text for item in row_data.select("th,td")]
                    for row_data in table_tag.select("tr")]

    # print(tab_data)
    for data in tab_data:
        data = list(map(lambda x:x.replace('\n', ''), data))
        data = list(map(lambda x:"-"+(x.replace('bc','').replace('Bc','').replace('BC','')) if RepresentsBCYear(x) else x, data))
        data = list(map(lambda x:x.replace('ad','').replace('Ad','').replace('AD','') if RepresentsADYear(x) else x, data))
        data = list(map(lambda x:float(x.replace(',','')) if RepresentsFloat(x) else x, data))
        writer.writerow(data)
        print(data)

