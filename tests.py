from functions.get_files_info import get_files_info

print("Result for the current directory:")
print(get_files_info("calculator", "."))

print("Result for the 'pkg' directory:")
print(get_files_info("calculator", "pkg"))

print("Result for the '/bin' directory:")
print(get_files_info("calculator", "/bin"))

print("Result for the '../' directory:")
print(get_files_info("calculator", "../"))