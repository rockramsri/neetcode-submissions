-- Write your query below
select employee_id,
CASE
when employee_id%2 <> 0 AND name not like 'M%' then salary
else 0
end as bonus  
from employees
ORDER by employee_id