def add(first, second):
    print(int(first) + int(second))

def subtract(first, second):
    print(int(first) - int(second))

def multiply(first, second):
    print(int(first) * int(second))

def divide(first, second):
    if int(second) == 0:
    	raise Exception("    I'm sorry, I can't divide by zero")
    else:
    	print(int(first) / int(second))