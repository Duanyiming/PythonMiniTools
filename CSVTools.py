# -*- coding: utf-8 -*-
#! python3

import csv
import numpy

def writeCSV(path, data):
    #TODO listX2  [[],[],[]]
    with open(path, "a+") as f:
        writer = csv.writer(f)
        writer.writerows(data)
        
def readCSV(path):
    with open(path, "r") as csvFile:
        dict_reader = csv.DictReader(csvFile)
        for i in dict_reader:
            print(i)      # >>> {'name': 'Li', 'score': '80'}
        return dict_reader

if __name__ == "__main__":
    data=[["name","score"],['li',100],["sad",100]]
    writeCSV("instance2.csv",data)
    data=readCSV("instance2.csv")
