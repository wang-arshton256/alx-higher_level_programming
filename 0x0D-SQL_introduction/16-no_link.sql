-- lists all the records of the table second_table of the database hbtn_0c_0
SELECT	score,
	name
FROM	second_table
WHERE NAME IS NOT NULL
ORDER BY score DESC;
