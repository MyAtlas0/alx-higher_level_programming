-- Lists all the records with the same scores in the second_table.
-- Records should be ordered by descending order (DESC).
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
