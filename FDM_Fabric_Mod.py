#Python 3.6.5
#Brandon F. Langdon
#__/\\\______________/\\\__/\\\\\\\\\\\__/\\\\\\\\\\\\\_______/\\\\\\\\\\___/\\\\\\\\\\\\____        
# _\/\\\_____________\/\\\_\/////\\\///__\/\\\/////////\\\___/\\\///////\\\_\/\\\////////\\\__       
#  _\/\\\_____________\/\\\_____\/\\\_____\/\\\_______\/\\\__\///______/\\\__\/\\\______\//\\\_      
#   _\//\\\____/\\\____/\\\______\/\\\_____\/\\\\\\\\\\\\\/__________/\\\//___\/\\\_______\/\\\_     
#    __\//\\\__/\\\\\__/\\\_______\/\\\_____\/\\\/////////___________\////\\\__\/\\\_______\/\\\_    
#     ___\//\\\/\\\/\\\/\\\________\/\\\_____\/\\\_______________________\//\\\_\/\\\_______\/\\\_   
#      ____\//\\\\\\//\\\\\_________\/\\\_____\/\\\______________/\\\______/\\\__\/\\\_______/\\\__  
#       _____\//\\\__\//\\\_______/\\\\\\\\\\\_\/\\\_____________\///\\\\\\\\\/___\/\\\\\\\\\\\\/___ 
#        ______\///____\///_______\///////////__\///________________\/////////_____\////////////_____


#Released 07/ /2018
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>


#Things to add
#Error checking such as rafts and brims for zero layer printing
#Functionality for multiple materials ie different material thicknesses
#Functionality for improved material adhesion such as increased flow, print speed, etc
#Test that head lift always occurs after the auto bed leveling




import os.path


#Will
print('             :::       ::: ::::::::::: :::        :::        ', '\n','            :+:       :+:     :+:     :+:        :+:         ', '\n','            +:+       +:+     +:+     +:+        +:+          ', '\n','            +#+  +:+  +#+     +#+     +#+        +#+           ', '\n','            +#+ +#+#+ +#+     +#+     +#+        +#+            ', '\n','             #+#+# #+#+#      #+#     #+#        #+#             ', '\n','              ###   ###   ########### ########## ##########       ', '\n')
#It
print('                         ::::::::::: :::::::::::                 ', '\n','                            :+:         :+:                      ', '\n','                            +:+         +:+                       ', '\n','                            +#+         +#+                        ', '\n','                            +#+         +#+                         ', '\n','                            #+#         #+#                          ', '\n','                        ###########     ###                           ', '\n')                  
#Print
print('        :::::::::  :::::::::  ::::::::::: ::::    ::: ::::::::::: ', '\n','       :+:    :+: :+:    :+:     :+:     :+:+:   :+:     :+:      ', '\n','       +:+    +:+ +:+    +:+     +:+     :+:+:+  +:+     +:+       ', '\n','       +#++:++#+  +#++:++#:      +#+     +#+ +:+ +#+     +#+        ', '\n','       +#+        +#+    +#+     +#+     +#+  +#+#+#     +#+         ', '\n','       #+#        #+#    #+#     #+#     #+#   #+#+#     #+#          ', '\n','       ###        ###    ### ########### ###    ####     ###           ','\n')  

#Begining header
print('\n','\n')
print('Welcome to the FDM/FFF gcode modification unit for fabric (GMUFF)','\n')
print('Please make sure this .py file is in the same directory/folder as the GCode file(s).','\n','\n')
print('Disclaimer:','\n','Use at your own and your machine\'s risk. ', '\n', 'Modify and test this code first, ensure it works for your setup.', '\n','See the readme for more information on what/how to test, it will be updated as new information is available.','\n', 'Please report bugs, make suggestions, and branch any custom versions to help others. ')
print('Assumption: File is from Ultimaker CURA and in ASCii text format')
print('Last warning is that this version doesn\'t do much with error checking.') #Delete once more sanity checks are added such as checking num etc

#File name

inFile = input('Filename: ')
			##printer specifications
			##eventually change to .cfg, .json, or other input file format
#printer max height
machHeight = input('Printer max height (mm): ')

#lift height
liftHeight = input('Minimum height to left print head (mm): ')

#wait time
pauseTime = input('Hold time after lift (min): ')

#interface layers
totalNumFabrics = input('How many pieces to insert: ')

#layer height to skip
fabricThick = input('How thick is the material (mm): ')
	#test valid number (<0.5)

#interface layers begin
begLayerNum = input('How many layers to skip before adding material (starts at 0): ')
	#test number is int
		#if not report error and request new number
		#if zero notify that gcode will be offset to print on fabric
#Test file for correct number of base layers
	#if number of interface layers is greater than number of base layer print warning



#DebugTests
print(inFile) 
print(machHeight)
print(liftHeight)
print(pauseTime)
print(totalNumFabrics)
print(fabricThick)
print(begLayerNum)

