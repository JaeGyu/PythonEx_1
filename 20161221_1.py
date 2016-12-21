#_*_ coding: UTF-8 _*_

import csv

def read_data():
    file = open('data.csv')
    reader = csv.reader(file)
    rows = [row[1:] for row in reader][1:]
    print(rows)
    return [float(row[0]) for row in rows],[float(row[1]) for row in rows]

def main():
    print("main 입니다.")
    print(read_data())


if __name__ == '__main__':
    main()