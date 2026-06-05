# You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.

# You are given an array of employees employees where:

# employees[i].id is the ID of the ith employee.
# employees[i].importance is the importance value of the ith employee.
# employees[i].subordinates is a list of the IDs of the direct subordinates of the ith employee.
# Given an integer id that represents an employee's ID, 
# return the total importance value of this employee and all their direct and indirect subordinates.

 

# Example 1:


# Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
# Output: 11
# Explanation: Employee 1 has an importance value of 5 and has two direct subordinates: employee 2 and employee 3.
# They both have an importance value of 3.
# Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.


"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employeeMap = {}

        for employee in employees:
            employeeMap[employee.id] = employee
            
        totalImportance = 0
        def dfs(employee):

            nonlocal totalImportance

            totalImportance += employee.importance

            for subordinates in employee.subordinates:
                dfs(employeeMap[subordinates])

        print(employees)
        dfs(employeeMap[id])
        return totalImportance