################################################
## Alejandro Hernandez		                 ###
## Project v2 | Python Version 3.4.2		 ###
## Last Edited 2/18/2015					 ###
################################################
import sqlite3
import datetime

################################################
### Part 1 Create/Load tables                ###
################################################

#------------------------------------------------------------------------------
# first, create the tables associated with movies.dat file
print('Part 1 ------------------------------------------------------------------------')

f = open('movies.dat', 'r')

con = sqlite3.connect('movies.db')
cur = con.cursor()
cur.execute('DROP TABLE movies')
print('Creating tables: movies, movie_categories, and categories')
cur.execute('CREATE TABLE movies (movie_id int PRIMARY KEY CHECK(movie_id BETWEEN 1 AND 3952), movie_title text, year int)')
cur.execute('DROP TABLE movie_categories')
cur.execute('CREATE TABLE movie_categories (movie_id int, category_id text, PRIMARY KEY(movie_id, category_id), FOREIGN KEY(movie_id) REFERENCES movies(movie_id), FOREIGN KEY(category_id) REFERENCES categories(category_id))')
cur.execute('DROP TABLE categories')
cur.execute('CREATE TABLE categories (category_id int PRIMARY KEY, genre_desc text)')
con.commit()

print('Reading data...')
no_movies = 0       # keeps track of number of movies
no_movie_cats = 0   # tracks number of records in movie_categories
cat_id = 1
for line in f:
    l = line.split("::")
    l_len = len(l)

    movie_id    = l[0]          # int
    movie_title = l[1][0:-7]    # text
    year        = l[1][-5:-1]   # int

    # inserts values into movies table
    cur.execute("INSERT INTO movies VALUES (?, ?, ?)", (movie_id, movie_title, year))

    # next bit of code will create the categories table "on the fly"
    # and will inserts values into movie_categories table
    categories   = l[2]
    if categories[-1] == '\n': 
        categories = l[2][:-1]
    genre = categories.split("|")

    i = 0
    while(i < len(genre)):
        cat = genre[i]
        cur.execute('SELECT category_id FROM categories WHERE genre_desc = ?', (cat,))
        x = cur.fetchall()
        if len(x) == 0:
            cur.execute('INSERT INTO categories VALUES (?, ?)', (cat_id, cat))
            cur.execute('INSERT INTO movie_categories VALUES (?, ?)',(movie_id, cat_id))
            cat_id += 1
        else:
            c_id = x[0][0]
            cur.execute("INSERT INTO movie_categories VALUES (?, ?)", (movie_id, c_id))
        i += 1

        no_movie_cats += 1        
    no_movies += 1

con.commit()

print ('Number of records entered into movies table: ' + str(no_movies))
print ('Number of records entered into movie_categories table: ' + str(no_movie_cats))

cur.execute('SELECT COUNT(*) FROM categories')
y=cur.fetchall()
cat_count = y[0][0]
print ('Number of records entered into categories table: ' + str(cat_count) +'\n')

con.close()
f.close()

#------------------------------------------------------------------------------
# create the additional age and occupation tables
con = sqlite3.connect('movies.db')
cur = con.cursor()
cur.execute('DROP TABLE age')
cur.execute('CREATE TABLE age(age_id int PRIMARY KEY, age_desc text)')
print('Creating tables: age and occupation')
cur.execute('DROP TABLE occupation')
cur.execute('CREATE TABLE occupation(occupation_id int PRIMARY KEY, occupation_desc text)')

print('Reading data...')
age = [1,18,25,35,45,50,56]
age_desc = ['Under 18','18-24','25-34','35-44','45-49','50-55','56+']
j = 0
while(j<len(age)):
    cur.execute('INSERT INTO age VALUES(?, ?)', (age[j],age_desc[j]))
    j += 1

occupation_desc = ['"other" or not specified', 'academic/educator', 'artist', 'clerical/admin',
                    'college/grad student', 'customer service', 'doctor/health care', 'executive/managerial',
                   'farmer', 'homemaker', 'K-12 student', 'lawyer', 'programmer', 'retired', 'sales/marketing',
                  'scientist', 'self-employed', 'technician/engineer', 'tradesman/craftsman', 'unemployed','writer']
k = 0
while(k<len(occupation_desc)):
    cur.execute('INSERT INTO occupation VALUES(?, ?)', (k, occupation_desc[k]))
    k += 1
    
cur.execute('SELECT COUNT(*) FROM age')
y=cur.fetchall()
age_count = y[0][0]
print ('Number of records entered into age table: ' + str(age_count))

cur.execute('SELECT COUNT(*) FROM occupation')
z=cur.fetchall()
occ_count = z[0][0]
print ('Number of records entered into occupation table: ' + str(occ_count) + '\n')
    
con.commit()    
con.close()

#------------------------------------------------------------------------------
# creates the users table
f = open('users.dat','r')
    
con = sqlite3.connect('movies.db')
cur = con.cursor()
cur.execute('DROP TABLE users')
print('Creating table: users')
cur.execute('CREATE TABLE users (user_id int PRIMARY KEY CHECK(user_id BETWEEN 0 AND 6040), gender text, age int, occupation int, zip_code text, FOREIGN KEY(occupation) REFERENCES occupation(occupation_id), FOREIGN KEY(age) REFERENCES age(age_id))')

print('Reading data...')
no_users = 0
for line in f:
    l =  line.split('::')

    user_id     = l[0] # int
    gender      = l[1] # text
    age         = l[2] # int
    occupation  = l[3] # int
    zip_code    = l[4] # text
    if zip_code[-1] == '\n':
        zip_code = zip_code[:-1]

    cur.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (user_id, gender, age, occupation, zip_code))
    no_users += 1

print ('Number of records entered into users table: ' + str(no_users) + '\n')
con.commit()
con.close()
f.close()

#------------------------------------------------------------------------------
# creates the Ratings table
f = open('ratings.dat','r')

con = sqlite3.connect('movies.db')
cur = con.cursor()
cur.execute('DROP TABLE ratings')
print('Creating table: ratings')
cur.execute('CREATE TABLE ratings (user_id int, movie_id int, rating int CHECK(rating BETWEEN 0 AND 5), time_stamp text, date text, FOREIGN KEY(user_id) REFERENCES users(user_id), FOREIGN KEY(movie_id) REFERENCES users(movie_id))')

print('Reading data...')
no_ratings = 0
for line in f:
    l =  line.split('::')

    user_id     = l[0] # int
    movie_id    = l[1] # int
    rating      = l[2] # int
    time_stamp  = l[3] # text
    if time_stamp[-1] == '\n':
        time_stamp = time_stamp[:-1]

    date = datetime.datetime.fromtimestamp(int(time_stamp)).strftime('%Y-%m-%d')
    
    cur.execute("INSERT INTO ratings VALUES (?, ?, ?, ?, ?)", (user_id, movie_id, rating, time_stamp, date))
    no_ratings += 1

print ('Number of records entered into ratings table: ' + str(no_ratings) + '\n')
con.commit()
con.close()
f.close()
