 --- Creating New Database 
 CREATE DATABASE my_database
 --- Creating New User 
 CREATE USER my_user WITH PASSWORD 'Password';
 --- Giving PRIVILEGES to new User 
 GRANT ALL PRIVILEGES ON DATABASE my_database  to my_user;
 GRANT USAGE ON schema public TO my_user;
GRANT ALL PRIVILEGES ON SCHEMA public TO my_user;

