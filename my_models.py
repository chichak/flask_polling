import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="polling_db",
        user= "ichrak",#os.environ['DB_USERNAME'],
        password= "keybfr")#os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
#cur.execute('DROP TABLE IF EXISTS tbl_languages;')
#cur.execute('CREATE TABLE tbl_poll (id serial PRIMARY KEY,'
#                                 'web_framework varchar (150) NOT NULL,'
#                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
#                                 )

# https://stackoverflow.com/questions/34494954/mogrify-and-returning-with-psycopg2
# https://stackoverflow.com/questions/8134602/psycopg2-insert-multiple-rows-with-one-query

# Insert data into the table
#tup = ('Flask','Laravel','React.js','Express','Django')
#args_str = ','.join(cur.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s,%s)", x) for x in tup)
#cur.execute("INSERT INTO table VALUES " + args_str) 

#table = 'prg_languages'
#query = cur.mogrify("INSERT INTO {} VALUES {} ".format(
 #                       table,
 #                       ', '.join('{}'.format(x) for x in tup)
 #                   ) )
#cur.execute(query) 

# '','','',''
## When adding a new ligne, i had to add the colon near to 'test_language' in order to make it work
cur.execute('INSERT INTO tbl_poll (web_framework)'
            'VALUES (%s)',
            ('FLASK',)
            )

# FLASK, , , , , Test_language

conn.commit()

cur.close()
conn.close()