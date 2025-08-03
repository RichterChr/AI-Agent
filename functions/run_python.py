import os, subprocess

# function for running a python file

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    abs_full_path = os.path.abspath(full_path)
    abs_working_path = os.path.abspath(working_directory)

    if not abs_full_path.startswith(abs_working_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
         
    if not os.path.exists(abs_full_path):
            return f'Error: File "{file_path}" not found.'
    if not abs_full_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
    args_list = ["python", abs_full_path] + args
        

    try:
        completed_process = subprocess.run(args_list, capture_output=True, cwd=abs_working_path, timeout=30)
        stdout_content = completed_process.stdout.decode()
        stderr_content = completed_process.stderr.decode()

        output = ""
        error = ""
        if stdout_content:
            output = f'STDOUT: {stdout_content}'
        if stderr_content:
            error = f'STDERR: {stderr_content}'
            
        if stdout_content == "" and stderr_content == "":
             return 'No output produced.'
        if completed_process.returncode != 0:
            return f'{error} Process exited with code {completed_process.returncode} \n{output}'
        return f'{error} \n{output}'
    except Exception as e:
        return f"Error: executing Python file: {e}"