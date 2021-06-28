# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 10:05:52 2021

@author: rgibs
"""
import random

# 5214 lines / 3 = 1738 examples
# .1 * 1738 = 173.8 test examples, or 174
# BETTER SOLUTION: make a list of selected examples for testing
    # create 2 new files: training and testing sets
    # read all lines in original
    # use 'for i in lines:'? iterate through lines, compare to selected line 
        # numbers, and copy to correct file

total = 1738
testsize = 174
testlist = []
linelist = []
while len(testlist) < testsize:
    r = random.randint(1,total)
    if r not in testlist: testlist.append(r)
print(testlist)
for i in testlist: #expand chosen examples to include all 3 line numbers
    start = ((i - 1) * 3) #first line of example
    linelist.append(start)
    linelist.append(start+1)
    linelist.append(start+2)
if ((len(linelist) == (3*testsize))): print('# lines is correct')
else: print('# lines incorrect:', len(linelist))

with open('C:/Users/rgibs/Downloads/ulf_dataset_all.txt') as f:
    with open('C:/Users/rgibs/Downloads/ulf_dataset_training.txt', 'w') as trainfile:
        with open('C:/Users/rgibs/Downloads/ulf_dataset_testing.txt', 'w') as testfile:
            lines = f.readlines()
            for i in range(len(lines)):
                if i in linelist: #if selected for testing, add to testing
                    testfile.write(lines[i])
                else:
                    trainfile.write(lines[i])
            testfile.close()
        trainfile.close()
    with open('C:/Users/rgibs/Downloads/ulf_dataset_training.txt') as trainfile:
        with open('C:/Users/rgibs/Downloads/ulf_dataset_testing.txt') as testfile:
            trainlines = trainfile.readlines()
            testlines = testfile.readlines()
            
            if (len(trainlines) == ((1738-174)*3)): print('train is correct length')
            else: print('train is incorrect length:', len(trainlines))
            if (len(testlines) == (174*3)): print('test is correct length')
            else: print('test is incorrect length:', len(testlines))
            
            for line in trainlines:
                if (line != '<|endoftext|>\n') and (line in testlines):
                    print('repeated line:', line)
                    break
            for line in testlines:
                if line != '<|endoftext|>\n' and line in trainlines:
                    print('repeated line:', line)
                    break
            testfile.close()
        trainfile.close()
    f.close()