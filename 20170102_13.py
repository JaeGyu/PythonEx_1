global_var = 0

def outter():
    def inner():
        global global_var
        global_var = 10
    inner()

outter()
print(global_var)