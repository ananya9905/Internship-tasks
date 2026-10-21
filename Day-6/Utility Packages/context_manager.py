class MyContext():
    def __init__(self, filename: str, mode: str) -> None:
        self.filename: str = filename
        self.mode: str = mode
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    def __exit__(self, exc_type, exc, tb):
        self.file.close()