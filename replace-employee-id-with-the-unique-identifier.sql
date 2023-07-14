/*
Employees:
    +---------------+---------+
    | Column Name   | Type    |
    +---------------+---------+
    | id            | int     |
    | name          | varchar |
    +---------------+---------+

EmployeeUNI:
    +---------------+---------+
    | Column Name   | Type    |
    +---------------+---------+
    | id            | int     |
    | unique_id     | int     |
    +---------------+---------+

Task:
    Show the unique ID of each user, If a user does not have a unique ID replace just show null.
    Return the result table in any order.
*/


SELECT
    unique_id,
    name
FROM
    Employees
LEFT JOIN EmployeeUNI USING (id);
