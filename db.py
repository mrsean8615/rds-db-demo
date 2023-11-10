import mysql.connector
import pandas as pd
import os


mydb = mysql.connector.connect(
    host = "rds-db-project-4.cvrkscuruxt3.us-west-1.rds.amazonaws.com",
    user = "admin",
    password = "Pikachu23343!",
    port = "3306",
    database = "data"
)

sql = "SELECT Team, player, opponent, position, champion, kills FROM leagueStats;"
cursor = mydb.cursor()
cursor.execute(sql)
result = cursor.fetchall()
# print(result)

df = pd.DataFrame()
for x in result:
    df2 = pd.DataFrame(list(x)).T
    df = pd.concat([df, df2])

df.to_html('index.html')