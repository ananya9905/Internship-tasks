from functools import wraps
import time

def timer():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"Execution Time: {end - start}sec")
            return result
        return wrapper
    return decorator