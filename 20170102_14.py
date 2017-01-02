global_var = 77

def outter():
    global_var = 100
    def inner():
        global global_var
        global_var += 1
        print(global_var)
    inner()

outter()