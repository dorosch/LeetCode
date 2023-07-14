/*
Weather:
    +---------------+---------+
    | Column Name   | Type    |
    +---------------+---------+
    | id            | int     |
    | recordDate    | date    |
    | temperature   | int     |
    +---------------+---------+

Task:
    Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
    Return the result table in any order.
 */

SELECT
    DISTINCT a.Id
FROM
    Weather a,
    Weather b
WHERE
    a.Temperature > b.Temperature AND
    DATEDIFF(a.Recorddate, b.Recorddate) = 1;
