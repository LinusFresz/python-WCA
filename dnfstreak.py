#!/usr/bin/python

import sys
from itertools import groupby
from db import WCA_Database

# Print table
def table(rank):
    sys.stdout=open("dnfstreak.txt","w")
    print('[spoiler=Longest streaks]')
    print('[table]')
    print('[tr][td][td]Name[/td][td]Streak[/td][/tr]')
    # If more than 100 people have an average, just take top 100
    for k in range(0, len(rank)):
        i = k+1
        for l in range(0,k):
            if rank[k][1] == rank[k-l][1]:
                i = k-l+1
        print('[tr][td]', i, '[/td][td]', rank[k][0],'[/td][td]', rank[k][1], '[/td][/tr]')
        if k > 100:
            break
    print('[/table]')
    print('[/spoiler]')
    sys.stdout.close()


cur = WCA_Database.query("SELECT eventId, personName, value1, value2, value3, value4, value5 FROM Results WHERE eventId = '333fm'")

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
    attempts = 0    # Count of all attempts
    solves = 0      # Count of all solved attempts
    count = 0       # Count of current solvestreak
    best = 0        # Count of best solvestreak
    sum = 0         # Sum of all solves of best mean
    mean = 0        # Calculated mean of best streak
    meanres = []    # Moves of each attempt of current streak
    safemeanres = []    # Moves of each attempt of best streak
    for k in range(0,len(results[i])):
        if results[i][k] == -1 and k != (len(results[i])-1):
            count = count + 1
            attempts = attempts + 1
            solves = solves + 1
            meanres.append(results[i][k])
        if results[i][k] > 0 and k != (len(results[i])-1):
            if count > best:
                best = count
                safemeanres = meanres
            meanres = []
            count = 0
            attempts = attempts + 1
        if k == (len(results[i])-1):
            if results[i][k] == -1 and count > best:
                best = count + 1
                solves = solves + 1
                meanres.append(results[i][k])
                safemeanres = meanres
            if results[i][k] > 0 and count > best:
                best = count
                safemeanres = meanres
            attempts = attempts + 1

    res.append((i, best))

# Sort all results by longest streak
sorted_x = sorted(res, key=lambda x:x[1], reverse=True)

# Build table with results
table(sorted_x)
