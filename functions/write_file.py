import os

#function for writing in a file

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(full_path)
    abs_working_path = os.path.abspath(working_directory)

    if not abs_file_path.startswith(abs_working_path):
        return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
    
    try:     
        if not os.path.exists(os.path.dirname(abs_file_path)):
            os.makedirs(os.path.dirname(abs_file_path))
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"