# Write your MySQL query statement below
select pr.firstName, pr.lastName, ad.city, ad.state from Person pr
LEFT JOIN Address ad on pr.personId = ad.personId
