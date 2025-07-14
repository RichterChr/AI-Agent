import os

def get_files_info(working_directory, directory=None):
    if directory == None:
        directory = "."
    full_path = os.path.join(working_directory, directory)
    abs_full_path = os.path.abspath(full_path)
    abs_working_path = os.path.abspath(working_directory)

    if not abs_full_path.startswith(abs_working_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(abs_full_path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        formatted_items = []
        for item in os.listdir(abs_full_path):
            item_path = os.path.join(abs_full_path, item)
            format_string = f'- {item}: file_size={os.path.getsize(item_path)}, is_dir={os.path.isdir(item_path)}'
            formatted_items.append(format_string)
        return "\n".join(formatted_items)
    except Exception as e:
        return f"Error: {str(e)}"