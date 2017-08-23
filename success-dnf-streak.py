#!/usr/bin/python

import sys
from itertools import groupby
from db import WCA_Database

# Print table, max length: 100
def table(rank):
    sys.stdout=open("successdnfstreak.txt","w")
    print('[spoiler=Longest streaks]')
    print('[table]')
    print('[tr][td][td]Name[/td][td]DNF-Streak[/td][td]last success before[/td][td]first success after[/td][/tr]')
    for k in range(0, len(rank)):
        i = k+1
        for l in range(0,k):
            if rank[k][1] == rank[k-l][1]:
                i = k-l+1
        print('[tr][td]', i, '[/td][td]', rank[k][0], '[/td][td]', rank[k][1], '[/td][td]', rank[k][2], '[/td][td]', rank[k][3], '[/td][/tr]')
        if k > 100:
            break
    print('[/table]')
    print('[/spoiler]')
    sys.stdout.close()


cur = WCA_Database.query("SELECT eventId, personName, value1, value2, value3, value4, value5 FROM Results WHERE eventId = '444bf'")

rows = cur.fetchall()

results = {}
res = []

# Get everyone's results
for row in rows:
    for i in ('value1', 'value2', 'value3', 'value4', 'value5'):
        if row[i] > 0 or row[i] == -1:
            results.setdefault(row['personName'], []).append(row[i])

# Find longest success streak
for i in results:
    count = 0       # Count of current solvestreak
    best = 0        # Count of best solvestreak
    sum = 0         # Sum of all solves of best mean
    icoun = []      # Count of Number of DNFs of current streak
    safecoun = []   # Count of Number of DNFs of longest streak
    
    for k in range(0,len(results[i])):
        if results[i][k] == -1 and k != (len(results[i])-1):
            count = count + 1
            icoun.append(k)
        if results[i][k] > 0 and k != (len(results[i])-1):
            if count > best:
                best = count
                safecoun = icoun
            icoun = []
            count = 0
        if k == (len(results[i])-1):
            if results[i][k] == -1 and count > best:
                best = count + 1
                icoun.append(k)
            if results[i][k] > 0 and count > best:
                best = count

    for l in safecoun:
        sum = sum + l
    if sum > 0:
        beg = results[i][safecoun[0]-1]
        if beg == -1:
            beg = -2
        end = results[i][safecoun[0]+len(safecoun)]
    else:
        beg = -2
        end = -2
    if beg != -2 and end != -2:
        res.append((i, best, beg, end))

# Sort all results by longest streak
sorted_x = sorted(res, key=lambda x:x[1], reverse=True)

# Build table with results
table(sorted_x)
