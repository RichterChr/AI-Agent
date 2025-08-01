import os
from config import MAX_CHARS

# function for opening and reading a file

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(full_path)
    abs_working_path = os.path.abspath(working_directory)

    if not abs_file_path.startswith(abs_working_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: "File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(f.read(1)) >= 1:
                return file_content_string[:MAX_CHARS] + f'[...File "{file_path}" truncated at 10000 characters].'
            else:
                return file_content_string
    except Exception as e:
        return f"Error: {str(e)}"