# Write your MySQL query statement below

 -- select name as 'Employee' from Employee emlp where salary > (select salary from Employee where id = emlp.managerId);

select a.name as 'Employee' from Employee a, Employee b where a.managerId = b.id and a.salary > b.salary;