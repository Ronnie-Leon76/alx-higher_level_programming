-- creates the database hbtn_0d_usa and the table states
-- states table contains: 
--      id INT unique, auto generated, not null and is a primary
--      name VARCHAR(256) Not Null


CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
