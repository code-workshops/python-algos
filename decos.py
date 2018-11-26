def multi(f):
    def wrapper(*args, **kwargs):
        a, b = args
        r = f(a, b)
        print(r * 2)
    return wrapper

@multi
def counter(a, b):
    print("Wrapping...")
    return a + b
