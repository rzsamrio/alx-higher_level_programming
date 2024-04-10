-- Lists Corresponding Data From 2 tables
-- Uses Inner Join
SELECT `cities`.id, `cities`.name, `states`.name FROM `cities`
JOIN `states` ON `cities`.state_id = `states`.id
ORDER BY `cities`.id;
