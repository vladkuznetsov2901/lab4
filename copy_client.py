import os

def file_copy_client(pipe_name, source_file, destination_file):
    with open(pipe_name, 'w') as pipe:
        pipe.write(f"{source_file},{destination_file}\n")

if __name__ == "__main__":
    pipe_name = "example.txt"
    source_file = "example.txt"
    destination_file = "D:\OperationSystems\lab4\dist"

    file_copy_client(pipe_name, source_file, destination_file)
