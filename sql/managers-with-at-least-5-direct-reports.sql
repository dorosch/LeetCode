SELECT
    m.name
FROM
    Employee AS e
INNER JOIN
    Employee AS m on e.managerId = m.id
GROUP BY
    e.managerId
HAVING
    COUNT(e.id) >= 5;
