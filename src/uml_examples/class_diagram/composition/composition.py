"""Пример взаимодействия объектов классов - композиция."""


class File:
    def __init__(self, filename):
        self.filename = filename

    def open(self):
        print(f"Open file: {self.filename}")

    def close(self):
        print(f"Close file: {self.filename}")


class FileLogger:

    def __init__(self, filename):
        self.file = File(filename)

    def write(self, message):
        self.file.open()
        print(f"Write message: {message}")
        self.file.close()


if __name__ == "__main__":
    logger = FileLogger("log.txt")
    logger.write("Hello, world!")
