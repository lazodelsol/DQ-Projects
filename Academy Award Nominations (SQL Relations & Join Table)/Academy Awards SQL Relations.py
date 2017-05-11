
# coding: utf-8

# In[1]:

import sqlite3
conn = sqlite3.connect("nominations.db")
schema = conn.execute("pragma table_info(nominations);").fetchall()
first_ten = conn.execute("SELECT * from nominations LIMIT 10;").fetchall()
for item in schema:
    print(item)
for item in first_ten:
    print(item)


# In[2]:

create_table = "CREATE TABLE ceremonies(id integer PRIMARY KEY, Year integer, Host text)"
conn.execute(create_table)


# In[ ]:

years_hosts = [(2010, "Steve Martin"),
               (2009, "Hugh Jackman"),
               (2008, "Jon Stewart"),
               (2007, "Ellen DeGeneres"),
               (2006, "Jon Stewart"),
               (2005, "Chris Rock"),
               (2004, "Billy Crystal"),
               (2003, "Steve Martin"),
               (2002, "Whoopi Goldberg"),
               (2001, "Steve Martin"),
               (2000, "Billy Crystal"),
            ]
insert_query = "INSERT INTO ceremonies (Year, Host) VALUES (?, ?);"


# In[ ]:

conn.executemany(insert_query, years_hosts)


# In[ ]:

schema = conn.execute("pragma table_info(ceremonies);").fetchall()
first_ten = conn.execute("SELECT * FROM ceremonies LIMIT 10;").fetchall()


# In[ ]:

for item in schema:
    print(item)
for item in first_ten:
    print(item)


# In[ ]:

conn.execute("PRAGMA foreign_keys = ON;")


# In[ ]:

create_table_two = "CREATE TABLE nominations_two(id integer PRIMARY KEY, category text, nominee text, movie text, character text, won integer, ceremony_id integer, FOREIGN KEY (ceremony_id) REFERENCES ceremonies(id));"
conn.execute(create_table_two)


# In[ ]:

combined_fields = "SELECT nominations.category as category, nominations.nominee as nominee, nominations.movie as movie, nominations.character as character, nominations.won as won, ceremonies.id as ceremony_id FROM nominations INNER JOIN ceremonies ON nominations.year == ceremonies.year;"
joined_nominations = conn.execute(combined_fields).fetchall()


# In[ ]:

insert_nominations_two = "INSERT INTO nominations_two (category, nominee, movie, character, won, ceremony_id) VALUES (?, ?, ?, ?, ?, ?);"
conn.executemany(insert_nominations_two, joined_nominations)


# In[ ]:

print(conn.execute("select * from nominations_two limit 5;").fetchall())


# In[ ]:

conn.execute("DROP TABLE nominations;")


# In[ ]:

conn.execute("ALTER TABLE nominations_two RENAME TO nominations")


# In[ ]:

create_movies = "CREATE TABLE movies(id integer PRIMARY KEY, movie text);"
create_actors = "CREATE TABLE actors(id integer PRIMARY KEY, actor text);"
create_movies_actors = "CREATE TABLE movies_actors(id integer PRIMARY KEY, movie_id integer, actor_id integer, FOREIGN KEY (movie_id) REFERENCES movies(id), FOREIGN KEY (actor_id) REFERENCES actors(id));"


# In[ ]:

conn.execute(create_movies)
conn.execute(create_actors)
conn.execute(create_movies_actors)


# In[4]:

insert_movies = "INSERT INTO movies (movie) SELECT distinct movie from nominations;"
insert_actors = "INSERT INTO actors (actor) SELECT distinct nominee from nominations;"
conn.execute(insert_movies)
conn.execute(insert_actors)

print(conn.execute("select * from movies limit 5;").fetchall())
print(conn.execute("select * from actors limit 5;").fetchall())


# In[5]:

pairs_query = "SELECT movie,nominee FROM nominations;"
movie_actor_pairs = conn.execute(pairs_query).fetchall()

join_table_insert = "INSERT INTO movies_actors (movie_id, actor_id) values ((select id from movies where movie == ?),(select id from actors where actor == ?));"
conn.executemany(join_table_insert,movie_actor_pairs)

print(conn.execute("select * from movies_actors limit 5;").fetchall())

