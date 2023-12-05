SELECT
    user_id,
    COALESCE(
        ROUND(
            (SELECT COUNT(action) FROM Confirmations c WHERE c.user_id = s.user_id AND action = 'confirmed') /
            (SELECT COUNT(action) FROM Confirmations c WHERE c.user_id = s.user_id),
            2
        ),
        0
    ) AS confirmation_rate
FROM
    Signups s
GROUP BY
    user_id;
