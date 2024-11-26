x = 10
def outer_function():
 #   print(f"value of x in outer function {x}")
    x= 20
    print(f"value of x in outer function after modification {x}")
    def inner_function():
        
        x = 30 #local variable 
        print(f"value in inner function after modification {x}") #output 30
    inner_function()
    print(x) #output : 20

print(f"value of x in global scope before function execute {x}")
outer_function()
print(f"value of x in outer function after function execution {x}")
