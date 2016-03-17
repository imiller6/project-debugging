def add(first, second):
    return int(first) + int(second)

def subtract(first, second):
    return int(first) - int(second)

def multiply(first, second):
    return int(first) * int(second)

def divide(first, second):
    if int(second) == 0:
    	raise Exception("    I'm sorry, I can't divide by zero")
    else:
    	return int(first) / int(second)