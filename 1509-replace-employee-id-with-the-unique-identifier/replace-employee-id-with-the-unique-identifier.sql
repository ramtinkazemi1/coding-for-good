# Write your MySQL query statement below
SELECT unique_id , name
FROM Employees emp
LEFT JOIN EmployeeUNI empUNI ON emp.id = empUNI.id