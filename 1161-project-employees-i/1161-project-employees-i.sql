# Write your MySQL query statement below

select proj.project_id,
       ROUND(avg(emp.experience_years),2) as average_years

from Employee as emp
JOIN Project as proj
on proj.employee_id = emp.employee_id
GROUP BY project_id

