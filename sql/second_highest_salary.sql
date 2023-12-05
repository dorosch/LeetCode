-- Data
create table employee (id BIGSERIAL PRIMARY KEY, salary int);

insert into employee (salary) values (100), (200), (300);


-- Answer
select max(salary) as SecondHighestSalary from Employee where salary < (select max(salary) from Employee);
