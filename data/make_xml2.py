import csv

def read_data(file):
    list=[]
    with open(file) as f:
        file_reader = csv.DictReader(f, restval=3)
        print(str(file_reader))



read_data('size_label.txt')


