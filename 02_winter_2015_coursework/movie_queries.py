import sqlite3
import sys
"""
file = 'user_info2.txt'
outfile = open(file,'w')

con = sqlite3.connect('movies.db')
cur = con.cursor()

#for row in cur.execute('SELECT * FROM categories'):
#    print(row)

print('Query output will be saved to %s\nProcessing Query...' % file)
for row in cur.execute('SELECT DISTINCT ratings.user_id, users.gender, age.age_desc, occupation.occupation_desc ' +
                       'FROM ratings, movies, movie_categories, categories, users, age, occupation ' +
                       'WHERE movies.movie_id = ratings.movie_id ' +
                       'AND movies.movie_id = movie_categories.movie_id ' +
                       'AND movie_categories.category_id = categories.category_id '+
                       'AND ratings.user_id = users.user_id ' +
                       'AND users.age = age.age_id ' +
                       'AND users.occupation = occupation.occupation_id '+
                       'AND genre_desc = "Horror" ' +
                       'AND rating > 3 ' +
                       'AND date BETWEEN "2001-01-01" AND "2002-12-31"'):
    line = str(row[0]) + ';' + str(row[1]) + ';' + row[2] + ';' + row[3]
    sys.stdout = outfile
    print(line)

con.close()    
outfile.close()
"""

"""
#-------------------------------------------------------
# queries
#outfile = open('movies.txt','w')
con = sqlite3.connect('movies.db')
cur = con.cursor()

print('Query output will be saved to movie_info.txt\nProcessing Query...')
for row in cur.execute('SELECT COUNT(DISTINCT user_id) ' +
                       'FROM users, age ' +
                       'WHERE age.age_id = users.age ' +
                       'AND age.age_desc = "18-24"'):
    #line = str(row[0]) + ';' + row[1] + ' ' + str(row[2])
    #sys.stdout = outfile
    print(row)
con.close()
#outfile.close()

# -----------------------------------------------------------------------------


# queries
#outfile = open('movies.txt','w')
con = sqlite3.connect('movies.db')
cur = con.cursor()

print('Query output will be saved to movie_info.txt\nProcessing Query...')
for row in cur.execute('SELECT COUNT(DISTINCT users.user_id), movies.movie_title, movies.year ' +
                       'FROM age, users, ratings, movies, movie_categories, categories ' +
                       'WHERE movies.movie_id = ratings.movie_id ' +
                       'AND movies.movie_id = movie_categories.movie_id ' +
                       'AND ratings.user_id = users.user_id ' +
                       'AND age.age_id = users.age ' +
                       'AND movie_categories.category_id = categories.category_id '+
                       'AND categories.genre_desc = "Horror" '
                       'AND age.age_desc = "18-24"'):
    #line = str(row[0]) + ';' + row[1] + ' ' + str(row[2])
    #sys.stdout = outfile
    print(row)
con.close()
#outfile.close()

# -----------------------------------------------------------------------------

"""


f = 'horror_movies2.txt'
outfile = open(f,'w')

con = sqlite3.connect('movies.db')
cur = con.cursor()

# start date:   2000-04-25
# end date:     2003-02-28
print('Query output will be saved to '+f+'\nProcessing Query...')
for row in cur.execute('SELECT ratings.user_id, movies.movie_title, rating, date ' +
                       'FROM ratings, movies, movie_categories, categories ' +
                       'WHERE movies.movie_id = ratings.movie_id ' +
                       'AND movies.movie_id = movie_categories.movie_id ' +
                       'AND movie_categories.category_id = categories.category_id '+
                       'AND genre_desc = "Horror" ' +
                       'AND rating > 3 ' +
                       'AND date BETWEEN "2001-01-01" AND "2002-12-31"'):
    line = str(row[0]) + ';' + row[1] + ';'+ str(row[2]) + ';' + row[3]
    sys.stdout = outfile
    print(line)

con.close()    
outfile.close()







