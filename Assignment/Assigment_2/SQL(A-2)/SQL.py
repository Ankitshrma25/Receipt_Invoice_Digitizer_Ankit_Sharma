import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER,
    dept_id INTEGER,
    FOREIGN KEY(dept_id) REFERENCES departments(dept_id)
)
""")

cursor.execute("DELETE FROM departments")
cursor.execute("DELETE FROM employees")

departments = [
    (101, "IT"),
    (102, "HR"),
    (103, "Sales")
]

employees = [
    (1, "Ankit", 50000, 101),
    (2, "Ravi", 40000, 102),
    (3, "Priya", 60000, 101),
    (4, "Sathiya", 45000, 103),
    (5, "John", 70000, None)
]

cursor.executemany("INSERT INTO departments VALUES (?,?)", departments)
cursor.executemany("INSERT INTO employees VALUES (?,?,?,?)", employees)

conn.commit()

print("\nAll Employees:")
for row in cursor.execute("SELECT * FROM employees"):
    print(row)

print("\nSalary > 45000:")
for row in cursor.execute("SELECT name, salary FROM employees WHERE salary > 45000"):
    print(row)

print("\nNames starting with A:")
for row in cursor.execute("SELECT name FROM employees WHERE name LIKE 'A%'"):
    print(row)

print("\nSalary between 40000 and 60000:")
for row in cursor.execute("SELECT name, salary FROM employees WHERE salary BETWEEN 40000 AND 60000"):
    print(row)

print("\nDepartment IN (101,102):")
for row in cursor.execute("SELECT name FROM employees WHERE dept_id IN (101,102)"):
    print(row)

print("\nOrder by salary DESC:")
for row in cursor.execute("SELECT name, salary FROM employees ORDER BY salary DESC"):
    print(row)

print("\nEmployee count per department:")
for row in cursor.execute("""
SELECT dept_id, COUNT(*)
FROM employees
GROUP BY dept_id
"""):
    print(row)

print("\nDepartments having more than 1 employee:")
for row in cursor.execute("""
SELECT dept_id, COUNT(*)
FROM employees
GROUP BY dept_id
HAVING COUNT(*) > 1
"""):
    print(row)

print("\nInner Join:")
for row in cursor.execute("""
SELECT e.name, d.dept_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id
"""):
    print(row)

print("\nLeft Join:")
for row in cursor.execute("""
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d
ON e.dept_id = d.dept_id
"""):
    print(row)

cursor.execute("UPDATE employees SET salary = 52000 WHERE name='Ankit'")
conn.commit()

print("\nAfter Update:")
for row in cursor.execute("SELECT name, salary FROM employees WHERE name='Ankit'"):
    print(row)

cursor.execute("DELETE FROM employees WHERE name='John'")
conn.commit()

print("\nAfter Delete:")
for row in cursor.execute("SELECT name FROM employees"):
    print(row)

conn.close()
