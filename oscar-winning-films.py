from lib.wikipedia_fetch import get_page_table, save_to_json
import re

table = get_page_table('http://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films')
data = []

for i, row in enumerate(table):
    if i > 1:
        entry = {}
        for ii, col in enumerate(row):
            if ii == 1:
                entry['name'] = col.text.strip()
            if ii == 3:
                year = re.split('\/', col.text.strip())[0]
                entry['year'] = int(year.strip())
            if ii == 5:
                awards = re.sub(r"\([0-9]*\)", "", col.text.strip())
                entry['awards'] = int(awards.strip())
            if ii == 7:
                nominations = re.sub(r"\[[0-9]*\]", "", col.text.strip())
                entry['nominations'] = int(nominations.strip())
        if 'name' in entry and 'awards' in entry:
            data.append(entry)

sorted(data, key=lambda k: k['awards'])
save_to_json(data, 'oscar-winning-films')
