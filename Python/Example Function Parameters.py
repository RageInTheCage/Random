def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def calc(x, y, method):
    return method(x, y)

x = 10
y = 2
z = calc(x, y, add)
print ("{0} {1} {2} = {3}".format(x, "add", y, z))

z = calc(x, y, subtract)
print ("{0} {1} {2} = {3}".format(x, "subtract", y, z))
