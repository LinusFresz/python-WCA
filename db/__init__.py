from db.Database import Database
from static.config import credentials

WCA_Database = Database(
        credentials['db'],
        credentials['host'],
        credentials['user'],
        credentials['passwd'],
        socket=credentials.get('socket', None),
        port=credentials.get('port', 3306)
    )
