#!/usr/bin/python

import sys
from db import WCA_Database

# Print table
def table(rank):
    sys.stdout=open("withoutpodium.txt","w")
    print('[spoiler=Most consecutive competitions without podium]')
    print('[table]')
    print('[tr][td][td]Name[/td][td]Number of competitions without podium[/td][td]Number of competitions overall[/td][td]starting with[/td][td]ending with[/td][td]beginning at first comp[/td][/tr]')
    # If more than 100 people have an average, just take top 100
    for k in range(0, len(rank)):
        i = k+1
        for l in range(0,k):
            if rank[k][0] == rank[k-l][0]:
                i = k-l+1
        print('[tr][td]', i, '[/td][td]', rank[k][1], '[/td][td]', rank[k][0], '[/td][td]', rank[k][4], '[/td][td]', rank[k][2][0], '[/td][td]', rank[k][2][len(rank[k][2])-1], '[/td][td]', rank[k][3], '[/td][/tr]')
        if k > 100:
            break
    print('[/table]')
    print('[/spoiler]')
    sys.stdout.close()


# First query to get all results of each competitor to determine the streaks
cur = WCA_Database.query("SELECT res.competitionId, res.eventId, res.roundTypeId, res.pos, res.personName, res.best, res.average, comp.year, comp.month, comp.day FROM Results AS res INNER JOIN Competitions AS comp ON res.competitionId = comp.id WHERE (roundTypeId = '1' OR roundTypeId = 'f' OR roundTypeId = 'c' OR roundTypeId = 'd') GROUP BY eventId,  competitionId, roundTypeId, personName ORDER BY personName, comp.year, comp.month, comp.day")

row = cur.fetchall()

# Second query to get the count of competitions per competitor
cur.execute("SELECT personName, COUNT(DISTINCT competitionId) AS companzahl FROM Results GROUP BY personName ORDER BY companzahl DESC")

rows = cur.fetchall()


# Determine the of final rounds for each competitor
counting = 1
compe = []          # final Rounds attended by each competitor
for k in range(1,len(row)):
    if row[k]['personName'] == row[k-1]['personName'] and k < (len(row)-1):
        counting = counting +1
    elif row[k]['personName'] != row[k-1]['personName'] and k < (len(row)-1):
        compe.append((row[k-1]['personName'], counting))
        counting = 1
    elif row[k]['personName'] == row[k-1]['personName'] and k == (len(row)-1):
        counting = counting + 1
        compe.append((row[k-1]['personName'], counting))
        counting = 1
    elif row[k]['personName'] != row[k-1]['personName'] and k == (len(row)-1):
        compe.append((row[k-1]['personName'], counting))
        counting = 1


# Count the rounds per competition per competitor
finalres = []       # Results of all competitors with a streak
wat = 1

for n in range(0,len(compe)):
    wut = compe[n][1] - 1
    count = 1
    comping = []     # List with number of rounds for each competitor
    for i in range(wat,wat+wut):
        if row[i]['competitionId'] == row[i-1]['competitionId'] and i < (wat+wut-1):
            count = count +1
        elif row[i]['competitionId'] != row[i-1]['competitionId'] and i < (wat+wut-1):
            comping.append((row[i-1]['competitionId'], count))
            count = 1
        elif row[i]['competitionId'] == row[i-1]['competitionId'] and i == (wat+wut-1):
            count = count + 1
            comping.append((row[i-1]['competitionId'], count))
        elif row[i]['competitionId'] != row[i-1]['competitionId'] and i == (wat+wut-1):
            comping.append((row[i-1]['competitionId'], count))

    # Check for each competition, if the competitor is on the podium
    f = 0
    withoutpod = 0      # Count of non-podium-places of each competition
    strecke = 0         # Number of competitions of the current streak
    streaking = 0       # Number of competitions of the longest streak
    competitions = []   # Competitions of the current streak
    saving = []         # Competitions of the longest streak
    
    for l in range(0,len(comping)):
        m = comping[l][1]
        for i in range(wat+f-1,wat+f+m-1):
            if row[i]['pos'] > 3:
                withoutpod = withoutpod + 1
            elif row[i]['pos'] < 4 and (row[i]['best'] > 0 or row[i]['average'] > 0):
                withoutpod = 0
                break

        if withoutpod > 0:
            competitions.append(comping[l][0])
            strecke = strecke + 1
            
            if strecke > streaking:
                saving = competitions
                streaking = strecke

        elif withoutpod == 0:
            strecke = 0
            competitions = []
        
        f = f + m
    
    wat = wat + wut + 1

    # Check, if the streak started with the first attended competition
    startwith = 'No'
    if saving != []:
        if saving[0] == comping[0][0]:
            startwith = 'Yes'

    # Add the Number of attended competition to the result
    countofcomps = 0
    for o in range(0,len(rows)):
        if rows[o]['personName'] == compe[n][0]:
            countofcomps = rows[o]['companzahl']

    # Take all interesting stuff of a competitor and put it in a list
    finalres.append((streaking, compe[n][0], saving, startwith, countofcomps))


# Sort the finalres-list by longest streak without podium
sorted_x = sorted(finalres, key=lambda x:x[0], reverse=True)

# # Build table with results
table(sorted_x)
