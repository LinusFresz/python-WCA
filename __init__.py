from pathlib import Path

conf = Path("static/config.py")

if not conf.is_file():
    print("""
        No current configuration file found.
        Please create a file 'config.py' in 'static' directory
        with the following dictionary as contents:
        
        credentials = {
            'host': 'host_for_mysql',
            'db': 'database_name',
            'user': 'database_user',
            'passwd': 'database_password'
        }
    """)
    exit(255)
