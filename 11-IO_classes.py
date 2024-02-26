# Define the FileManager class here

# Demonstrate using FileManager to write and read from a file
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def write_content(self, content):
        with open(self.filename, "w") as file:
            file.write(content)

    def read_content(self):
        with open(self.filename, "r") as file:
            return file.read()


filename = "example.txt"
content = input("Enter the content to write to the file: ")

file_manager = FileManager(filename)
file_manager.write_content(content)

print(f"the content of the file is: {file_manager.read_content()}")
