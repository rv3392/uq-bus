import os
import subprocess
import schedule
import sys
import time

GTFS_ZIP_FILE = "gtfs.zip"
GTFS_TRIP_UPDATE_URL = os.environ["GTFS_TRIP_UPDATE_URL"]
GTFS_SERVICE_ALERT_URL = os.environ["GTFS_SERVICE_ALERT_URL"]
GTFS_VEHICLE_POSITIONS_URL = os.environ["GTFS_VEHICLE_POSITIONS_URL"]
GTFS_SCRIPT_NAME = "./gtfsrdb/gtfsrdb.py"

DB_HOST = os.environ["DB_HOST"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_PORT = os.environ["DB_PORT"]

DB_URI = "postgresql+psycopg2://" + DB_USER + ":" + DB_PASSWORD + \
                "@" + DB_HOST + ":" + DB_PORT + "/" + DB_USER

def load_data():
    script_call = [
        sys.executable,
        GTFS_SCRIPT_NAME,
        "-t", GTFS_TRIP_UPDATE_URL,
        "-a", GTFS_SERVICE_ALERT_URL,
        #"-p", GTFS_VEHICLE_POSITIONS_URL,
        "-d", DB_URI,
        "-c", "-o",
    ]
    proc = subprocess.Popen(script_call)
    proc.wait()

load_data()

schedule.every().minutes.do(load_data)
while True:
    schedule.run_pending()
    time.sleep(55)


