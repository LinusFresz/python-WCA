#!/usr/bin/python

import sys
from db import WCA_Database

# Print table
def table(rank, format):
    sys.stdout=open("best4place.txt","w")
    print('[spoiler=Best results in fourth place]')
    print('[table]')
    print('[tr][td][td]Name[/td][td]Streak[/td][/tr]')
    # If more than 100 people have an average, just take top 100
    for k in range(0, len(rank)):
        i = k+1
        for l in range(0,k):
            if rank[k][format] == rank[k-l][format]:
                i = k-l+1
        print('[tr][td]', i, '[/td][td]', rank[k][format],'[/td][td]', rank[k]['personName'], '[/td][td]', rank[k]['competitionId'], '[/td][/tr]')
        if k > 100:
            break
    print('[/table]')
    print('[/spoiler]')
    sys.stdout.close()


cur = WCA_Database.query("SELECT best, average, personName, competitionId, pos FROM Results WHERE pos = 4 AND eventId = '333fm' AND best > 0 AND average = 0 ORDER BY best")

rows = cur.fetchall()


table(rows, 'best')
