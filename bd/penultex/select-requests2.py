import sqlalchemy
db = "postgresql://ruslan:ru13aaogh06(@localhost:5432/dbhomework"
engine = sqlalchemy.create_engine(db)
connection = engine.connect()
#количество исполнителей в каждом жанре;
connection.execute("""SELECT g.name, COUNT(performers) FROM genre g
LEFT JOIN performe_genre p_g ON genre.id = p_g.id
LEFT JOIN performers p ON author_id = p.id;
""")
#количество треков, вошедших в альбомы 2019-2020 годов
connection.execute("""SELECT s.name, COUNT(s) FROM albums a
LEFT JOIN songs s ON s.albumid = a.id
WHERE a.year_of_issue BETWEEN 2019 and 2020;
""")
#средняя продолжительность треков по каждому альбому
connection.execute("""SELECT s.duration, AVG(s.duration) FROM albums a
LEFT JOIN songs s ON s.albumid = a.id;
""")
#все исполнители, которые не выпустили альбомы в 2020 году
connection.execute("""SELECT p.name FROM performers p
LEFT JOIN performers_album p_a ON p.id = p_a.author_id
LEFT JOIN albums a ON a.id = p_a.album_id
WHERE NOT a.year_of_issue = 2020;
""")
#названия сборников, в которых присутствует конкретный исполнитель Feduk
connection.execute("""SELECT c.name FROM collection c
LEFT JOIN coll_of_songs cs ON c.id = cs.coll_id
LEFT JOIN songs s ON s.id = cs.song_id
LEFT JOIN albums a ON a.id = s.albumid
LEFT JOIN performers_album pa ON pa.album_id = a.id
LEFT JOIN performers p ON p.id = pa.author_id
WHERE p.name LIKE 'Feduk';
""")
#название альбомов, в которых присутствуют исполнители более 1 жанра
connection.execute("""SELECT a.name FROM albums a
LEFT JOIN performers_album pa ON pa.album_id = a.id
LEFT JOIN performers p ON p.id = pa.author_id
LEFT JOIN performe_genre pg ON pg.author_id = p.id
LEFT JOIN genre g ON g.id = pg.genre_id
GROUP BY a.name 
HAVING COUNT(g.name) > 1""")
#наименование треков, которые не входят в сборники
connection.execute("""SELECT s.name FROM songs s
LEFT JOIN coll_of_songs cs ON cs.song_id = s.id
WHERE cs.song_id is null""")
#исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
connection.execute("""SELECT p.name, s.duration FROM songs s
LEFT JOIN albums a ON a.id = s.albumid
LEFT JOIN performers_album pa ON pa.album_id = a.id
LEFT JOIN performers p ON p.id = pa.author_id
GROUP BY p.name, s.duration
HAVING s.duration = (SELECT MIN(s.duration) FROM songs);
""")
#название альбомов, содержащих наименьшее количество треков
connection.execute("""SELECT a.name FROM albums a
LEFT JOIN songs s ON s.albumid = a.id
WHERE in (
    select album_id
    from tracks
    group by album_id
    having count(id) = (
        select count(id)
        from tracks
        group by album_id
        order by count
        limit 1)
        )
""")
