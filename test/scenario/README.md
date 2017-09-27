# Testing the OBNL Scenario Package


## About

This directory contains tests for OBNL's Scenario Package:
- `test_scenario.py`: tests the basic functionality of the Scenario Package, including persistency with JSON files
- `test_scenario_db.py`: tests the database persistency


## Prerequisites

For testing the basic functionality, a standard OBNL installation is sufficient. For testing the database persistency, the following prerequisites apply:
- The [SQLAlchemy](http://www.sqlalchemy.org/) and [psycopg2](https://pypi.python.org/pypi/psycopg2) Python packages need to be installed.
- A working implementation of the [CityGML 3D City Database Simulation Package](http://) (PostgreSQL version) needs to be available. **The database should be empty.**
- Adapt the `PostgreSQLConnectionInfo` in file `test_scenario_db.py` to your actual  database implementation. By *default*, it is assumed that the database name is `testdb`, that it is installed locally (and accessible via standard port 5432) and that it can be accessed by a user called `postgres` (with password `postgres`).


## Testing the Scenario Package

For testing the OBNL Scenario Package, open a command terminal, change to the test directory and type the follwing:
```
python test_scenario.py
python test_scenario_db.py
```

**NOTE**: When rerunning the test for the database persistency, make sure the database is empty before!