from lib.wikipedia_fetch import get_page_table, save_to_json

table = get_page_table('http://en.wikipedia.org/wiki/List_of_urban_areas_by_population')
data = []

for i, row in enumerate(table):
    if i > 1:
        entry = {}
        for ii, col in enumerate(row):
            if ii == 1:
                entry['rank'] = int(col.text.strip())
            if ii == 5:
                entry['name'] = col.text.strip()
            if ii == 7:
                entry['country'] = col.text.strip()
            if ii == 9:
                entry['population'] = int(col.text.strip().replace(',', ''))
            if ii == 11:
                entry['area'] = int(col.text.strip().replace(',', ''))
            if ii == 13:
                entry['density'] = int(col.text.strip().replace(',', ''))
        if 'name' in entry and 'population' in entry:
            data.append(entry)

sorted(data, key=lambda k: k['population'])
save_to_json(data, 'urban-areas')
