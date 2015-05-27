# Sample Data

This is a collection of test data JSON files taken from WikiPedia. It's intended to be used with RethinkDB, but can be for anything in which some test data is required.

## Inserting into RethinkDB

These are the ReQL queries to insert the test data into your RethinkDB database. Notice that these queries use the remote URL for the GitHub repository. Hence, you don't need to clone this repository in order to run these queries. Also, keep in mind that RethinkDB uses the `test` database by default, so these tables will be created in the `test` database.

*Countries*

```
// Create table
r.tableCreate('countries')
// Insert data from JSON files
r.table('countries')
 .insert(r.json(r.http('https://raw.githubusercontent.com/thejsj/sample-data/master/countries.json')))
```

*Oscar Winning Films*
```
// Create table
r.tableCreate('films')
// Insert data from JSON files
r.table('films')
 .insert(r.json(r.http('https://raw.githubusercontent.com/thejsj/sample-data/master/oscar-winning-films.json')))
```
*World's most populated urban areas*

```
// Create table
r.tableCreate('urban_areas')
// Insert data from JSON files
r.table('urban_areas')
 .insert(r.json(r.http('https://raw.githubusercontent.com/thejsj/sample-data/master/urban-areas.json')))
```

## Generating

In order to re-generate this data, you must install the dependencies and run the python scripts.

```
pip install
python countries.py
python oscar-winning-films.py
python urban-areas.py
```

