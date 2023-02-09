from bs4 import BeautifulSoup
import urllib.request
import time
import random
import csv

def get_soup(target_url):
    html = urllib.request.urlopen(target_url).read()
    time.sleep(random.uniform(2,5))
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def info_data(soup):
    head = soup.find('div', {'class': 'article-container'})
    head2 = head.find('h2')
    name = head2.text.strip()
    lic = soup.find('li', {'class': 'content'})
    lis = lic.find_all('li')
    ID = lis[0].text.strip()
    time = lis[1].text.strip()
    memory = lis[2].text.strip()
    submissions = lis[3].text.strip()
    accepted = lis[4].text.strip()
    li1 = soup.find('a', {'class': 'username'})
    author = li1.text.strip()
    li2 = lic.find('li', {'class': 'source'})
    li2s = li2.find('a')
    source = li2s.text.strip()
    print(ID, name, time, memory, submissions, accepted, author, source)

def problem_data(soup):
    section = soup.find('section', {'class': 'problem_sample_input'})
    print(section)

def input_data(soup):
    section = soup.find('section', {'class': 'problem_statement'})
    print(section)

def output_data(soup):
    section = soup.find('section', {'class': 'problem_input'})
    print(section)

def sample_input_data(soup):
    section = soup.find('section', {'class': 'problem_output'})
    pres = section.find_all('pre')
    input = pres[0].text.strip()
    print(input)

def sample_output_data(soup):
    section = soup.find('section', {'class': 'problem_sample_output'})
    pres = section.find_all('pre')
    input = pres[0].text.strip()
    print(input)

def extract_data(soup):
    table = soup.find('table', {'class': 'problem_list'})
    trs = table.find_all('tr')
    for idx, tr in enumerate(trs):
        if idx > 0:
            tds = tr.find_all('td')
            target_url = 'https://www.algospot.com/judge/problem/read/'+tds[1].text.strip()
            time.sleep(random.uniform(2,4))
            soup = get_soup(target_url)
            info_data(soup)
            problem_data(soup)
            input_data(soup)
            output_data(soup)
            sample_input_data(soup)
            sample_output_data(soup)

target_url = 'https://www.algospot.com/judge/problem/list/1'
soup = get_soup(target_url)
span = soup.find('span', {'class': 'step-links'})
a1 = span.find_all('a')
pg_num = int(a1[6].text.strip())+1
for i in range(1, pg_num):
    target_url = 'https://www.algospot.com/judge/problem/list/{}?order_by=slug'.format(i)
    time.sleep(random.uniform(2,4))
    soup = get_soup(target_url)
    extract_data(soup)
