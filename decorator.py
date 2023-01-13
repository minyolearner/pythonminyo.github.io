# Starting Functional Programming Paradigm
# Taking Function & Modifing Function - adding some additional behavior to that function
# decorator is going to be function that takes a function of input and return a modified version of that function as output
# Some other language function can't be modified  

def announce(f):
    def wrapper():
        print("This function going to run...")
        f()
        print("Done with the funtion..")
    return wrapper 

@announce
def hello():
    print("Hello, World!")

hello()