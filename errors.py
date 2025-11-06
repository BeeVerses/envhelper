class EnvFileNotFound(FileNotFoundError):
    def __init__(self, path):
        super().__init__(f".env файл не найден: {path}")

class MissingEnvVariable(Exception):
    def __init__(self, key):
        super().__init__(f"Отсутствует необходимая переменная среды: {key}")
