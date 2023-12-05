/*
Activity:
    +----------------+---------+
    | Column Name    | Type    |
    +----------------+---------+
    | machine_id     | int     |
    | process_id     | int     |
    | activity_type  | enum    |
    | timestamp      | float   |
    +----------------+---------+

Task:
    There is a factory website that has several machines each running the same number of processes.
    Write an SQL query to find the average time each machine takes to complete a process.

    The time to complete a process is the 'end' timestamp minus the 'start' timestamp.
    The average time is calculated by the total time to complete every process on the machine
    divided by the number of processes that were run.

    The resulting table should have the machine_id along with the average time as processing_time,
    which should be rounded to 3 decimal places.

    Return the result table in any order.
*/


SELECT
    a.machine_id,
    ROUND(
        (SELECT AVG(b.timestamp) FROM Activity b WHERE b.activity_type = 'end' AND b.machine_id = a.machine_id) -
        (SELECT AVG(b.timestamp) FROM Activity b WHERE b.activity_type = 'start' AND b.machine_id = a.machine_id),
        3
    ) AS processing_time
FROM
    Activity a
GROUP BY
    a.machine_id;
