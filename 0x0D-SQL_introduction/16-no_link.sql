-- Lists all records in a table containing Name value in order
SELECT `score`, `name` FROM `second_table`
WHERE `name` IS NOT NULL
ORDER BY `score` DESC;
