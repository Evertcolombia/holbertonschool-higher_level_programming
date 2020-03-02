-- show records grup for score in desc order
SELECT score, COUNT(score) as number FROM second_table GROUP BY score ORDER BY score DESC;
