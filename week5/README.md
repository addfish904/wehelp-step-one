# Wehelp – 第五週作業

## Task 2: Create database and table in your MySQL server

CREATE DATABASE `website`;
USE `website`;

CREATE TABLE member (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    follower_count INT UNSIGNED NOT NULL DEFAULT 0,
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

## Task 3: SQL CRUD

### INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.

INSERT INTO member (name, username, password) 
VALUES ('test', 'test', 'test');

INSERT INTO member (name, username, password, follower_count)
VALUES 
('Alice', 'alice123', 'pass123', 60),
('Bob', 'bob456', 'word456', 20),
('Charlie', 'charlie789', 'safe789', 255),
('David', 'david101', 'strong101', 5);

### SELECT all rows from the member table.

SELECT * FROM member;

### SELECT all rows from the member table, in descending order of time.

SELECT * FROM member ORDER BY time DESC;

### SELECT total 3 rows, second to fourth, from the member table, in descending order
of time

SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;

### SELECT rows where username equals to test.

SELECT * FROM member WHERE username = 'test';

### SELECT rows where name includes the es keyword.

SELECT * FROM member WHERE name LIKE '%es%';

### SELECT rows where both username and password equal to test.

SELECT * FROM member WHERE username = 'test' AND password = 'test';

### UPDATE data in name column to test2 where username equals to test.

UPDATE member 
SET name = 'test2'
WHERE username = 'test';

## Task 4: SQL Aggregation Functions



