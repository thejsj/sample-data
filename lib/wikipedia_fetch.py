from bs4 import BeautifulSoup
import urllib
import json
import os

def get_page(url):
    return BeautifulSoup(urllib.urlopen(url))

def get_page_table(url):
    soup = get_page(url)
    return soup.find_all('table', class_='wikitable')[0]

def get_location(name, file_extension):
    parent_path = os.path.abspath(os.curdir)
    file_name = "%s/%s.%s" % ('data', name, file_extension)
    return os.path.join(parent_path, file_name)

def save_to_json(data, name):
    json_file = open(get_location(name, 'json'), 'w')
    json_file.write(
        json.dumps(data, sort_keys=True, indent=2, separators=(',', ': '))
    )
    json_file.close()



