--
SELECT name FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.show_id = 
	(SELECT id FROM tv_shows
	 WHERE title = 'Dexter'); 
