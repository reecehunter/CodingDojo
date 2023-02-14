USE users_schema;

INSERT INTO users
VALUES
(1, "Reece", "Hunter", "reece@mail.gom", current_time(), current_time()),
(2, "Bob", "Bobson", "bob@mail.gom", current_time(), current_time()),
(3, "Phil", "Bill", "phil@mail.gom", current_time(), current_time());

SELECT * FROM users;

SELECT * FROM users WHERE email = "reece@mail.gom";

SELECT * FROM users WHERE id = 3;

UPDATE users SET last_name = "Pancakes" WHERE id = 3;

DELETE FROM users WHERE id = 2;

SELECT * FROM users ORDER BY first_name;

SELECT * FROM users ORDER BY first_name DESC;