-- Desplays the 3 cities with the average temperature (in Fahrenheit)
-- during July and August ordered in descending temperature(DESC).
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
