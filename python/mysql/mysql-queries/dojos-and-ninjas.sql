INSERT INTO dojos
VALUES
(1,"dojo1",current_time(),current_time()),
(2,"dojo2",current_time(),current_time()),
(3,"dojo3",current_time(),current_time())

DELETE FROM dojos WHERE id IN (1,2,3);

INSERT INTO dojos
VALUES
(1,"dojo1",current_time(),current_time()),
(2,"dojo2",current_time(),current_time()),
(3,"dojo3",current_time(),current_time())

INSERT INTO ninjas
VALUES
(1, 1, "ninja1", "hunter", 22, current_time(), current_time()),
(2, 1, "ninja2", "kyle", 50, current_time(), current_time()),
(3, 1, "ninja3", "bob", 80, current_time(), current_time());

INSERT INTO ninjas
VALUES
(1, 2, "ninja1", "hunter", 22, current_time(), current_time()),
(2, 2, "ninja2", "kyle", 50, current_time(), current_time()),
(3, 2, "ninja3", "bob", 80, current_time(), current_time());

INSERT INTO ninjas
VALUES
(1, 3, "ninja1", "hunter", 22, current_time(), current_time()),
(2, 3, "ninja2", "kyle", 50, current_time(), current_time()),
(3, 3, "ninja3", "bob", 80, current_time(), current_time());

SELECT * FROM ninjas ORDER BY id ASC limit 1;

SELECT * FROM ninjas ORDER BY id DESC limit 1;

SELECT dojo_id FROM ninjas ORDER BY id DESC limit 1;

SELECT dojo_id
FROM ninjas
ORDER BY id
DESC limit 1;