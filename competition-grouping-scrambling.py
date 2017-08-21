#!/usr/bin/python

import sys
import pymysql
import random


# Create scrambling and Grouping for this years German Nationals 2017
# selectscrambler(event, roundnumber, eventid, scrambler, firstscrambler, lastscrambler, groups)
selectscrambler("333fm", 1, "Fewest Moves", 0, 0, 20, 1)
selectscrambler("444bf", 1, "444BLD", 0, 0, 20, 1)
selectscrambler("555bf", 1, "555BLD", 0, 0, 20, 1)
selectscrambler("777", 1, "777 1st", 5, 0, 20, 2)
selectscrambler("666", 1, "666 1st", 5, 0, 20, 2)
selectscrambler("minx", 1, "Megaminx 1st", 5, 0, 25, 2)
selectscrambler("333mbf", 1, "Multi-Blind", 0, 0, 20, 1)
selectscrambler("777", "f", "777 Final", 4, 20, 30, 1)
selectscrambler("666", "f", "666 Final", 4, 20, 30, 1)
selectscrambler("minx", "f", "Megaminx Final", 4, 20, 30, 1)

selectscrambler("sq1", 1, "Square-1 1st", 3, 0, 20, 2)
selectscrambler("clock", 1, "Clock 1st", 3, 0, 15, 2)
selectscrambler("555", 1, "555 1st", 5, 0, 30, 3)
selectscrambler("skewb", 1, "Skewb 1st", 5, 0, 40, 3)
selectscrambler("pyram", 1, "Pyraminx 1st", 5, 0, 40, 3)
selectscrambler("333ft", 1, "Feet 1st", 3, 0, 20, 2)
selectscrambler("333ft", "f", "Feet Final", 0, 0, 20, 1)
selectscrambler("333bf", 1, "Blindfolded 1st", 3, 0, 40, 2)
selectscrambler("skewb", 2, "Skewb 2nd 1", 4, 0, 50, 2)
selectscrambler("pyram", 2, "Pyraminx 2nd", 4, 0, 50, 2)
selectscrambler("333oh", 1, "One-Handed 1st", 5, 0, 50, 3)
selectscrambler("444", 1, "444 1st", 5, 0, 40, 4)
selectscrambler("clock", "f", "Clock Final", 4, 14, 25, 1)
selectscrambler("sq1", "f", "Square-1 Final", 3, 20, 30, 1)
selectscrambler("skewb", "f", "Skewb Final", 3, 20, 30, 1)
selectscrambler("pyram", "f", "Pyraminx Final", 3, 20, 30, 1)
selectscrambler("333oh", 2, "One-Handed 2nd", 4, 0, 50, 2)

selectscrambler("555", 2, "555 2nd", 5, 0, 40, 2)
selectscrambler("444", 2, "444 2nd", 5, 0, 45, 2)
selectscrambler("333", 1, "333 1st", 5, 0, 70, 5)
selectscrambler("222", 1, "222 1st", 4, 0, 60, 4)
selectscrambler("333", 2, "333 2nd", 4, 0, 70, 4)
selectscrambler("222", 2, "222 2nd", 4, 0, 60, 2)
selectscrambler("555", "f", "555 Final", 4, 20, 30, 1)
selectscrambler("333bf", "f", "Blindfolded Final", 3, 20, 40, 1)
selectscrambler("333", 3, "333 Semi", 3, 0, 40, 1)
selectscrambler("333oh", "f", "One-Handed Final", 4, 0, 50, 1)
selectscrambler("222", "f", "222 Final", 3, 20, 30, 1)
selectscrambler("444", "f", "444 Final", 3, 20, 30, 1)


### Preparation Grouping
def groupcount(number,groups):
    return round(number/groups, 0)

# Grouping for all events with given number of groups
def grouping(row, groups, column):
    eventcount = 0
    for k in row:
        if k[column] == "1":
            eventcount += 1
    
    res = groupcount(eventcount, groups)    # Average number of competitors per group
    l = 1
    m = 0           # Count of groups
    counter = 0
    for k in range(0, len(row)):
        if row[k][column] == "1":
            if (l-1) % res == 0:
                m += 1
                if m > groups:
                    m -= 1
            resultstring[counter] = resultstring[counter] + (m,)       # Adding group number for competitors
            l += 1
        else:
            group = ("",)
            resultstring[counter] = resultstring[counter] + ("",)      # Leaving group empty if competitors doesn't compete
        counter += 1

# Collects all rankings from SQL-string for choosen event
def geteventresults(eventranking, rows, event):
    for k in rows:
        if event == k[1]:
            eventranking.append(k)

# Selects correct ranking for choosen event
def rankings(eventranking, resultstring, ranking, event):

    geteventresults(eventranking, rows, event)
    for k in range(0,len(resultstring)):
        true = 0
        for l in eventranking:
            if resultstring[k][2] == l[0]:
                ranking[k] = ranking[k] + (l[2],)
                true = 1
                break
        if not true:
            ranking[k] = ranking[k] + (99999,)


# Get data from cubecomp.de csv-export
file = open('test.txt')
alldata = []

for row in file:
    list = row.split(',')
    list[24] = list[24].replace("\n", "")
    alldata.append((list))

row = sorted(alldata, key=lambda x: x[1])


# Create new string for grouping and add name + DOB
resultstring = []

for k in row:
    resultstring.append((k[1], k[2], k[3]))


### Preparation Scrambling
rowcount = 3 # first column with grouping-data

