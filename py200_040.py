def add_txt(t1, t2="python"):
    print(t1 + ":" + t2)
    
add_txt("best")
add_txt("best","Java")

def func1(*args):
    print(args)

func1(1,2,3)
func1()

def func2(w,h,**kwargs):
    print(kwargs)

func2(1,2,a=1)
