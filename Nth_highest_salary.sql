-- Data
create table employee (id BIGSERIAL PRIMARY KEY, salary int);

insert into employee (salary) values (100), (200), (300);


-- Answer
CREATE OR REPLACE FUNCTION getNthHighestSalary (N int)
    RETURNS int
    LANGUAGE plpgsql
    AS
$$
    BEGIN
        RETURN (SELECT DISTINCT(salary) from Employee order by salary DESC LIMIT 1 OFFSET N - 1);
    END
$$;
