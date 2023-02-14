-- displays the top 3 of cities temperature during july and august ordered by
-- temperatures

SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month = 7 OR month = 8 GROUP BY city WHERE month='7'
ORDER BY avg_temp DESC LIMIT 3;

