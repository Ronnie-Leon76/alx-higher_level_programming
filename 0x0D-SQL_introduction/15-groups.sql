-- This script lists the number of records with the same score in the table
-- second_table of the database hbtn_0c_0
SELECT DISTINCT score, COUNT(score) OVER(PARTITION BY score)  AS number FROM second_table ORDER BY score DESC;
