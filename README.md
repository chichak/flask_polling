# flask_polling
This project makes use of flask ajax postgress to build a live polling system.

## First this is the database schema : 
### First table : 

CREATE TABLE tblprogramming (
	id serial PRIMARY KEY,
	title VARCHAR ( 150 ) NOT NULL
);

INSERT INTO
    tblprogramming(title)
VALUES
('Flask'),
('Laravel'),
('React.js'),
('Express'),
('Django');

### Second Table: 

CREATE TABLE tbl_poll (
	id serial PRIMARY KEY,
	web_framework VARCHAR ( 150 ) NOT NULL
);

INSERT INTO
    tbl_poll(web_framework)
VALUES
('Flask'),
('Flask'),
('Flask'),
('Express'),
('React.js'),
('Laravel'),
('Flask'),
('Flask'),
('Laravel'),
('Django'),
('Django'),
('Flask');
