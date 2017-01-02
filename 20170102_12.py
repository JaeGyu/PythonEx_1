def outter():
    def inner():
        print("inner")
    inner()

outter()