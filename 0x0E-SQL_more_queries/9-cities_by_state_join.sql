-- To list all cities in the 'hbtn_0d_usa' database, along with their respective states
-- sorted in ascending order by cities.id
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id=states.id
ORDER BY cities.id;
