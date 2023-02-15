--  script that creates the table unique_id on your MySQL server.

CREATE TABLE IF NOT EXISTS unique_id( 
	id INT UNIQUE NOT NULL,
	name VARCHAR(256)
);
