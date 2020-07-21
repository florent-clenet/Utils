import csv
import os

class Utils(object):

    def __sortKeysList(data):
        #get all keys from all dict
        allKeys = list()
        for x in range(0, len(data)):
            allKeys += list(data[x].keys()) #all keys

        #clean dupicated keys
        cleanKeys = list()
        indent_key = 0
        for x in range (0,len(allKeys)):
            cleanKeys.append(allKeys[0])
            try:
                while True:
                    allKeys.remove(cleanKeys[indent_key])
            except ValueError:
                pass #do nothing
            indent_key += 1
            if len(allKeys) == 0:
                break #job done
        return cleanKeys
        #All keys are listed, no clone anymore


    #@staticmethod
    def list2csv(self,data=list(),fileName="report.csv",path="."):
        """
            From list of dictionaries, write all the data in a csv file.
            Data are modified before writting so you can read it easily with a simple text editor.
            All columns alignment are made by adding spaces after values/keys.

            :param data: list of dictionaries
            :param fileName: output csv file name
            :param path: file path
            :type data: Dictionary list
            :type fileName

            :Example:
            
            Output example:
            |column 1|column 2      |VeryLongColumn 3|column 4      |
            |value1  |value1        |value1          |value1        |
            |value2  |VeryLongValue2|value2          |              |
            |value3  |              |value3          |VeryLongValue3|

            It work even if dictionnaries don't have the same keys.
            Unknow key will be added and value filles with ' '.
        """

        #test path and data lenght before starting
        if (len(data) != 0) and (path != None):
            #if file already exist, delete and create
            if os.path.isfile(path+"/"+fileName) == True:
                os.remove(path+"/"+fileName)
            with open(path+"/"+fileName, "w",newline='') as csvfile:
                #from data, list all keys
                keys = list()
                keys = Utils.__sortKeysList(data)
                
                #add key length in front of key name (for column width)
                #example : KeyOne : 6, KeyTwo : 6, KeyThree : 8
                ColumnWidth = dict()
                for x in range (0, len(keys)):
                    ColumnWidth[keys[x]] = len(keys[x])
                
                #If Key is missing in dict, add it with empty string value
                for x in range (0, len(data)):
                    for y in range (0, len(keys)):
                        if keys[y] not in data[x].keys():
                            data[x][keys[y]] = ""


                #adapt length with length of values (in case of value length > key length)
                for i in range (0, len(data)):
                    for x in range (0, len(data[i])):
                        width = len(str(data[i][keys[x]]))
                        if (ColumnWidth[keys[x]]) < width:
                            ColumnWidth[keys[x]] = width
                #all column width are now listed
                
                #copy keys list
                keysShift = keys.copy()
                #add space shift in keys
                for i in range (0, len(keys)):
                    #for each column name, change width
                    keysShift[i] = keysShift[i] + ((ColumnWidth[keys[i]] - len(str(keysShift[i]))) * " ")
                
                #for each dictionnary, change values by adding space for column width
                for i in range (0, len(data)):
                    for x in range (0, len(data[i])):
                        data[i][keys[x]] = str(data[i][keys[x]]) + ((ColumnWidth[keys[x]] - len(str(data[i][keys[x]]))) * " ")

                #use csv.writer to write keys with space shift
                writer = csv.writer(csvfile,delimiter='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(keysShift)

                #use csv.DictWriter to write all values in the good column (fieldname option)
                Dictwriter = csv.DictWriter(csvfile, fieldnames=keys, delimiter='|', quoting=csv.QUOTE_MINIMAL)
                for i in range (0, len(data)):
                    Dictwriter.writerow(data[i])

