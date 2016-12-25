#_*_ coding: UTF-8 _*_

import csv

def read_data():
    file = open('data.csv')
    reader = csv.reader(file)
    rows = [row[1:] for row in reader][1:]
    file.close()	
    print(rows)
    return [float(row[0]) for row in rows],[float(row[1]) for row in rows]

def read_data2():
    with open("data.csv") as file:
        reader = csv.reader(file)
        rows = [row[1:] for row in reader][1:]
        print("출력 합니다.")
        print(rows)

def read_data3():
    with open("data.csv") as file:
        reader = csv.reader(file)
        '''for row in reader:
            continue
            print(row)'''
        rows = [row[1:] for row in reader][1:]
        print("rows :: ")
        print(rows)

def list_test():
    list = [[1,2],[3,4],[5,6]]
    print("before :: ",list)
    print([row for row in list])
    print([row[1:] for row in list])
    print(list[1:][1:])

def main():
    print("main 입니다.")
    #print(read_data())
    #print(read_data2())
    #read_data3()
    list_test()


if __name__ == '__main__':
    main()
