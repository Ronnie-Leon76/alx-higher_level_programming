-- creates the database hbtn_0d_usa and the table cities
-- cities contains:
--      id: INT, unique, auto generated, not null, and is a primary key
--      state_id: INT, not null, must be a Foreign Key, reference to id of the states table
--      name: VARCHAR(256), not null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id));