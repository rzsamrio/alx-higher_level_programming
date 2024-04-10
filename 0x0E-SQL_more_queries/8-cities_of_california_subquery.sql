-- List all the cities of Carlifornia in the country database
-- Uses subquery
SELECT id, name FROM `cities`
WHERE state_id =
	(SELECT id FROM `states`
	 WHERE `name` = 'California')
ORDER BY `cities`.id;
