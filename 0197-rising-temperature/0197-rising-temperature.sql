# Write your MySQL query statement below

select id from Weather a where a.temperature > (select temperature from Weather b where subdate(a.recordDate, 1) = b.recordDate)

-- select a.id from Weather a, Weather b where DATEDIFF(a.recordDate, b.recordDate) = 1 and a.temperature > b.temperature;