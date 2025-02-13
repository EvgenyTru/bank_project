from src.config import log_dir


def log(filename: str|None = None):
    """Декоратор log, который будет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки. Декоратор должен принимать необязательный аргумент
    filename, который определяет, куда будут записываться логи (в файл или в консоль)"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                logging = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                raise e
            else:
                logging = f"{func.__name__} ok"
                return result
            finally:

                if not filename:
                    print(logging)
                else:
                    file_path = log_dir.joinpath(filename)
                    with file_path.open(mode="a", encoding="utf-8") as file:
                        file.write(f"{logging}\n")


        return wrapper


    return decorator
