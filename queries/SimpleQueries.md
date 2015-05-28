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
  .filter(r.row('population').gt(30))
  .filter(function (country) { return country('population').gt(5000) })
  .count()
```

### Join

For a `eqJoin`, you need to have an index that matches. In this case, create a secondary index on "country" in the "urban" table.

![RethinkDB-Secondary-Indexes](https://raw.githubusercontent.com/santacruzjs/sample-data/master/queries/images/RethinkDB-Secondary-Indexes.png "RethinkDB-Secondary-Indexes")

```
r.table('countries')
  .eqJoin("name", r.table("urban"), {index:"country"})
  .without({"right": "id"})
  .zip()
```
