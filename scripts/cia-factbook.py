import csv
from lib.wikipedia_fetch import save_to_json

csvfile = open('./scripts/cia-data-all.csv')
reader = csv.DictReader(csvfile)
countries = []
for row in reader:
    country = {}
    for key, col in row.iteritems():
        country[key] = col
    countries.append(country)
save_to_json(countries, 'cia-countries')
