INSERT INTO dojos (name)
VALUES ("Chicago"), ("Seattle"),("Online");

SET SQL_SAFE_UPDATES = 0;
DELETE FROM dojos;

INSERT INTO ninjas (first_name, last_name,age, dojo_id)
VALUES ("Marck","Sam",25,3),("Jeff","Yark",30,3),("Franck","Ray",22,3);

INSERT INTO ninjas (first_name,last_name,age,dojo_id)
VALUES ("Rose","Glad",33,1),("Lise","Joh",26,1),("Karl","Hill",29,1);

INSERT INTO ninjas (first_name,last_name,age,dojo_id)
VALUES ("Sofie","Hog",66,2),("Seal","Bob",41,1),("Teck","Grace",26,1);

SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE dojos.id = 3;

SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
	WHERE dojos.id = (SELECT id FROM dojos ORDER BY id DESC LIMIT 1);
    
SELECT * FROM dojos
WHERE dojos.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1);

