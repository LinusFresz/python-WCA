#!/usr/bin/python

import sys
from db import WCA_Database

# Print table
def table(rank):
    sys.stdout=open("pbstreak.txt","w")
    print('[spoiler=Most consecutive competitions with at least one PB]')
    print('[table]')
    print('[tr][td][td]Number of competitions with at least one PB[/td][td]Name[/td][td]first competition[/td][td]last competition[/td][td]status[/td][td]started at first competition[/td][/tr]')
    # If more than 100 people have an average, just take top 100
    for k in range(0, len(rank)):
        i = k+1
        for l in range(0,k):
            if rank[k][0] == rank[k-l][0]:
                i = k-l+1
        print('[tr][td]', i, '[/td][td]', rank[k][0], '[/td][td]', rank[k][1], '[/td][td]', rank[k][2], '[/td][td]', rank[k][3], '[/td][td]', rank[k][4], '[/td][td]', rank[k][5], '[/td][/tr]')
        if k > 100:
            break
    print('[/table]')
    print('[/spoiler]')
    sys.stdout.close()


# Query to get all results of each competitor to determine the streaks
cur = WCA_Database.query("SELECT res.competitionId, res.eventId, res.roundTypeId, res.pos, res.personName, res.personId, res.best, res.average, res.personCountryId, comp.year, comp.month, comp.day FROM Results AS res INNER JOIN Competitions AS comp ON res.competitionId = comp.id GROUP BY eventId,  competitionId, roundTypeId, personId ORDER BY personId, comp.year, comp.month, comp.day")

row = cur.fetchall()

# Determine Number of rounds for each competitor
counting = 1                    # Number of rounds per competitor, safed in 'competitorslength'
competitorslength = []          # List of Number of rounds attended by each competitor
for k in range(1,len(row)):
    if row[k]['personId'] == row[k-1]['personId']:
        counting = counting +1
        if k == (len(row)-1):
            competitorslength.append((row[k-1]['personId'], counting, row[k-1]['personName']))
            counting = 1
    elif row[k]['personId'] != row[k-1]['personId']:
        competitorslength.append((row[k-1]['personId'], counting, row[k-1]['personName']))
        counting = 1

# Count the rounds per competition per competitor
finalres = []           # Results of all competitors with a streak
startcompetitor = 1     # Row in which the results of a competitor start

for n in competitorslength:
    endcompetitor = n[1] - 1    # Row with last competition of current competitor
    count = 1                   # Count row of competitions for current competitor
    listofcomps = []            # List with number of rounds of each competition for current competitor
    for i in range(startcompetitor,startcompetitor+endcompetitor):
        if row[i]['competitionId'] == row[i-1]['competitionId']:
            count = count +1
            if i == (startcompetitor+endcompetitor-1):
                listofcomps.append((row[i-1]['competitionId'], count))
        elif row[i]['competitionId'] != row[i-1]['competitionId']:
            listofcomps.append((row[i-1]['competitionId'], count))
            count = 1

    competitionrows = 0
    pb = 0              # Count for each competition, if the competitor had PBs
    streak = 0          # Current Streak of competitions with pbs
    finalstreak = 0     # Longest streak
    complist = []       # Current list of consecutive comps with pbs
    finalcomplist = []  # List with comps of longest streak + first streak without pb
    
# Tracking the PB of every event for every competitor
    pbsingle = {'222': 10**10, '333': 10**10, '444': 10**10, '555': 10**10, '666': 10**10, '777': 10**10, 'minx': 10**10, 'pyram': 10**10, 'skewb': 10**10, '333oh': 10**10, '333ft': 10**10, 'clock': 10**10, 'sq1': 10**10, '333fm': 10**10, '333bf': 10**10, '444bf': 10**10, '555bf': 10**10, '333mbf': 0, '333multitime': 10**10, '333multicubes': 0, 'magic': 10**10, 'mmagic': 10**10}
    pbaverage = {'222': 10**10, '333': 10**10, '444': 10**10, '555': 10**10, '666': 10**10, '777': 10**10, 'minx': 10**10, 'pyram': 10**10, 'skewb': 10**10, '333oh': 10**10, '333ft': 10**10, 'clock': 10**10, 'sq1': 10**10, '333fm': 10**10, '333bf': 10**10, 'magic': 10**10, 'mmagic': 10**10}
    
# Check for each competition, if the competitor had a PB
    for l in listofcomps:
        complength = l[1]
        for k in range(startcompetitor+competitionrows-1,startcompetitor+competitionrows+complength-1):
            for key in pbsingle:
                if key == row[k]['eventId']:
                    if row[k]['eventId'] == '333mbf' and row[k]['best'] > 0:
                        solved = 0
                        points = 0
                        multi = row[k]['best']
                    
                        cubes = 99-round(multi/10000000)
                        time = multi-round(multi/10000000)*10000000
                
                        if (cubes == pbsingle['333multicubes'] and time <= pbsingle['333multitime']) or cubes > pbsingle['333multicubes']:
                            pbsingle['333multicubes'] = cubes
                            pbsingle['333multitime'] = time
                            pb = pb + 1
                    elif pbsingle[key] >= row[k]['best'] and row[k]['best'] > 0:
                        pbsingle[key] = row[k]['best']
                        pb = pb + 1
            for key in pbaverage:
                if key == row[k]['eventId'] and pbaverage[key] >= row[k]['average'] and row[k]['average'] > 0:
                    pbaverage[key] = row[k]['average']
                    pb = pb + 1

        if pb == 0: # If no PB, check if current streak > longest streak and reset
            if streak > finalstreak:
                finalstreak = streak
                finalcomplist = complist
            streak = 0
            complist = []
        
        else:               # Count current streak and add competitions to list of current streak
            streak = streak + 1
            complist.append(row[k]['competitionId'])

        pb = 0
        
        competitionrows = competitionrows + complength
    startcompetitor = startcompetitor + endcompetitor + 1

    ongo = 'ended'                  # If competitor broke a PB at his last comp + in longest streak -> ongoing streak
    if streak > finalstreak:        # Check if the competitor broke his streak with his last competition
        finalstreak = streak
        finalcomplist = complist
        ongo = 'ongoing'

# Check, if the streak started with the first attended competition
    startwith = 'No'
    if len(finalcomplist) > 15:
        if finalcomplist[0] == listofcomps[0][0]:
            startwith = 'Yes'
        
# Take all interesting stuff of a competitor and put it in a list
        finalres.append((finalstreak, n[2], finalcomplist[0], finalcomplist[len(finalcomplist)-1], ongo, startwith))

# Sort the finalres-list by longest streak without podium
sorted_x = sorted(finalres, key=lambda x:x[0], reverse=True)

# Build table with results
table(sorted_x)
