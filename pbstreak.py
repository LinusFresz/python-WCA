#!/usr/bin/python

# I know this script is quite ugly and there are way better ways to do this task
# Anyway because I am just a beginner at programming with python I am quite happy to get a script going to fulfill this task


import pymysql
import sys


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



# Connection to database
conn = pymysql.connect(host='127.0.0.1',
                       unix_socket='/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock',
                       user='root',
                       passwd=None,
                       db='wca')


# Query to get all results of each competitor to determine the streaks
cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute("SELECT res.competitionId, res.eventId, res.roundId, res.pos, res.personName, res.personId, res.best, res.average, comp.year, comp.month, comp.day FROM Results AS res INNER JOIN Competitions AS comp ON res.competitionId = comp.id GROUP BY eventId,  competitionId, roundId, personId ORDER BY personId, comp.year, comp.month, comp.day")

row = cur.fetchall()


# Determine all rounds for each competitor
counting = 1
compe = []          # Rounds attended by each competitor
for k in range(1,len(row)):
    if row[k]['personId'] == row[k-1]['personId'] and k < (len(row)-1):
        counting = counting +1
    elif row[k]['personId'] != row[k-1]['personId'] and k < (len(row)-1):
        compe.append((row[k-1]['personId'], counting, row[k-1]['personName']))
        counting = 1
    elif row[k]['personId'] == row[k-1]['personId'] and k == (len(row)-1):
        counting = counting + 1
        compe.append((row[k-1]['personId'], counting, row[k-1]['personName']))
        counting = 1
    elif row[k]['personId'] != row[k-1]['personId'] and k == (len(row)-1):
        compe.append((row[k-1]['personId'], counting, row[k-1]['personName']))
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



    f = 0
    nope = 0            # Count for each competition, if the competitor had PBs
    streak = 0          # Current Streak of competitions with pbs
    finalstreak = 0     # Longest streak
    complist = []       # Current list of consecutive comps with pbs
    finalcomplist = []  # List with comps of longest streak + first streak without pb


    # Tracking the PB of every event for every competitor
    twosingle = 10**10
    twoaverage = 10**10
    rubikssingle = 10**10
    rubiksaverage = 10**10
    foursingle = 10**10
    fouraverage = 10**10
    fivesingle = 10**10
    fiveaverage = 10**10
    sixsingle = 10**10
    sixaverage = 10**10
    sevensingle = 10**10
    sevenaverage = 10**10
    megasingle = 10**10
    megaaverage = 10**10
    pyrasingle = 10**10
    pyraaverage = 10**10
    skoobsingle = 10**10
    skoobaverage = 10**10
    ohsingle = 10**10
    ohaverage = 10**10
    feetsingle = 10**10
    feetaverage = 10**10
    clocksingle = 10**10
    clockaverage = 10**10
    sqsingle = 10**10
    sqaverage = 10**10
    fmsingle = 10**10
    fmaverage = 10**10
    bldsingle = 10**10
    bldaverage = 10**10
    fourbld = 10**10
    fivebld = 10**10
    multipoints = 0
    multitime = 10**10
    magicsingle = 10**10
    magicaverage = 10**10
    mmagicsingle = 10**10
    mmagicaverage = 10**10


    # Check for each competition, if the competitor had a PB
    for l in range(0,len(comping)):
        m = comping[l][1]
        for k in range(wat+f-1,wat+f+m-1):
            if row[k]['eventId'] == '222':
                if row[k]['best'] < twosingle and row[k]['best'] > 0:
                    twosingle = row[k]['best']
                else:
                    nope = nope + 1
                if row[k]['average'] < twoaverage and row[k]['average'] > 0:
                    twoaverage = row[k]['average']
                else:
                    nope = nope + 1
            elif row[k]['eventId'] == '333':
                if row[k]['best'] < rubikssingle and row[k]['best'] > 0:
                    rubikssingle = row[k]['best']
                else:
                    nope = nope + 1
                if row[k]['average'] < rubiksaverage and row[k]['average'] > 0:
                    rubiksaverage = row[k]['average']
                else:
                    nope = nope + 1
            elif row[k]['eventId'] == '444':
                if row[k]['best'] < foursingle and row[k]['best'] > 0:
                    foursingle = row[k]['best']
                else:
                    nope = nope + 1
                if row[k]['average'] < fouraverage and row[k]['average'] > 0:
                    fouraverage = row[k]['average']
                else:
                    nope = nope + 1
            elif row[k]['eventId'] == '555':
                if row[k]['best'] < fivesingle and row[k]['best'] > 0:
                    fivesingle = row[k]['best']
                else:
                    nope = nope + 1
                if row[k]['average'] < fiveaverage and row[k]['average'] > 0:
                    fiveaverage = row[k]['average']
                else:
                    nope = nope + 1
            elif row[k]['eventId'] == '666':
                if row[k]['best'] < sixsingle and row[k]['best'] > 0:
                    sixsingle = row[k]['best']
                else:
                    nope = nope + 1
                if row[k]['average'] < sixaverage and row[k]['average'] > 0:
                    sixaverage = row[k]['average']
                else:
                    nope = nope + 1
            elif row[k]['eventId'] == '777':
                if row[k]['best'] < sevensingle and row[k]['best'] > 0:
                    sevensingle = row[k]['best']
                else:
                    nope = nope + 1
                if row[k]['average'] < sevenaverage and row[k]['average'] > 0:
                    sevenaverage = row[k]['average']
                else:
                    nope = nope + 1
            elif row[k]['eventId'] == 'minx':
                if row[k]['best'] < megasingle and row[k]['best'] > 0:
                    megasingle = row[k]['best']
                else:
                    nope = nope + 1
                if row[k]['average'] < megaaverage and row[k]['average'] > 0:
                    megaaverage = row[k]['average']
                else:
                    nope = nope + 1
            elif row[k]['eventId'] == 'pyram':
                if row[k]['best'] < pyrasingle and row[k]['best'] > 0:
                    pyrasingle = row[k]['best']
                else:
                    nope = nope + 1
                if row[k]['average'] < pyraaverage and row[k]['average'] > 0:
                    pyraaverage = row[k]['average']
                else:
                    nope = nope + 1
            elif row[k]['eventId'] == 'skewb':
                if row[k]['best'] < skoobsingle and row[k]['best'] > 0:
                    skoobsingle = row[k]['best']
                else:
                    nope = nope + 1
                if row[k]['average'] < skoobaverage and row[k]['average'] > 0:
                    skoobaverage = row[k]['average']
                else:
                    nope = nope + 1
            elif row[k]['eventId'] == '333oh':
                if row[k]['best'] < ohsingle and row[k]['best'] > 0:
                    ohsingle = row[k]['best']
                else:
                    nope = nope + 1
                if row[k]['average'] < ohaverage and row[k]['average'] > 0:
                    ohaverage = row[k]['average']
                else:
                    nope = nope + 1
            elif row[k]['eventId'] == '333ft':
                if row[k]['best'] < feetsingle and row[k]['best'] > 0:
                    feetsingle = row[k]['best']
                else:
                    nope = nope + 1
                if row[k]['average'] < feetaverage and row[k]['average'] > 0:
                    feetaverage = row[k]['average']
                else:
                    nope = nope + 1
            elif row[k]['eventId'] == 'clock':
                if row[k]['best'] < clocksingle and row[k]['best'] > 0:
                    clocksingle = row[k]['best']
                else:
                    nope = nope + 1
                if row[k]['average'] < clockaverage and row[k]['average'] > 0:
                    clockaverage = row[k]['average']
                else:
                    nope = nope + 1
            elif row[k]['eventId'] == 'sq1':
                if row[k]['best'] <= sqsingle and row[k]['best'] > 0:
                    sqsingle = row[k]['best']
                else:
                    nope = nope + 1
                if row[k]['average'] <= sqaverage and row[k]['average'] > 0:
                    sqaverage = row[k]['average']
                else:
                    nope = nope + 1
            elif row[k]['eventId'] == '333bf':
                if row[k]['best'] <= bldsingle and row[k]['best'] > 0:
                    bldsingle = row[k]['best']
                else:
                    nope = nope + 1
                if row[k]['average'] <= bldaverage and row[k]['average'] > 0:
                    bldaverage = row[k]['average']
                else:
                    nope = nope + 1
            elif row[k]['eventId'] == '333fm':
                if row[k]['best'] <= fmsingle and row[k]['best'] > 0:
                    fmsingle = row[k]['best']
                else:
                    nope = nope + 1
                if row[k]['average'] <= fmaverage and row[k]['average'] > 0:
                    fmaverage = row[k]['average']
                else:
                    nope = nope + 1
            elif row[k]['eventId'] == '444bf':
                if row[k]['best'] <= fourbld and row[k]['best'] > 0:
                    fourbld = row[k]['best']
                else:
                    nope = nope + 2
            elif row[k]['eventId'] == '555bf':
                if row[k]['best'] <= fivebld and row[k]['best'] > 0:
                    fivebld = row[k]['best']
                else:
                    nope = nope + 2
            elif row[k]['eventId'] == 'magic':
                if row[k]['best'] <= magicsingle and row[k]['best'] > 0:
                    magicsingle = row[k]['best']
                else:
                    nope = nope + 1
                if row[k]['average'] <= magicsingle and row[k]['average'] > 0:
                    magicsingle = row[k]['average']
                else:
                    nope = nope + 1
            elif row[k]['eventId'] == 'mmagic':
                if row[k]['best'] <= mmagicsingle and row[k]['best'] > 0:
                    mmagicsingle = row[k]['best']
                else:
                    nope = nope + 1
                if row[k]['average'] <= mmagicsingle and row[k]['average'] > 0:
                    mmagicsingle = row[k]['average']
                else:
                    nope = nope + 1
            elif row[k]['eventId'] == '333mbf':
                if row[k]['best'] > 0:
                    solved = 0
                    points = 0
                    list = []
                    list.append(row[k]['best'])
                    
                    cubes = 99-round(list[0]/10000000)
                    time = list[0]-round(list[0]/10000000)*10000000
                
                    if (cubes == multipoints and time <= multitime) or cubes > multipoints:
                        multipoints = cubes
                        multitime = time
                    else:
                        nope = nope + 2
                else:
                    nope = nope + 2


        if nope == 2*m: # If no PB, check if current streak > longest streak and reset
            #complist.append(row[k]['competitionId']) # This competition breaks the streak, no PB set there -> will be the last competition in complist/finalcomplist
            if streak > finalstreak:
                finalstreak = streak
                finalcomplist = complist
            streak = 0
            complist = []

        else:               # Count current streak and add competitions to list of current streak competitions
            streak = streak + 1
            complist.append(row[k]['competitionId'])

        nope = 0


        f = f + m
    wat = wat + wut + 1

    ongo = 'ended'                  # If competitor broke at his last comp a PB + in streak -> ongoing streak
    if streak > finalstreak:        # Check if the competitor broke his streak with his last competition
        finalstreak = streak
        finalcomplist = complist
        ongo = 'ongoing'


    # Check, if the streak started with the first attended competition
    startwith = 'No'
    if finalcomplist != []:
        if finalcomplist[0] == comping[0][0]:
            startwith = 'Yes'
        
        # Take all interesting stuff of a competitor and put it in a list
        finalres.append((finalstreak, compe[n][2], finalcomplist[0], finalcomplist[len(finalcomplist)-1], ongo, startwith))


# Sort the finalres-list by longest streak without podium
sorted_x = sorted(finalres, key=lambda x:x[0], reverse=True)

# Build table with results
table(sorted_x)

cur.close()
conn.close()



