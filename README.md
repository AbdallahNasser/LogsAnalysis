# LogsAnalysis
Udacity full-stack web developer nanodegree - Logs Analysis (database project)

# Requirements
To be able to use it, you must have [Python2](https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi), [PostgreSQL](https://www.postgresql.org) & [psycopg2 library](http://initd.org/psycopg/docs/install.html) installed on your machine

# How to use it
1. clone/download this repository
2. Download this [database file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
3. Unzip.
4. Move 'newsdata.sql' file to your working directory.
5. Load data to local database: `psql -d news -f newsdata.sql`
6. Run ` database.py `
