


def logger(count):  
    def inner(func):
        def wrapper(*arg, **kwargs):
            for _ in range(count):
                print('LOGGED')
                pass
            rv = func(*arg, **kwargs)
            return rv
        return wrapper
    return inner
    

@logger(3)
def yolo(x, y):
    return f'{x}{y}'



print(yolo('YO', 'LO'))