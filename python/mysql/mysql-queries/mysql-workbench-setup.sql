INSERT INTO names VALUES (1, "Reece", current_time(), current_time());
DELETE FROM names WHERE id = 1;
INSERT INTO names VALUES (1, "Reece", current_time(), current_time()), (2, "Hunter", current_time(), current_time());
UPDATE names SET name = "Alfred" WHERE id = 1;
DELETE FROM names WHERE id = 1;
DELETE FROM names WHERE id = 2;