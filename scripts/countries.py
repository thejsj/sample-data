from lib.wikipedia_fetch import get_page_table, save_to_json

table = get_page_table('http://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
data = []

for i, row in enumerate(table):
    if i > 1:
        entry = {}
        for ii, col in enumerate(row):
            if ii == 3:
                entry['name'] = col.text.strip()
            if ii == 5:
                entry['population'] = int(col.text.strip().replace(',', ''))
            if ii == 7:
                entry['date'] = col.text.strip()
            if ii == 9:
                percentage = col.text.strip().replace('%', '')
                entry['percentage_of_population'] = percentage
        if 'name' in entry and 'population' in entry:
            data.append(entry)

sorted(data, key=lambda k: k['population'])
save_to_json(data, 'countries')
