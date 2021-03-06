# python

A lot of cool stats for the WCA-database done by me, Linus! Mostly Python + SQL.

Look at 'SQL-collection' for some cool SQL-queries you can use on your own.

## Setup

In order to use most of the files, you need a database connection.
Since I do not want to disclose my private connection details to you,
you need to create a static config.

Create directory `static` in project root and add `config.py` with the following dictionary contents:
```python
credentials = {
    'host': 'localhost',
    'db': 'local_database',
    'user': 'JohnDoe',
    'passwd': 'password123',
    'port': 3306,
    'socket': '/path/to/unix/socket'
}
```

The keys for `port` and `socket` are optional

## See the newest posts:

- Most official Solves 2017: https://hackmd.io/s/BybI0LPIZ, August 2017
- PB-streaks: https://www.speedsolving.com/forum/threads/odd-wca-stats-stats-request-thread.26121/page-229#post-1207284, database: 30.11.2016, done with pbstreak.py
Update August 2017: https://hackmd.io/s/HkSiyxW8Z
- Competition Streak without podiums: https://www.speedsolving.com/forum/threads/odd-wca-stats-stats-request-thread.26121/page-229#post-1207222, database: 28.11.2016, done with streakwithoutpodiums.py
- Best fourth place in every event: https://www.speedsolving.com/forum/threads/odd-wca-stats-stats-request-thread.26121/page-228#post-1206981, database: 28.11.2016, done with besttop4.py and besttop4-average.py
- Best 4. place for FMC (single and mean): https://www.speedsolving.com/forum/threads/the-fmc-thread.13599/page-198#post-1206825, database: 28.11.2016, done with best4place.py
- Best sum of top3 in 3x3, not only finals: https://www.speedsolving.com/forum/threads/odd-wca-stats-stats-request-thread.26121/page-228#post-1206822, database: 28.11.2016, done with besttop3.py
- Longstest DNF-streaks between two successes for 3BLD, 4BLD and 5BLD: https://www.speedsolving.com/forum/threads/odd-wca-stats-stats-request-thread.26121/page-228#post-1206341, database: 25.11.2016, done with success-dnf-streak.py
- FMC rolling averages (mean of 3, average of 5, 12, 25 and 50): https://www.speedsolving.com/forum/threads/odd-wca-stats-stats-request-thread.26121/page-228#post-1206236, database: 23.11.2016, done with fmcmean.py
- Comparison between 3BLD, 4BLD and 5BLD times: https://www.speedsolving.com/forum/threads/odd-wca-stats-stats-request-thread.26121/page-228#post-1206087, database: 23.11.2016, done with bigbldcomparison.py and successstreak.py
