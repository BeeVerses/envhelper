import os
from .parser import parse_env_line
from .errors import EnvFileNotFound, MissingEnvVariable

def load_env(path=".env", override=False):
    if not os.path.exists(path):
        raise EnvFileNotFound(path)
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            result = parse_env_line(line)
            if result:
                key, value = result
                if not override and key in os.environ:
                    continue
                os.environ[key] = value

def get_env(key, default=None):
    return os.getenv(key, default)

def set_env(key, value, save=False, path=".env"):
    os.environ[key] = str(value)
    if save:
        with open(path, "a", encoding="utf-8") as f:
            f.write(f"{key}={value}\n")

def get_env_int(key, default=None):
    value = os.getenv(key, default)
    try:
        return int(value)
    except (TypeError, ValueError):
        return default

def get_env_bool(key, default=False):
    value = os.getenv(key)
    if value is None:
        return default
    return str(value).lower() in ("1", "true", "yes", "on")

def require_env(key):
    value = os.getenv(key)
    if value is None:
        raise MissingEnvVariable(key)
    return value
