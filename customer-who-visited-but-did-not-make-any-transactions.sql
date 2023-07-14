/*
Visits:
    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | visit_id    | int     |
    | customer_id | int     |
    +-------------+---------+

Transactions:
    +----------------+---------+
    | Column Name    | Type    |
    +----------------+---------+
    | transaction_id | int     |
    | visit_id       | int     |
    | amount         | int     |
    +----------------+---------+

Task:
    Write a SQL query to find the IDs of the users who visited without making any transactions and
    the number of times they made these types of visits.
    Return the result table sorted in any order.
*/


SELECT
    customer_id,
    COUNT(visit_id) AS count_no_trans
FROM
    Visits
LEFT JOIN
    Transactions USING (visit_id)
WHERE
    transaction_id IS NULL
GROUP BY
    customer_id;
