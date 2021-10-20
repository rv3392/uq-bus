import os
import subprocess
import schedule
import time

GTFS_ZIP_FILE = "gtfs.zip"
GTFS_SCHEDULE_URL = os.environ["GTFS_SCHEDULE_URL"]
GTFS_SCRIPT_NAME = "./gtfsdb/bin/gtfsdb-load"

DB_HOST = os.environ["DB_HOST"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_PORT = os.environ["DB_PORT"]

def load_data(url):
    script_call = [
        GTFS_SCRIPT_NAME,
        "--database_url", "postgresql://" + DB_USER + ":" + DB_PASSWORD +
                "@" + DB_HOST + ":" + DB_PORT,
        url
    ]
    proc = subprocess.Popen(script_call, stdout=subprocess.PIPE)
    proc.wait()

load_data(GTFS_SCHEDULE_URL)

schedule.every().day.at("01:00").do(load_data, GTFS_SCHEDULE_URL)
while True:
    schedule.run_pending()
    time.sleep(6000)


