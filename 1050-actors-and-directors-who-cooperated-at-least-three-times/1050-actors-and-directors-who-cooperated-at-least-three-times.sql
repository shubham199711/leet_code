# Write your MySQL query statement below
select actor_id, director_id from ActorDirector group by 2, 1 having count(*) > 2;
