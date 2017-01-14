print("-"*60)

def main():
    print("hello")

    v = [i for i in range(10)]
    print(v)

    v = [lambda x : x+1 for i in range(10)]
    print(v)

if __name__ == "__main__":
    main()



