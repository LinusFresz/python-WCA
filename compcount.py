#!/usr/bin/python

from db import WCA_Database

cur = WCA_Database.query("SELECT personName, COUNT(DISTINCT competitionID) AS companzahl FROM Results WHERE competitionId LIKE '%2017' GROUP BY personName ORDER BY companzahl DESC Limit 100")

rows = cur.fetchall()

for k in rows:
    print(k)
