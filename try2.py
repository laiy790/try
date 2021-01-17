import requests
import sqlite3
conn = sqlite3.connect('try2.sqlite')
cursor = conn.cursor()
url = 'https://www.numbeo.com/crime/rankings_current.jsp'
html = requests.get(url)
html.encoding = 'big5'
sqlstr ='CREATE TABLE "table01" ("Rank"  INTEGER PRIMARY KEY NOT NULL,\
"City"   TEXT,\"Crime"  TEXT,\"Safety"  TEXT)'
cursor.execute(sqlstr)
conn.commit()
conn.close()
