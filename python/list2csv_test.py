#!/usr/bin/env python
import os
import sys
from Utils import Utils
sys.path.insert(0, os.path.dirname(__file__))

'''
In this exemple, we are created 4 dictionnaries with different informations (Keys/values)
Those dictionnaries are pushed in a list called 'ListTest'
which is passed as parameter in function list2csv from Utils.py with file name and out path
'''

Dico1=dict()
Dico1['KEY_INFORMATION'] = 'Dict 1'
Dico1['Some_information'] = 'me'
Dico1['ActivationDate'] = '16/07/2020'
Dico1['OneMoreInformation'] = 'Lalala'

Dico2=dict()
Dico2['KEY_INFORMATION'] = 'Dict 2'
Dico2['KEYONE'] = 2
Dico2['Signature'] = 'Mister_Bean'
Dico2['ActivationDate'] = '17/07/2020 to 31/02/2021'

Dico3=dict()
Dico3['KEY_INFORMATION'] = 'Dict 3'
Dico3['OneMoreInformation'] = 'Batmobile'
Dico3['TwoMoreInformation'] = 'batarang'
Dico3['KEYONE'] = 3
Dico3['Signature'] = 'IMBATMAN?'
Dico3['ActivationDate'] = 124744512558812

Dico4=dict()
Dico4['KEY_INFORMATION'] = 'Dict 4'
Dico4['OneMoreInformation'] = 'Some_blabla_with_blibli'
Dico4['TwoMoreInformation'] = 'This is info 2'
Dico4['KEYONE'] = '4'
Dico4['Signature'] = 'ThisIsMyPersonalSignature'
Dico4['ActivationDate'] = '18/07/2020'


ListTest = list()
listSize = 1000000

print("Dictionary list in creation:")
#This test will create list with 4M lines
for i in range (0,listSize):
    Utils.ProgressBar(i,listSize)
    ListTest.append(Dico1)
    ListTest.append(Dico2)
    ListTest.append(Dico3)
    ListTest.append(Dico4)
print("\n -- Done! --")
Utils.list2csv(ListTest,"report.csv",valueDelimiter='|')