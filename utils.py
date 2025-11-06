import os

def dump_env(path=".env"):
    with open(path, "w", encoding="utf-8") as f:
        for k, v in os.environ.items():
            f.write(f"{k}={v}\n")
