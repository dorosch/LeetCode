/*
Sales:
    +-------------+-------+
    | Column Name | Type  |
    +-------------+-------+
    | sale_id     | int   |
    | product_id  | int   |
    | year        | int   |
    | quantity    | int   |
    | price       | int   |
    +-------------+-------+

Product:
    +--------------+---------+
    | Column Name  | Type    |
    +--------------+---------+
    | product_id   | int     |
    | product_name | varchar |
    +--------------+---------+

Task:
    Write an SQL query that reports the product_name, year, and price for each sale_id in the Sales table.
    Return the resulting table in any order.
*/


SELECT
    product_name,
    year,
    price
FROM
    Sales
LEFT JOIN Product USING (product_id);
