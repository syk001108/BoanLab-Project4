#CSV파일 저장 없는 버전
from bs4 import BeautifulSoup
import urllib.request
import time
import random
import csv
import re

def get_soup(target_url):
    html = urllib.request.urlopen(target_url).read()
    time.sleep(random.uniform(2,5))
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def remove_html(sentence):
    sentence.find('h4').decompose()
    p = sentence.find_all('span')
    img = sentence.find_all('img')
    sentence = str(sentence)
    for i in p:
        sentence = sentence.replace(str(i), '')
    for png in img:
        sentence = sentence.replace(str(png), "https://www.algospot.com" + png['src'])
    sentence = sentence.replace('<sup>', '^{')
    sentence = sentence.replace('</sup>', '}')
    sentence = sentence.replace('<sub>', '_{')
    sentence = sentence.replace('</sub>', '}')
    sentence = re.sub('(<([^>]+)>)', '', sentence)
    sentence = sentence.replace('&lt;', '<')
    sentence = sentence.replace('\lt', '<')
    sentence = sentence.replace('&gt;', '>')
    sentence = sentence.replace('\gt', '>')
    sentence = sentence.replace('&le;', '≤')
    sentence = sentence.replace('\le', '≤')
    sentence = sentence.replace('&ge;', '≥')
    sentence = sentence.replace('\ge', '≥')
    sentence = sentence.replace('&Hat;', '^')
    sentence = sentence.replace('&apos;', '`')
    sentence = sentence.replace('&semi;', ';')
    sentence = sentence.replace('&amp;', '&')
    sentence = sentence.replace('&quot;', '"')
    sentence = sentence.replace('&num;', '#')
    sentence = sentence.strip()
    return sentence

def info_data(soup):
    head = soup.find('div', {'class': 'article-container'})
    head2 = head.find('h2')
    name = head2.text.strip()
    lic = soup.find('li', {'class': 'content'})
    lis = lic.find_all('li')
    ID = lis[0].text.strip()
    time = lis[1].text.strip()
    memory = lis[2].text.strip()
    li1 = soup.find('a', {'class': 'username'})
    author = li1.text.strip()
    return(ID, name, time, memory, author)

def problem_data(soup):
    section = soup.find('section', {'class': 'problem_statement'})
    section = remove_html(section)
    return section

def input_data(soup):
    section = soup.find('section', {'class': 'problem_input'})
    section = remove_html(section)
    return section

def output_data(soup):
    section = soup.find('section', {'class': 'problem_output'})
    section = remove_html(section)
    return section

def sample_input_data(soup):
    section = soup.find('section', {'class': 'problem_sample_input'})
    pres = section.find_all('pre')
    input_d = pres[0].text.strip()
    return input_d

def sample_output_data(soup):
    section = soup.find('section', {'class': 'problem_sample_output'})
    pres = section.find_all('pre')
    output_d = pres[0].text.strip()
    return output_d

def extract_data(soup):
    table = soup.find('table', {'class': 'problem_list'})
    trs = table.find_all('tr')
    for idx, tr in enumerate(trs):
        if idx > 0:
            tds = tr.find_all('td')
            target_url = 'https://www.algospot.com/judge/problem/read/'+tds[1].text.strip()
            time.sleep(random.uniform(2,4))
            soup = get_soup(target_url)
            info = info_data(soup)
            problem = problem_data(soup)
            input_d = input_data(soup)
            output_d = output_data(soup)
            sam_in_d = sample_input_data(soup)
            sam_out_d = sample_output_data(soup)

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
