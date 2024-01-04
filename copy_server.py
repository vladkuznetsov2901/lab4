import os
import shutil


def file_copy_server(pipe_name):
    if not os.path.exists(pipe_name):
        os.mkfifo(pipe_name)

    with open(pipe_name, 'r') as pipe:
        while True:
            task = pipe.readline().strip()

            if not task:
                break

            source_file, destination_file = task.split(",")

            try:
                shutil.copy(source_file, destination_file)
                print(f"File copied: {source_file} to {destination_file}")
            except Exception as e:
                print(f"Error copying file: {e}")


if __name__ == "__main__":
    pipe_name = "example.txt"
    file_copy_server(pipe_name)
