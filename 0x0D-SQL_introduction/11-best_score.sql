-- Lists all the records with a score >= 10 in the second_table.
-- Records should be ordered by score (top first).
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
