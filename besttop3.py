#!/usr/bin/python

import pymysql
import sys

# Print table
def table(rank):
    sys.stdout=open("besttop3.txt","w")
    print('[spoiler=Best top 3]')
    print('[table]')
    print('[tr][td][td]Sum of averages[/td][td]round[/td][td]Competition[/td][/tr]')
    # If more than 100 people have an average, just take top 100
    for k in range(0, len(rank)):
        i = k+1
        for l in range(0,k):
            if rank[k][0] == rank[k-l][0]:
                i = k-l+1
        print('[tr][td]', i, '[/td][td]', rank[k][0],'[/td][td]', rank[k][2], '[/td][td]', rank[k][1], '[/td][/tr]')
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
cur.execute("SELECT best, average, pos, competitionId, eventId, roundId FROM Results WHERE (pos = 1 or pos = 2 or pos = 3) AND eventId = '333' GROUP BY competitionId, roundId, average")


rows = cur.fetchall()


# Adding the results of top3 of this round and sorting by lowest sum
res = []

for i in range(0,len(rows)):
    sum = 0
    if rows[i]['pos'] == 1 and rows[i]['average'] != 0:
        for k in range(i,i+3):
            sum = sum + rows[k]['average']
        res.append((sum, rows[i]['competitionId'], rows[i]['roundId']))
    else:
        continue

sorted_x = sorted(res, key=lambda x:x[0])


# Counting the best averages for each round-type
fircoun = 0
seccoun = 0
thicoun = 0
fincoun = 0
dafuq = 0

for i in range(0, 250):
    
    if sorted_x[i][2] == '1' or sorted_x[i][2] == 'a' or sorted_x[i][2] == '0' or sorted_x[i][2] == 'd':
        fircoun = fircoun + 1
    elif sorted_x[i][2] == '2' or sorted_x[i][2] == 'b':
        seccoun = seccoun + 1
    elif sorted_x[i][2] == '3' or sorted_x[i][2] == 'c':
        thicoun = thicoun + 1
    elif sorted_x[i][2] == '4' or sorted_x[i][2] == 'f':
        fincoun = fincoun + 1
    else:
        dafuq = dafuq + 1

give = [fircoun, seccoun, thicoun, fincoun]


# Print final results + generate results table
for i in range(0,len(give)):
    print('Best averages in round', i+1, ':', give[i])

table(sorted_x)


cur.close()
conn.close()



