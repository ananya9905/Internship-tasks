def file_generator(filename: str):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            yield line