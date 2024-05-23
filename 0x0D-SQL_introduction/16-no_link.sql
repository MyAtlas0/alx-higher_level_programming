-- Lists all the records with a name value in the second_table.
-- Records should be ordered by descending order (DESC).
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
