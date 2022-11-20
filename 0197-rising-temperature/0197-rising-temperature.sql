# Write your MySQL query statement below

-- select id from Weather a where a.temperature > (select temperature from Weather b where a.recordDate = subdate(b.recordDate, 1))

select a.id from Weather a, Weather b where DATEDIFF(a.recordDate, b.recordDate) = 1 and a.temperature > b.temperature;