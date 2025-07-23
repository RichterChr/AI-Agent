from functions.run_python import run_python_file

# Tests für run_python

print(run_python_file("calculator", "main.py"))

print(run_python_file("calculator", "main.py", ["3 + 5"]))

print(run_python_file("calculator", "tests.py"))

print(run_python_file("calculator", "../main.py"))

print(run_python_file("calculator", "nonexistent.py"))