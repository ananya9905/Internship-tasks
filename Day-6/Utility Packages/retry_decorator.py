from functools import wraps

def retry(attempts: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(attempts):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    if attempt == (attempts - 1):
                        raise
                    else:
                        continue
        return wrapper
    return decorator
