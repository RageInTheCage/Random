def f():
    global x
    print(x)
    
    def y():
        print(x)
    y()
    
x = 3
f()
