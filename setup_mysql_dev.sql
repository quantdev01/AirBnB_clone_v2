-- db creation

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- CREATE DATABASE IF NOT EXISTS performance_schema; 
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
--CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'Hbnb_dev_pwd@24';
USE hbnb_dev_db;
-- GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD ON hbnb_dev_db TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_dev_db TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
