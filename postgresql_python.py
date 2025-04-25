'''
This is for operating postgresql via Python. 
'''
# read libraries
import psycopg2
from psycopg2.extras import execute_values
import os

"""
These are commands on cmd
psql -U (username) - login the postgresql
(when you are asked to input a password) cowons9
c (databasename) - change database
psql -U (user_name) (database_name) #get into the database; -U (username) means to use the username 
create database (database_name) #create a database(NOTICE; Capital letter is not allowed for database_name)
create table (table_name) #create a table
create (schemaname).(table_name) #create a table on the desginated schema
* when you execute command of postgres, ';' is a finish maker of your statement
set search_path =(schema_name) #change schema

\d (table_name) # check contents of the table
ALTER TABLE テーブル名 ALTER COLUMN カラム名 TYPE データ型 # change data type
ALTER TABLE example2 ADD UNIQUE(user_id, date); # add a unique contraint
ALTER TABLE hoge_table ALTER COLUMN hoge_column TYPE INTEGER[] USING '{}'; # change data type from column to array

alter table (table_name) alter (column) drop default #selete default option
alter table (table_name) alter (column) add generated always as identity #add default option of sequential id numbering
alter table (table name) add primary key(columns name) # add primary key
alter table (table_name) rename column (column_name_before) to (column_name_after);
"""

"""
collation = sort order rule
connection limit the upper limit number of connections to this database at the same time

"""

# authentication
id = os.getenv('dir_name')
pw = os.getenv('env_var_name')

# connection
conn = psycopg2.connect(
    '''
    dbname=DBName host=localhost user=userName password=PW port =5432
    '''
    )
cur = conn.cursor()

# issue query
cur.execute("select version()")