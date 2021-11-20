import sqlalchemy
db = "postgresql://ruslan:ru13aaogh06(@localhost:5432/dbhomework"
engine = sqlalchemy.create_engine(db)
connection = engine.connect()
connection.execute("""SELECT name, year_of_issue from albums
WHERE year_of_issue = 2018;
""").fetchall()
connection.execute("""SELECT name, duration from songs
ORDER BY duration DESC
LIMIT 1;
""").fetchall()
connection.execute("""SELECT name, duration from songs
WHERE duration >= 3.5;
""").fetchall()
connection.execute("""SELECT name from collection
WHERE year_of_issue BETWEEN 2018 and 2020;
""").fetchall()
connection.execute("""SELECT name from performers
WHERE not name LIKE '%% %%';
""").fetchall()
connection.execute("""SELECT name from songs
WHERE name LIKE '%%my';
""").fetchall()