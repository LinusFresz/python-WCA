#!/usr/bin/python

import pymysql

conn = pymysql.connect(host='127.0.0.1',
                       unix_socket='/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock',
                       user='root',
                       passwd=None,
                       db='wca')


cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute("SELECT eventId, personId, best FROM RanksSingle WHERE eventId = '333bf' GROUP BY personId")

bld = cur.fetchall()

cur.execute("SELECT eventId, personId, best FROM RanksSingle WHERE eventId = '444bf' GROUP BY personId")

fobf = cur.fetchall()

cur.execute("SELECT eventId, personId, best FROM RanksSingle WHERE eventId = '555bf' GROUP BY personId")

fibf = cur.fetchall()

#Check for 5BLD > 4BLD if 4BLD success
print('5BLD > 4BLD:')
for i in range(0,len(fobf)):
    for k in range(0,len(fibf)):
        if fobf[i]['personId'] == fibf[k]['personId']:
            if fobf[i]['best'] > fibf[k]['best']:
                print(fobf[i]['personId'], fobf[i]['best'], fibf[k]['best'])

#Check for 4BLD > 3BLD if 3BLD success
print('4BLD > 3BLD:')
for i in range(0,len(bld)):
    for k in range(0,len(fobf)):
        if bld[i]['personId'] == fobf[k]['personId']:
            if bld[i]['best'] > fobf[k]['best']:
                print(bld[i]['personId'], bld[i]['best'], fobf[k]['best'])

#Check for 5BLD > 3BLD if 3BLD success
print('5BLD > 3BLD:')
for i in range(0,len(bld)):
    for k in range(0,len(fibf)):
        if bld[i]['personId'] == fibf[k]['personId']:
            if bld[i]['best'] > fibf[k]['best']:
                print(bld[i]['personId'], bld[i]['best'], fibf[k]['best'])


#Check for 4BLD success without 3BLD success
print('4BLD without 3BLD:')
for k in range(0,len(fobf)):
    if (all(fobf[k]['personId'] != bld[i]['personId'] for i in range(0,len(bld)))):
        print(fobf[k]['personId'], fobf[k]['best'])

#Check for 5BLD success without 3BLD success
print('5BLD without 3BLD:')
for k in range(0,len(fibf)):
    if (all(fibf[k]['personId'] != bld[i]['personId'] for i in range(0,len(bld)))):
        print(fibf[k]['personId'], fibf[k]['best'])

#Check for 5BLD success without 4BLD success
print('5BLD without 4BLD:')
for k in range(0,len(fibf)):
    if (all(fibf[k]['personId'] != fobf[i]['personId'] for i in range(0,len(fobf)))):
        print(fibf[k]['personId'], fibf[k]['best'])




cur.close()
conn.close()



