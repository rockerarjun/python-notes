import csv
import os
import sys
#from urllib2 import urlopen
import requests
import lxml.html as html
from lxml.etree import XPath
from pyquery import PyQuery as pq
#import xrange 

BASE_URL = "http://www.seismonepal.gov.np/file.json"
#BASE_URL = "http://http://www.seismonepal.gov.np/index.php?action=earthquakes&show=recent



def read_url(url):
    """ Read given Url , Returns pq() of page"""
    #html = urlopen(url).read()
    html = requests.get(url).text
    '''
    jf = json.load(html)
    print(jf)
    print(jf['menu']['header'])
    print(jf['menu']['items'][0]['id'])
    print(jf['menu']['items'][5])
    print(jf['menu']['items'][6])
    '''
    return pq(html)


def get_page_rows(page):
    response = read_url(page)
    rows = response.find('div.block2-content table tr') #table.wikitable tr
    print("count >> ", rows.__len__())

    data = list()
    for row in rows.items():
        edate = row.find('td').eq(0).find('span').text()
        etime = row.find('td').eq(1).find('span').text()2
        elatitude = row.find('td').eq(2).find('span').text()
        elongitude = row.find('td').eq(3).find('span').text()
        emagnitude = row.find('td').eq(4).find('span').text()
        epicentre = row.find('td').eq(5).find('span').text().strip()
        if edate:
            data.append([edate, etime, elatitude, elongitude, emagnitude, epicentre])
    return data


def write_csv(mydict):
    with open('earthquake.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in mydict.items():
            if type(value) is not list:
                value = value.encode('utf-8')
                writer.writerow([key, value])


def writeto_csv(mydict):
    with open(os.path.dirname(os.path.abspath(__file__))+'/earthquake.csv', 'w+') as csv_file:
       # writer = csv.DictWriter(csv_file,
        #                        fieldnames=["Date", "Time", "Latitude", "Longitude", "Magnitude", "Epicentre"])
        #writer.writeheader()
        writer = csv.writer(csv_file)
        writer.writerow(('Date', 'Time', 'Latitude', 'Longitude','Magnitude','Epicentre'))
        #writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for data in mydict:
            row=(
                data[0],data[1],data[2],data[3],data[4],data[5])            )
            writer.writerow(row)


if __name__ == '__main__':
    
    pages=[]
    for i in range(1,4):
        url='http://www.seismonepal.gov.np/index.php?action=earthquakes&show=recent&page='+str(i)
        pages.append(url)
    
    

    #pages = ["http://www.seismonepal.gov.np/index.php?action=earthquakes&show=recent&page=%s" % page for page in
             #xrange(1, 3)]
    data = list()
    for page in pages:
        scrape_page = get_page_rows(page)
        print("Finding Page >> ", page)
        data.append(scrape_page)
    print("data:",len(data))
    
    
    writeto_csv(data)
    #writeto_csv(data)
    print('Completed')