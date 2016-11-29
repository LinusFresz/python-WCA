#!/usr/bin/python

import pymysql, sys

# Choose the event you want to have a single-ranking of
getit = 'best'
category = '555bf'

# Print table
def table(rank, event, place):
    sys.stdout=open("best4place.txt","w")
    print('[spoiler=Best results in fourth place,', category, ']')
    print('[table]')
    print('[tr][td][td]Single[/td][td]Name[/td][td]Competition[/td][td]Current ranking[/td][/tr]')
    # If more than 100 people have an average, just take top 100
    for k in range(0, len(rank)):
        i = k+1
        for l in range(0,k):
            if rank[k][event] == rank[k-l][event]:
                i = k-l+1
        print('[tr][td]', i, '[/td][td]', rank[k][event],'[/td][td]', rank[k]['personName'], '[/td][td]', rank[k]['competitionId'], '[/td][td]', place[k], '[/td][/tr]')
        if k > 10:
            break
    print('[/table]')
    print('[/spoiler]')
    sys.stdout.close()


conn = pymysql.connect(host='127.0.0.1',
                       unix_socket='/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock',
                       user='root',
                       passwd=None,
                       db='wca')


# Get the results of interest from the database: one query for all results of fourth places in this category, the second query for the actual ranking
cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute("SELECT best, average, personName, competitionId, pos FROM Results WHERE pos = 4 and eventId = (%s) and best > 0 ORDER BY best", (category))

rows = cur.fetchall()

cur.execute("SELECT best, eventId from RanksSingle WHERE eventId = (%s)", (category))

row = cur.fetchall()


# Check the results of the fourth place against the current ranking
ranking = []

for i in range(0,len(rows)):
    for k in range(0,len(row)):
        if rows[i]['best'] == row[k]['best']:
            ranking.append(k+1)
            break

# Generate table with results
table(rows, getit, ranking)

cur.close()
conn.close()



