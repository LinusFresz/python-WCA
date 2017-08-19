#!/usr/bin/python

import sys


def groupcount(number,groups):
    return int(round(number/groups, 0))


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
            resultstring[counter] = resultstring[counter] + (m,)       # Adding group number for competitors
        
            l += 1
        else:
            group = ("",)
            resultstring[counter] = resultstring[counter] + ("",)      # Leaving group empty if competitors doesn't compete

        counter += 1

    

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


# Grouping for this years German Nationals

# grouping(source, groups, column of source)
grouping(row, 5, 8)
grouping(row, 4, 7)
grouping(row, 4, 14)
grouping(row, 3, 16)
grouping(row, 2, 18)
grouping(row, 2, 19)
grouping(row, 2, 9)
grouping(row, 1, 10)
grouping(row, 3, 13)
grouping(row, 2, 11)
grouping(row, 2, 21)
grouping(row, 3, 22)
grouping(row, 2, 20)
grouping(row, 3, 23)
grouping(row, 2, 24)
grouping(row, 1, 15)
grouping(row, 1, 17)
grouping(row, 1, 12)


# Write grouping in file
sys.stdout=open("grouping.csv","w")
header = ', Name, 333, 222, 444, 555, 666, 777, 333bf, 333fm, 333oh, 333ft, megaminx, pyraminx, clock, skewb, sq1, 444bf, 555bf, 333mbf'


print(header)

l = 0
for k in resultstring:
    l += 1
    print(l, ",", k[0], ",", k[3], ",", k[4], ",", k[5], ",", k[6], ",", k[7], ",", k[8], ",", k[9], ",", k[10], ",", k[11], ",", k[12], ",", k[13], ",", k[14], ",", k[15], ",", k[16], ",", k[17], ",", k[18], ",", k[19], ",", k[20])
    if l % 25 == 0:
        print(header)

sys.stdout.close()
