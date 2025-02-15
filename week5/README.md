# 📝 Wehelp – 第五週作業

## 📌 Task 2: Create database and table in your MySQL server

```sql
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
```

## 📌 Task 3: SQL CRUD

🔹 3-1：INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.
```sql
INSERT INTO member (name, username, password) 
VALUES ('test', 'test', 'test');

INSERT INTO member (name, username, password, follower_count)
VALUES 
('Alice', 'alice123', 'pass123', 60),
('Bob', 'bob456', 'word456', 20),
('Charlie', 'charlie789', 'safe789', 255),
('David', 'david101', 'strong101', 5);
```
🔹 3-2：SELECT all rows from the member table.
```sql
SELECT * FROM member;
```
🔹 3-3：SELECT all rows from the member table, in descending order of time.
```sql
SELECT * FROM member ORDER BY time DESC;
```
🔹 3-4：SELECT total 3 rows, second to fourth, from the member table, in descending order
of time
```sql
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
```
🔹 3-5：SELECT rows where username equals to test.
```sql
SELECT * FROM member WHERE username = 'test';
```
🔹 3-6：SELECT rows where name includes the es keyword.
```sql
SELECT * FROM member WHERE name LIKE '%es%';
```
🔹 3-7：SELECT rows where both username and password equal to test.
```sql
SELECT * FROM member WHERE username = 'test' AND password = 'test';
```
🔹 3-8：UPDATE data in name column to test2 where username equals to test.
```sql
UPDATE member 
SET name = 'test2'
WHERE username = 'test';
```

## 📌 Task 4: SQL Aggregation Functions

🔹 4-1：SELECT how many rows from the member table.
```sql
SELECT COUNT(*) FROM member;
```
🔹 4-2：SELECT the sum of follower_count of all the rows from the member table.
```sql
SELECT SUM(follower_count) FROM member;
```
🔹 4-3：SELECT the average of follower_count of all the rows from the member table.
```sql
SELECT AVG(follower_count) FROM member;
```
🔹 4-4：SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.
```sql
SELECT AVG(follower_count) FROM(
SELECT follower_count
FROM member
ORDER BY follower_count DESC
LIMIT 2
) AS subquery;
```
## 📌 Task 5: SQL JOIN

🔹 5-1：Create a new table named message, in the website database.
```sql
CREATE TABLE message(
id BIGINT PRIMARY KEY AUTO_INCREMENT,
member_id BIGINT NOT NULL,
content VARCHAR(255) NOT NULL,
like_count INT UNSIGNED NOT NULL DEFAULT 0,
time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (member_id) REFERENCES member(id)
);
```
```sql
INSERT INTO message (member_id, content, like_count)
VALUES
(1, 'Hello world!', 25),
(2, 'Good Morning!', 10),
(3, 'I love SQL', 220),
(4, 'Let\'s Learn MySQL', 7),
(5, 'Good Bye!', 84);
```
🔹 5-2：SELECT all messages, including sender names. We have to JOIN the member table to get that.
```sql
SELECT message.*, member.name
FROM message
JOIN member
ON message.member_id = member.id
```
🔹 5-3：SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
```sql
SELECT message.*, member.name 
FROM message 
JOIN member ON message.member_id = member.id
WHERE member.username = 'test';
```
🔹 5-4：Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
```sql
SELECT AVG(message.like_count) 
FROM message 
JOIN member ON message.member_id = member.id
WHERE member.username = 'test';
```
🔹 5-5：Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.
```sql
SELECT member.username, AVG(message.like_count) AS avg_likes
FROM message 
JOIN member ON message.member_id = member.id
GROUP BY member.username;
