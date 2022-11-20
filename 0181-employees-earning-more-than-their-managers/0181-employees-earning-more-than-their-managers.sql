# Write your MySQL query statement below

select name as 'Employee' from Employee emlp where salary > (select salary from Employee where id = emlp.managerId);