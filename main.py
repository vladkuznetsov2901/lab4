import threading
import time


class FileOutputProcess:
    def __init__(self, file_name):
        self.file_name = file_name
        self.lock = threading.Lock()

    def output_file(self):
        with self.lock:
            with open(self.file_name, 'r') as file:
                content = file.read()
                print(content)


file_process = FileOutputProcess('example.txt')

threads = []
for _ in range(5):
    t = threading.Thread(target=file_process.output_file)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
