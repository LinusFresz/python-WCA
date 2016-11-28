#!/usr/bin/python

import pymysql, sys

# Print table
def table(rank, getit):
    sys.stdout=open("best4place.txt","w")
    print('[spoiler=Best results in fourth place]')
    print('[table]')
    print('[tr][td][td]Name[/td][td]Streak[/td][/tr]')
    # If more than 100 people have an average, just take top 100
    for k in range(0, len(rank)):
        i = k+1
        for l in range(0,k):
            if rank[k][getit] == rank[k-l][getit]:
                i = k-l+1
        print('[tr][td]', i, '[/td][td]', rank[k][getit],'[/td][td]', rank[k]['personName'], '[/td][td]', rank[k]['competitionId'], '[/td][/tr]')
        if k > 100:
            break
    print('[/table]')
    print('[/spoiler]')
    sys.stdout.close()

conn = pymysql.connect(host='127.0.0.1',
                       unix_socket='/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock',
                       user='root',
                       passwd=None,
                       db='wca')


cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute("SELECT best, average, personName, competitionId, pos FROM Results WHERE pos = 4 and eventId = '333fm' and best > 0 and average = 0 ORDER BY best")


rows = cur.fetchall()

table(rows, 'best')

cur.close()
conn.close()



