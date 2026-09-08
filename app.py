def greet(name):
    return "Hi there, %s" % name

def version():
    return "1.1.0"

if __name__ == "__main__":
    print(greet("world"), version())
