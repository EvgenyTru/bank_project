import os


def log(filename: str = "DEFAULT"):
    """Декоратор log, который будет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки. Декоратор должен принимать необязательный аргумент
    filename, который определяет, куда будут записываться логи (в файл или в консоль)"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                logging = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                result = func(*args, **kwargs)
            else:
                logging = f"{func.__name__} ok"
            if filename == "DEFAULT":
                print(logging)
            else:
                if os.path.isdir(f"{os.getcwd()}\\logs") is False:
                    os.mkdir(f"{os.getcwd()}\\logs")
                with open(f"{os.getcwd()}\\logs\\{filename}", "a") as file:
                    file.write(f"{logging} \n")
            return result

        return wrapper

    return decorator
