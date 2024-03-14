-- Desplays the average temperature (in Fahrenheit)
-- by City ordered in descending temperature(DESC).
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
