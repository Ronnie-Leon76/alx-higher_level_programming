-- This script displays the average temperature (Fahrenheit) by city ordered by
-- temperature (descending)
SELECT city, AVG(value) OVER(PARTITION BY value) AS avg_temp FROM temperatures ORDER BY avg_temp DESC;
