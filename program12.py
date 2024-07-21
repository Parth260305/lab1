# Specify the file path
file_path = "newfile.txt"
print(f"File '{file_path}' has been created.")
# Writing to a file
with open(file_path, 'w') as file:
    file.write("Hello.\n")

# Reading from the file
with open(file_path, 'r') as file:
    content = file.read()
    print("File content:")
    print(content)
