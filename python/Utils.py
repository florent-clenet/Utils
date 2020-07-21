import csv
import os
import copy

class Utils(object):

    @staticmethod
    def __sortKeysList(data):
        """
            Return listed keys from dict list
        """
        allKeys = list()
        for x in range(0, len(data)):
            allKeys += copy.deepcopy(list(data[x].keys())) #copy all keys
        #clean dupicated keys
        cleanKeys = list(dict.fromkeys(allKeys))
        return cleanKeys
        #All keys are listed, no clone anymore

    @staticmethod
    def __dict_to_list(rowdict, fieldnames, ColumnWidth):
        """
            From dict, return sorted values by keys
            If key don't exist in the key, just add some spaces
            This function do not modify input data
        """
        returnedList = list()
        #for each key...
        for key in fieldnames:
            restval = None
            #...if dict don't know the key, add only space " "
            if rowdict.get(key,restval) == None:
                returnedList.append(ColumnWidth[key] * " ")
            #...else, if key is know by dict, add value with good amount of " " for readable csv file
            else:
                returnedList.append(str(rowdict[key]) + ((ColumnWidth[key] - len(str(rowdict[key]))) * " ") )
        return returnedList


    @staticmethod
    def list2csv(data=list(),fileName="report.csv",path='.', valueDelimiter=','):
        """
            From list of dictionaries, write all the data in a csv file.
            Data are modified before writting so you can read it easily with a simple text editor.
            All columns alignment are made by adding spaces after values/keys.
            This function do not corrupt your input data and work even if dictionnaries don't have the same keys.

            :param data: list of dictionaries
            :param fileName: output csv file name
            :param path: file path
            :param path: file path
            :type data: dictionary list
            :type fileName : string
            :type path : string
            :type valueDelimiter : string

            :Example:
            
            Output example:
            |column 1|column 2      |VeryLongColumn 3|column 4      |
            |value1  |value1        |value1          |value1        |
            |value2  |VeryLongValue2|value2          |              |
            |value3  |              |value3          |VeryLongValue3|

        """

        #test path and data lenght before starting
        if(len(data) != 0):
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

                #adapt length with length of values (in case of value length > key length)
                for i in range (0, len(data)):
                    for x in range (0, len(data[i])):
                        #width = len(str(data[i][keys[x]]))
                        width = len(str(data[i].get(keys[x])))
                        if (ColumnWidth[keys[x]]) < width:
                            ColumnWidth[keys[x]] = width
                #all column width are now listed
                
                #copy keys list
                keysShift = keys.copy()
                #add space shift in keys
                for i in range (0, len(keys)):
                    #for each column name, change width
                    keysShift[i] = keysShift[i] + ((ColumnWidth[keys[i]] - len(str(keysShift[i]))) * " ")
                
                #use csv.writer to write keys with space shift
                writer = csv.writer(csvfile,delimiter=str(valueDelimiter), quoting=csv.QUOTE_MINIMAL)
                writer.writerow(keysShift)

                #writerow all value for each key by calling __dict_to_list
                for i in range (0, len(data)):
                    writer.writerow(Utils.__dict_to_list(copy.deepcopy(data[i]), keys, ColumnWidth))
        else: print("ERROR : no input data")

