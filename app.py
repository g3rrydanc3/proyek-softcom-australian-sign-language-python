import collections
import os
import csv

dataDirectory = "./signs/"

dataFieldName = ['x', 'y', 'z', 'roll', '#pitch', '#yaw', 'thumb', 'fore', 'index', 'ring',
                 '#little', '#keycode', '#gs1', '#gs2', '#receiver']     #PREFIX # = IGNORE

allData = {}

def load():
    print "Load data to memory..."
    for signer in os.listdir(dataDirectory):
        if not os.path.isfile(dataDirectory + signer):    #CHECK IS IT FOLDER?
            signerDirectory = dataDirectory + signer
            allData[signer] = {}
            for signFile in os.listdir(signerDirectory):
                signOutput =  signFile.split(".")[0][:-1]
                dictReader = csv.DictReader(open(signerDirectory + "/" + signFile, "rb"),
                                            fieldnames=dataFieldName,
                                            delimiter=',', quotechar='"')
                allData[signer][signOutput] = []
                for row in dictReader:
                    tempArray = {}
                    for key in row:
                        if key[0] != "#":
                            #print signer + " " + signOutput + " " + key
                            tempArray[key] = row[key]
                    allData[signer][signOutput].append(tempArray)


def normalize():
    print "Normalize data..."
    for signer in allData:
        for signOutput in allData[signer]:
            #print signer + " " + signOutput + str(len(allData[signer][signOutput]))
            print signer + " " + signOutput + str(allData[signer][signOutput][0])

def learn():
    print "Learning..."

def main():
    load()
    normalize()
    learn()
    while True:
        print "1. TODO MENU"
        inputMenu = raw_input("Please enter number: ")
        if  inputMenu == "1":
            print "1"
        elif inputMenu == "2":
            print "2"




if __name__ == "__main__":
    main()
