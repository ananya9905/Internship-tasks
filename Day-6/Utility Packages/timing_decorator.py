from functools import wraps
import time

def timer():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            return f"Execution Time: {end - start}sec"
        return wrapper
    return decorator