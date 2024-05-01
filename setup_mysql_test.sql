-- comment
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- CREATE DATABASE IF NOT EXISTS performance_schema;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'Hbnb_test_pwd@24';
USE hbnb_test_db;
-- USE performance_schema; 
GRANT ALL PRIVILEGES ON hbnb_test_db TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema TO 'hbnb_test'@'localhost';