print (os.path.isfile(inFile))
                                                    #
    if inFile.endswith('.gcode'):                           #checks for .gcode
        outfile = inFile[:-6] + '_ClothMod.gcode'
        print (outfile)
    elif inFile.endswith('.txt'):                           #check for .txt file. Just at test at this time
        outfile = inFile[:-4] + '_ClothMod.gcode'
        print (outfile)
    elif inFile.endswith('.g'):                             #check for .g file. Just a test at this time unless it has CURA format
        outfile = inFile[:-2] + '_ClothMod.gcode'
        print (outfile)
    else:                                                   #catch all other error. Should loop back to file input as a test
        print ("I don't recognize this file type")

writeOutFile = open(outfile, 'wt')                      #opens the copy file for writing into

#zInitPosition = 0                                       #variable container for z original poition
#zModPosition = 0                                        #variable container for changes in the zposition through the build

                                                        #Consider adding intelligence to spread the layer jump throughut the build
                                                            ##for instance layers below target position shrink a little (0.18 instead of 0.2)
                                                            ##some number of layers above the target are also shrunk by a little. Help spread any distorition
                                                            ##Probably would require a small flow rate adjustment for some machines
zSearch ='Z'
zPosNum = 0
firstLayer = ';LAYER:0'
changeBegin = false
        #CURA converts the input mm/s into mm/min for Marlin
        #Time of 5 minutes hold is then 5 min to travel 10mm
        #10mm/5min = 2mm/min
liftHeightShort = liftHeight - 10
holdTime = 10 / pauseTime    #mm/min

        #this will get written, line by line, to the file once the firt layer has been found
skipParameterList = ["LIFT HEIGHT", 'G0 F3600 Z' + str(liftHeightShort), ";HOLD TIME", 'G0 F' + holdTime + ' Z' +liftHeight, 'RESUME PRINTING']

print(';LAYER:' + str(counter))
print (type(counter))

counter = 0

with open (inFile, 'rt') as readInFile:                 #with opens the file and closes it once everything has been read
    for line in readInFile:                             #Begins reading each line in the input file one at a time to 'line'
                                                            ##Need to test if this is a new layer and check for zhop but this is more complicated
                                                            ##and will need to be added into later versions. Possibly similar logic for processing the different gcode file types
        
       # layerNum = ';LAYER:' + str(counter)             #sets the layer with the counter on each loop
                                                               #doesn't work because the 'line' itterates more than the layers do. This test needs to be set else where.
        lineLength = len(line)                          #reads the length of the current string variable for the current line

    #Find zero layer ;LAYER:0
        if (begLayerNum == 0):
            print ("Printing on fabric.")
            changeBegin = true
            #Insert skipParameterList            
        elif (line == firstLayer):
            print ("Fabric layer found.")
            changeBegin = true
            #Insert skipParameterList                   Should write all this to the file (doesn't need to know what the z layer was/should be yet) then get z layer info on next loop

         #ends beginning layer search. find() outputs either -1 if not found or the index of the character(s) in the searched string
        zLineGrab = line.find(zSearch)                
    #write non changed lines to file
        if (changeBegin == true and zLineGrab != (-1)):
            #break line into movement and zNumber
            zLineGrab = zLineGrab + 1
            stringLength = lineLength - zLineGrab
            zStartPos = line[zLineGrab:]
            zStartPos = int(zStartPos)
            zEndPosition = zStartPos + fabrickThick

            #Add the fabric thickness to the zheight
        else
            writeOutFile.write(line)
    #modify 




    #if line.find(zSearch) != -1:                        #Tests if the line string contains Z (This can be generalized to some gcode programs but not all, ex Skeinforge adds Z to everyline)
    #    zPosNum = line.find(zSearch)
    #    zInitPoition = line[zPosNum + 1:]

        #if (skipBegin == true and line == layerNum)     #Signals that next line is to 
        #    nextLineGrab = true

   
        
        
        elif (counter == begLayerNum):       #tests that both cases are true
            skipBegin = true
            origLine = line
            truncateLine = line[zPosNum:]
             
            editLine = truncateLine + 
            
        elif (line == layerNum):
            ++counter
            
            
            writeOutFile.write(line)
                       
         

    else:                                           #writes line to file
            writeOutFile.write(line)
            
    ++counter

        
    



writeOutFile.close()                                    #closes the copy file




#readInFile = open(inFile,'rt')  #opens text file for read only and text format  (ex in_file)
#content = readInFile.read()     #reads opened file into a string
#readInFile.close()              #closes the text file
#lines = []                               #Empty list
#with open (inFile, 'rt') as readInFile:     #opens the file as an object
#    for line in readInFile:             #Read a line from object to the variable (loops)
#        lines.append(line)              #adds the next line into the array
#        print(lines)                    #Prints the variable contents

#Create copy file 
#Test line and copy
	#If test layer is a begLayerNum input lift and pause




