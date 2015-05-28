# Simple Sample Queries

Below are some queries that work against the Countries & Urban data sets.

## Reading Data

```
//All Countries
r.table("countries") 
//All Countries, but just the name & population fields
r.table("countries")
  .pluck(["name", "population"])
```

### Filters, anyone?

```
r.table("countries")
  //.filter(r.row['population'] > 30) //BROKEN
  //.filter(r.row('population') > 30) //BROKEN
  //.filter(lambda country: country['population'] > 5000) //no lambdas for you!
  .filter(r.row('population').gt(30))
  .count()
```

### Join

For a join, you need to have an index that matches. In this case, create a secondary index on "country" in the "urban" table.

![RethinkDB-Secondary-Indexes](https://raw.githubusercontent.com/santacruzjs/sample-data/master/queries/images/RethinkDB-Secondary-Indexes.png "RethinkDB-Secondary-Indexes")

```
r.table('countries')
  .eqJoin("name", r.table("urban"), {index:"country"})
  .without({"right": "id"})
  .zip()
```
