import psycopg2

myDbname = "HerAiDatabaseExample"
myUser = "username"
myHost = "localhost"
myPassword = "Hockey#7"
portNum = 5432

conn = psycopg2.connect("dbname={myDbname} user={myUser} password={myPassword} host={localhost} port={portNum}")

cursor = conn.cursor()

cursor.execute("""SELECT * from HerAiLocal.public.Users""")

rows = cursor.fetchall()

print("\nShow me the databases:\n")
for row in rows:
    print("{0}, {1} ", row[0], row[1])
