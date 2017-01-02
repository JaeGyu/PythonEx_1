g_v = 0

def outter():
    g_b = 1
    def inner():
        nonlocal g_b
        g_b += 1
        print("1)",g_b)
    inner()
    print("2)",g_b)

outter()