-- create_database.sql

-- Create database
CREATE DATABASE IF NOT EXISTS user_admin_app;

-- Create a user (optional, skip if using root)
CREATE USER 'alwavega'@'localhost' IDENTIFIED BY 'flaskpass';
GRANT ALL PRIVILEGES ON user_admin_app.* TO 'alwavega'@'localhost';
FLUSH PRIVILEGES;
