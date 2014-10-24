#assingment ver 1

import os
import sys
import csv
import re


    
#initialized the file path
def get_fid(filepath):
        if os.path.exists(filepath):
                xa = str(input('Please input FID feature : '))
                query = 'FID == ' + xa
                print 'Query:'
                print query
                print
                
                import csv
                csvData = csv.reader(open(filepath))
                csvTable = []
                isHeader = True
                for row in csvData:
                    if isHeader:
                        isHeader = False
                        headerRow = row
                        for i in range(len(headerRow)):
                            # replace spaces w/ underscores in column headers
                            headerRow[i] = headerRow[i].replace(' ', '_')
                    else:
                        csvTable.append(row)
                # determine column types: string/int/float
                colType = []
                for i in range(len(headerRow)):
                    isFloat = True
                    isInt = True
                    for j in range(len(csvTable)):
                        try:
                            v = float(csvTable[j][i])
                            if not v == int(v):
                                    isInt = False
                        except ValueError:
                                isFloat = False
                                isInt = False
                    colT = ''
                    if isInt:
                            colT = 'int'
                    elif isFloat:
                            colT = 'float'
                    else:
                            colT = 'string'
                    colType.append(colT)

                # print headerRow[i], colT
    
                # run the query
                for j in range(len(csvTable)):
                    # assign the column variables
                    for i in range(len(headerRow)):
                            if colType[i] == 'string':
                                    exec(headerRow[i] + '=' + '"' + csvTable[j][i] + '"')
                            elif colType[i] == 'float':
                                    exec(headerRow[i] + '=' + 'float("' + csvTable[j][i] + '")')
                            elif colType[i] == 'int':
                                    exec(headerRow[i] + '=' + 'int("' + csvTable[j][i] + '")')

                    # output the rows matching the query
                    if eval(query):
                            tab = csvTable[j]
                            print "Information of FID feature" + xa + " is"
                            print "------------------------------"
                            print "|" + headerRow[0] + " : " + tab[0] + "    | "
                            print "|" + headerRow[1] + " : " + tab[1] + "    | " 
                            print "|" + headerRow[2] + " : " + tab[2] + "                   |"
                            print "|" + headerRow[3] + " : " + tab[3] + "         |"
                            print "|" + headerRow[4] + " : " + tab[4] + "     |"
                            print "|" + headerRow[5] + " : " + tab[5] + "          |"
                            print "|" + headerRow[6] + " : " + tab[6] + "                 |"
                            print "|" + headerRow[7] + " : " + tab[7] + "       |"
                            print "|" + headerRow[8] + " : " + tab[8] + "               |"
                            print "|" + headerRow[9] + " : " + tab[9] + "              |"
                            print "|" + headerRow[10] + " : " + tab[10] + "     |"
                            print "|" + headerRow[11] + " : " + tab[11] + "       |"
                            print "|" + headerRow[12] + " : " + tab[12] + "     |"
                            print "|" + headerRow[13] + " : " + tab[13] + "   |"
                            print "|" + headerRow[14] + " : " + tab[14] + "               |"
                            print "|" + headerRow[15] + " : " + tab[15] + "               |"
                            print "|" + headerRow[16] + " : " + tab[16] + "               |"
                            print "|" + headerRow[17] + " : " + tab[17] + "              |"
                            print "|" + headerRow[18] + " : " + tab[18] + "             |"
                            print "|" + headerRow[19] + " : " + tab[19] + "              |"
                            print "|" + headerRow[20] + " : " + tab[20] + "              |"
                            print "------------------------------"
        elif IOError:
                print "------------------" 
                print "!!!!!warning!!!!!!" 
                print "!!file not exist!!" 
                print "!!!!!warning!!!!!!" 
                print "------------------"
        
def get_file_path(filename):
	cur_dir = os.getcwd()
	file_path = os.path.join(os.getcwd(), filename)
	return file_path



def test_file(filepath):#this function also provide a header checker#
        if os.path.exists(filepath):
                with open(filepath, 'rU') as csvfile:
                        reader = [line.split(',') for line in csvfile.readlines()]
                        blank = re.compile(r'\s*')
                        print "checking format data"
                        for i in reader[0]:
                                if blank.match(i).end() == len(i):
                                        print "------------------" 
                                        print "!!!!!warning!!!!!!" 
                                        print "!data not correct!" 
                                        print "!!!!!warning!!!!!!" 
                                        print "------------------"
                                
        elif IOError:
                print "------------------" 
                print "!!!!!warning!!!!!!" 
                print "!!file not exist!!" 
                print "!!!!!warning!!!!!!" 
                print "------------------"
                
def read_csv_file(filepath):
        if os.path.exists(filepath): 
                with open(filepath, 'rU') as csvfile:                
                        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                        for row in reader:        
                                print ' '.join(row) #eliminate sign of [ ]
                                print ""
        elif IOError:
                print "------------------" 
                print "!!!!!warning!!!!!!" 
                print "!!file not exist!!" 
                print "!!!!!warning!!!!!!" 
                print "------------------"
                        
                                

#path = get_file_path(y)

ax = 1

while True:
        print "start program!!!!!"
        print " "
        print "select menu :"
        print " "
        print "[1] checking header correction"
        print "[2] display data structure"
        print "[3] belum ada"
        print "[4] belum ada"
        print "[5] search features by FID"
        print "[6] belum ada"
        print "[7] quit"
        print ""
        x = input('please choose : ')
        if x == 1:
                print "please type your file (*.csv)"
                y = raw_input ('filename: ')
                print ""
                z = get_file_path(y)
                if test_file(z) == 0:
                        test_file(z)
                
                #print test_file(z)
                os.system("pause")
        elif x == 2:
                print "please type your file (*.csv)"
                y = raw_input ('filename: ')
                print ""
                z = get_file_path(y)
                if read_csv_file(z) == 0:
                        read_csv_file(z)
                os.system("pause")
        elif x == 3:
                print "please type your file (*.csv)"
                y = raw_input ('filename: ')
                print ""
                z = get_file_path(y)
                print read_csv_file(z)
                os.system("pause")
        elif x == 4:
                print "belum jadi"
                os.system("pause")
        elif x == 5:
                print "please type your file (*.csv)"
                y = raw_input ('filename: ')
                print ""
                z = get_file_path(y)
                print get_fid(z)
                os.system("pause")
        elif x == 6:
                print "belum jadi"
                os.system("pause")
        elif x == 7:
                print "goodbye"
                break
        ax += 1
        


        







	
	
	
