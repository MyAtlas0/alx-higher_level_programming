					#0x0D-SQL_introduction README File



Last Updated: 14/03/2024;
Contributor(s): MyAtlas0;


TASKS:

0. List databases

#mandatory
Write a script that lists all databases of your MySQL server.

# Filename: 0-list_databases.sql


1. Create a database

#mandatory
Write a script that creates the database hbtn_0c_0 in your MySQL server.

If the database hbtn_0c_0 already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements

# Filename: 1-create_database_if_missing.sql



2. Delete a database

#mandatory
Write a script that deletes the database hbtn_0c_0 in your MySQL server.

If the database hbtn_0c_0 doesn’t exist, your script should not fail
You are not allowed to use the SELECT or SHOW statements

# Filename: 2-remove_database.sql


3. List tables

#mandatory
Write a script that lists all the tables of a database in your MySQL server.

The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)

# Filename: 3-list_tables.sql



4. First table

#mandatory
Write a script that creates a table called first_table in the current database in your MySQL server.

first_table description:
id INT
name VARCHAR(256)
The database name will be passed as an argument of the mysql command
If the table first_table already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements

# Filename: 4-first_table.sql


5. Full description

#mandatory
Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.

The database name will be passed as an argument of the mysql command
You are not allowed to use the DESCRIBE or EXPLAIN statements

# Filename: 5-full_table.sql



6. List all in table

#mandatory
Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

All fields should be printed
The database name will be passed as an argument of the mysql command

# Filename: 6-list_values.sql



7. First add

#mandatory
Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

New row:
id = 89
name = Best School
The database name will be passed as an argument of the mysql command

# Filename: 7-insert_value.sql



8. Count 89

#mandatory
Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

The database name will be passed as an argument of the mysql command

# Filename: 8-count_89.sql



9. Full creation

#mandatory
Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

second_table description:
id INT
name VARCHAR(256)
score INT
The database name will be passed as an argument to the mysql command
If the table second_table already exists, your script should not fail
You are not allowed to use the SELECT and SHOW statements
Your script should create these records:
id = 1, name = “John”, score = 10
id = 2, name = “Alex”, score = 3
id = 3, name = “Bob”, score = 14
id = 4, name = “George”, score = 8

# Filename: 9-full_creation.sql


10. List by best

#mandatory
Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

Results should display both the score and the name (in this order)
Records should be ordered by score (top first)
The database name will be passed as an argument of the mysql command

# Filename: 10-top_score.sql
