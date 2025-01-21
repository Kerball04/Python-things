import os

filename = input("Enter a file and I'll give you its extension: ")

file_path = f"/home/kerball/git/Python-things/1-100/7/{filename}"
_, file_extension = os.path.splitext(file_path)
print("The extension this file possesses is " + file_extension)  

# correct