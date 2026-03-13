import psycopg2
conn = psycopg2.connect(dbname="postgres",user="postgres", password="Gautam",host="localhost",port="5432")

cursor = conn.cursor()
cursor


print("Connected Successfully")