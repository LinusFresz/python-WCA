#!/usr/bin/python

import pymysql

conn = pymysql.connect(host='127.0.0.1', 
unix_socket='/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock', 
user='root', 
passwd=None, 
db='wca')

cur = conn.cursor()
cur.execute("USE wca")
cur.execute("SELECT personName, COUNT(DISTINCT competitionID) AS companzahl FROM Results WHERE personCountryId = 'Germany' AND competitionId LIKE '%2016' GROUP BY personName ORDER BY companzahl DESC Limit 100")
print(cur.fetchall())
cur.close()
conn.close()