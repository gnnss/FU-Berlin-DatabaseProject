import csv
import psycopg2

# Connect to  DB election
try:
    connect_str = "dbname='election' user='' password='' host='localhost'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    reader = csv.reader(open('lastFinalFile.csv', 'rb'))
    print("connected")
except:
    print(Exception)
    print("not Connected")

try:
    cursor.execute("""COPY file FROM '/Desktop/American-Election-Tweets/lastFinalFile.csv' DELIMITERS ';' CSV HEADER""")
    print("second step succeeded")
except:
    print("second step failed")
