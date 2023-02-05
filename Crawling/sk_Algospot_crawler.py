from bs4 import BeautifulSoup
import urllib.request
import time
import random

def get_soup(target_url):
    html = urllib.request.urlopen(target_url).read()
    time.sleep(random.uniform(2,5))
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def extract_data(soup):
    table = soup.find('table', {'class': 'problem_list'})
    trs = table.find_all('tr')
    for idx, tr in enumerate(trs):
        if idx > 0:
            tds = tr.find_all('td')
            ID = tds[1].text.strip()
            name = tds[2].text.strip()
            writer= tds[3].text.strip()
            submissions = tds[4].text.strip()
            accepted = tds[5].text.strip()
            print(ID, name, writer, submissions, accepted)

for i in range(1, 19):
    target_url = 'https://www.algospot.com/judge/problem/list/{}?order_by=slug'.format(i)
    time.sleep(random.uniform(2,4))
    soup = get_soup(target_url)
    extract_data(soup)
