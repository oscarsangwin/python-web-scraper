import urllib.request
import urllib.error
from html.parser import HTMLParser
import os
import random
import time

class MyHTMLParser(HTMLParser):

    def __init__(self):
        self.in_title_tag = 0
        super().__init__()
    
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if name == 'href' and value.startswith('http'):
                    if value not in scraped and value not in to_scrape:
                        new_found.append(value)
        elif tag == 'title':
            self.in_title_tag = 1
    
    def handle_data(self, data):
        if self.in_title_tag == 1:
            f.write(f'Head tag: {data} from url: {url}\n')
    
    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title_tag = 0

def clear():
    os.system('clear')

def display_error(e):
    print(f'The url {url} gave an error: {e}')
    input(f'Press enter to skip: ')

parser = MyHTMLParser()

to_scrape = ['https://www.bbc.co.uk/news']
scraped = []

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

with open('scraped.txt', 'w') as f:
    while True:
        clear()
        print('\n- - - WEB SCRAPER - - -')
        print(f'{len(scraped)} urls scraped.')
        print(f'{len(to_scrape)} urls to scrape.')
        
        if len(to_scrape) == 0:
            input('There are no more urls to scrape. Press enter to exit...')
            break
        else:
            print('\nPress enter to scrape a random unscraped url, or type \'x\' then enter to exit...')
            if input('-> ') == 'x':
                break
            else:
                url = random.choice(to_scrape)
                to_scrape.remove(url)
                scraped.append(url)
                print(f'...Scraping: {url}...')
                
                req = urllib.request.Request(url, headers={'User-Agent' : user_agent})

                try:
                    html = urllib.request.urlopen(req).read().decode()
                except urllib.error.HTTPError as e:
                    display_error(e)
                except Exception as e:
                    display_error(e)
                else:
                    new_found = []
                    parser.feed(html)
                    to_scrape.extend(new_found)
                    print(f'Found {len(new_found)} links.')
                    time.sleep(0.5)