# Selects scramblers for each group and creates grouping
def selectscrambler(event, roundnumber, roundid, scrambler, firstplace, lastplace, groups):
    global rowcount
    ranking = []
    eventranking = []

    for k in row:
        ranking.append((k[1], k[3]))
    
    rankings(eventranking, resultstring, ranking, event)
    ranking = sorted(ranking, key = lambda x:x[2])
    
    # Adds correct columnid for events AND creates grouping for first rounds
    if roundnumber == 1:
        grouping(row, groups, columnids[event])
        newgrouping = {event: rowcount}
        eventids.update(newgrouping)
        rowcount += 1

    # Actual grouping happens here
    for n in range(1,groups+1):
        scramblerlist.append([roundid, n])
        for l in range(0,len(scramblerlist)):
            if scramblerlist[l][0] == roundid:      # Only finishes after enough scramblers are in list
                while len(scramblerlist[l]) < (scrambler + 2):
                    rank = random.choice(range(firstplace, lastplace))

                    if roundnumber == 1 or roundnumber == "f":
                        notdouble = checking(ranking, eventids, event, groups, roundnumber, rank, n, l)

                        if notdouble:
                            scramblerlist[l].append(ranking[rank][0])
                    else:
                        notdouble = checking2(ranking, eventids, event, groups, roundnumber, rank, n, l, firstplace, lastplace)

                        if notdouble:
                            scramblerlist[l].append(ranking[rank][0])


# 2 checks if scrambler can be used
# Check 1 for 1st rounds and finals
# Not possible if scrambler in same group, scrambler not registered for event or already scrambler in this group
def checking(ranking, eventids, event, groups, roundnumber, rank, n, l):
    notdouble = 1
    for k in resultstring:
        if k[0] == ranking[rank][0] and groups > 1:
            if not k[eventids[event]]:
                notdouble = 0
            if k[eventids[event]] == n:
                notdouble = 0
            
    for m in range(0, len(scramblerlist[l])):
        if ranking[rank][0] == scramblerlist[l][m]:
            notdouble = 0

    return notdouble       # notdouble == 1: scrambler can be added to list, notdouble == 0: try another scrambler


# Check 2 for 2nd/3rd rounds
# Need to distinguish between fast and slow cubers for earlier and later rounds (e.g. fast people scramble group 1, slow people group 2)
def checking2(ranking, eventids, event, groups, roundnumber, rank, n, l, firstplace, lastplace):
    notdouble = 1
    if n <= round(groups/2, 0) and rank < round(lastplace/2, 0):
        for k in resultstring:
            if k[0] == ranking[rank][0] and groups > 1:
                if not k[eventids[event]]:
                    notdouble = 0
        for m in range(0, len(scramblerlist[l])):
            if ranking[rank][0] == scramblerlist[l][m]:
                notdouble = 0
    elif n >= round(groups/2, 0) and rank >= round(lastplace/2, 0):
        for k in resultstring:
            if k[0] == ranking[rank][0] and groups > 1:
                if not k[eventids[event]]:
                    notdouble = 0
        for m in range(0, len(scramblerlist[l])):
            if ranking[rank][0] == scramblerlist[l][m]:
                notdouble = 0
    else:
        notdouble = 0

    return notdouble


# Connect to WCA-DB
conn = pymysql.connect(host='db.suushiemaniac.com',
                       unix_socket='/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock',
                       user='wca',
                       passwd='db',
                       db='wca-export'
                       )

cur = conn.cursor()
cur.execute("SELECT * FROM RanksAverage")
    
rows = cur.fetchall()

eventids = {"333": 999, "222": 999, "444": 999, "555": 999, "666": 999, "777": 999, "333bf": 999, "333fm": 999, "333oh": 999, "333ft": 999, "minx": 999, "pyram": 999, "clock": 999, "skewb": 999, "sq1": 999, "444bf": 999, "555bf": 999, "333mbf": 999}       # eventids in scrambling-string (added in selectscrambler()
columnids = {"333": 8, "222": 7, "444": 14, "555": 16, "666": 18, "777": 19, "333bf": 9, "333fm": 10, "333oh": 13, "333ft": 11, "minx": 21, "pyram": 22, "clock": 20, "skewb": 23, "sq1": 24, "444bf": 15, "555bf": 17, "333mbf": 12}           # columnids in grouping-string

scramblerlist = []

# place for selectscrambler()

# Add columns for events with < 5 scramblers
for k in range(0,len(scramblerlist)):
    while len(scramblerlist[k]) < 7:
        scramblerlist[k].append("")


### Write grouping and scrambling in separate files
sys.stdout=open("scrambling.csv","w")
header = "Event, Group, Scrambler 1, Scrambler 2, Scrambler 3, Scrambler 4, Scrambler 5"

print(header)

for k in scramblerlist:
    print(k[0], ",", k[1], ",", k[2], ",", k[3], ",", k[4], ",", k[5], ",", k[6])

sys.stdout.close()

sys.stdout=open("grouping.csv","w")
header = ', Name, 333, 222, 444, 555, 666, 777, 333bf, 333fm, 333oh, 333ft, megaminx, pyraminx, clock, skewb, sq1, 444bf, 555bf, 333mbf'

print(header)
l = 0
for k in resultstring:
    l += 1
    print(l, ",", k[0], ",", k[eventids["333"]], ",", k[eventids["222"]], ",", k[eventids["444"]], ",", k[eventids["555"]], ",", k[eventids["666"]], ",", k[eventids["777"]], ",", k[eventids["333bf"]], ",", k[eventids["333fm"]], ",", k[eventids["333oh"]], ",", k[eventids["333ft"]], ",", k[eventids["minx"]], ",", k[eventids["pyram"]], ",", k[eventids["clock"]], ",", k[eventids["skewb"]], ",", k[eventids["sq1"]], ",", k[eventids["444bf"]], ",", k[eventids["555bf"]], ",", k[eventids["333mbf"]])
    if l % 32 == 0:
        print(header)
        print(header)

sys.stdout.close()

cur.close()
conn.close()
