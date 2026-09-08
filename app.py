def greet(name):
    return f"Hello, {name}!"

def version():
    return "2.0.0"

if __name__ == "__main__":
    print(greet("world"), version())
