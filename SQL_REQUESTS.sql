--SQL-commands according to the home task_02

SELECT u.id as user_personal_id, u.fullname, t.title FROM users as u LEFT JOIN tasks as t ON u.id = t.user_id ORDER BY u.id;

SELECT * FROM tasks WHERE status_id IN (SELECT id FROM status WHERE name = "new");

UPDATE status SET name = 'working on' WHERE name = 'new';

SELECT id, fullname FROM users WHERE id NOT IN (SELECT user_id FROM tasks);

INSERT INTO tasks (title, description, status_id , user_id)
VALUES ('Execute interactive synergies', 'Manage finish check father modern dark quite clearly.', 1, 5),
('Do something', 'Manage it', 3, 4);

SELECT * FROM tasks WHERE status_id NOT IN (SELECT id FROM status WHERE id = 1);

DELETE FROM tasks WHERE id = 1;

SELECT id, fullname, email FROM users WHERE email LIKE '%6%';

UPDATE users SET fullname = 'Johny Walker' WHERE fullname = 'Dana Thomas';

SELECT status_id , COUNT(title) AS number_of_tasks FROM tasks GROUP BY status_id;

SELECT id, title FROM tasks WHERE user_id IN (SELECT id FROM users WHERE email LIKE '%@example.com');

SELECT t.id, u.fullname AS task_owner, t.title
FROM tasks AS t 
JOIN users AS u ON u.id = t.user_id
WHERE u.email LIKE '%@example.com';

SELECT id, title, description FROM tasks WHERE LENGTH (description)> 0;

SELECT u.fullname AS user_name, t.title AS task_name, s.name AS status_of_the_task
FROM tasks AS t
INNER JOIN users AS u ON  u.id = t.user_id
INNER JOIN status AS s ON s.id  = t.status_id 
WHERE s.name = 'in progress';

SELECT t.user_id AS personal_user_id, u.fullname AS name_of_the_person, COUNT(t.title) AS number_of_user_tasks
FROM tasks AS t
JOIN users AS u ON u.id = t.user_id
GROUP BY t.user_id;






