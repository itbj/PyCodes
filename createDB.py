import sqlite3

conn = sqlite3.connect("music.db")
cursor = conn.cursor()

#Create table "albums"
cursor.execute("""CREATE TABLE albums
				(title text, artis text, release_date text,
				 publisher text, media_type text)
				""")

#Insert some data
cursor.execute("INSERT INTO albums VALUES ('Glow', 'Andy Hunter','7/24/2012','Xplore Records','MP3')")

#Save data to database
conn.commit()

#Insert multiple records using the more secure "?" method
albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
          ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
          ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
          ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]

cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
conn.commit()

