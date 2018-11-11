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


#Released 11/ /2018
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

#See the readme for more information on what/how to test the program 
#It will be updated as new information is available.
#Please report bugs, make suggestions, and branch any custom versions to help others.


import os.path
import sys
import time

#Will
print('             :::       ::: ::::::::::: :::        :::        ', '\n','            :+:       :+:     :+:     :+:        :+:         ', '\n','            +:+       +:+     +:+     +:+        +:+          ', '\n','            +#+  +:+  +#+     +#+     +#+        +#+           ', '\n','            +#+ +#+#+ +#+     +#+     +#+        +#+            ', '\n','             #+#+# #+#+#      #+#     #+#        #+#             ', '\n','              ###   ###   ########### ########## ##########       ', '\n')
#It
print('                         ::::::::::: :::::::::::                 ', '\n','                            :+:         :+:                      ', '\n','                            +:+         +:+                       ', '\n','                            +#+         +#+                        ', '\n','                            +#+         +#+                         ', '\n','                            #+#         #+#                          ', '\n','                        ###########     ###                           ', '\n')                  
#Print
print('        :::::::::  :::::::::  ::::::::::: ::::    ::: ::::::::::: ', '\n','       :+:    :+: :+:    :+:     :+:     :+:+:   :+:     :+:      ', '\n','       +:+    +:+ +:+    +:+     +:+     :+:+:+  +:+     +:+       ', '\n','       +#++:++#+  +#++:++#:      +#+     +#+ +:+ +#+     +#+        ', '\n','       +#+        +#+    +#+     +#+     +#+  +#+#+#     +#+         ', '\n','       #+#        #+#    #+#     #+#     #+#   #+#+#     #+#          ', '\n','       ###        ###    ### ########### ###    ####     ###           ','\n')  

#Pause to show my spiffy vintage logo.
time.sleep(5.5)
#Clear screen on Windows, uncomment. Compiled version will be expecting Windows execution and is uncommented to look vintage.
clearScreenVariable = os.system('cls')
#Clear screen for Linux and OSX, uncomment. (just trying to be cool and old school, there is no point to doing this.)
#clearScreenVariable = os.system('clear')
#The variable will contain 0 as the output from system. Otherwise this would be on the screen and not look as clean.

#Beginning header
print('\n')
print('Welcome to the FDM/FFF gcode modification unit for fabric (GMUFF)','\n')
print('Please make sure this program is opened in the same directory/folder as the GCode file(s).','\n','\n')
print('Disclaimer:','\n','Use at your own and your machine\'s risk. ', '\n', 'Modify and test this code first; ensure it works for your setup.')
print('Assumption: File is from Ultimaker CURA or S3D and in ASCii text format', '\n\n')

#Iitializations for while statements, can quickly disable inputs to focus testing (this will often cause the program to fail but makes for quick and dirty debugging)
fileTest = True
heightTest = True
fabricThickTest = True
totalNumFabricTest = True
begLayerNumTest = True
liftHeightTest = True
pauseTimeTest = True
fabricSpacingTest = True
raftCheckTest = True

#File name and directory check
while (fileTest == True):
	try:
		origGcodeFile = input('Filename: ')
		fo = open (origGcodeFile)
	except IOError:
		print ("No such file in current directory.")
		print ("Press ctrl + c to exit if needed.")
	except KeyboardInterrupt:
		print ("\n\n\n","**************","User Interrupt","**************","\n\n\n")
		sys.exit(1)
	else:
		with open(origGcodeFile) as fileGenerationTest:
			firstLineInFile = fileGenerationTest.readline()
			#Need to search for S3D or just match the first line to the S3D first line
		fileIsS3D = "; G-Code generated by Simplify3D(R)"
		#print(firstLineInFile)
		lengthOfFirstLine = len(firstLineInFile)
		lengthOfRefLine = len(fileIsS3D)
		if (lengthOfFirstLine > lengthOfRefLine):
			firstLineInFile = firstLineInFile[0:35]
			#print(firstLineInFile)

		if (firstLineInFile == fileIsS3D):
			raftCheckTest = True
			#print('Found S3D')
			#print(firstLineInFile)
		else:
			#print('Not S3D')
			raftCheckTest = False
		fileTest = False

#Maximum height of printer
while (heightTest == True):
    try:
        machHeight = float(input('Printer max height (mm): '))
    except:
        #Extra characters or anything that makes the variable become a non-integer gets caught
        print ("That doesn't seem to be a valid number.")
    else:
        if (machHeight <= 10):
            print ("Typo? A machine height of only ", machHeight," doesn't give adequate room for the head to lift with this program.")
            #Not much room to move the head so the fabric can be burned, head shifted, or injury can occur
        elif (machHeight < 100):
            print ("A machine with height of only ", machHeight," is pretty small for this process. Please be careful to avoid burns.")
            #Regardless the height, if the number is real, we exit
            heightTest = False
        else:
            heightTest = False


#Material thickness
while (fabricThickTest == True):
    try:      
        #layer height to skip
        fabricThick = float(input('How thick is the material (mm): '))
    except:
        #Extra characters or anyhting that makes the variable become a non-integer gets caught
        print ("That doesn't seem to be a valid number.")
    else:
        # Checks for negatives and zero thickness
        if (fabricThick <= 0):
            print ("Material must have a thickness greater than zero")
            fabricThickTest = True
        else:
            #Currently there is no extrusion multiplier for the layer jump so it's risky to skip more than 1.5x the layer thickness as there will be little to no layer to layer bonding
            if (fabricThick > 0.5):
                print ("Fabric layer greater than 0.5 mm can cause problems with layer adhesion at this time.","\nGood guide rule is to keep the fabric layer less than 1.5 times the layer thickness.")
                fabricThickTest = False
            else:
                #Everything looks good so far
                fabricThickTest = False


#Number of interface sections
while (totalNumFabricTest == True):
	try:
		totalNumFabrics = int(input('How many pieces to insert: '))
	except:
		#Extra characters or anything that makes the variable become a non-integer gets caught
		print ("That doesn't seem to be a valid number.")
	else:
        #Should have at least one space to make, otherwise nothing happens
		if (totalNumFabrics <= 0):
			print ("Should have at least one piece to insert or gap to make.")
			totalNumFabricTest = True
        #Everything looks good so far
		else:
			totalNumFabricTest = False


#Spacing between interface regions
if(totalNumFabrics > 1):
	while (fabricSpacingTest == True):
		try:
			layersBetweenFabric = int(input('How many printed layers between each fabric piece? '))
		except:
			print ("That doesn't seem to be a valid number.")
		else:
			#add reject <0
			if (layersBetweenFabric == 0):
				fabricQuestionTest = True
				while (fabricQuestionTest == True):
					print (layersBetweenFabric, 'layers between fabric.')
					confirmNothingBetween = input('Is this correct? (Y,N) ')
					confirmNothingBetween = confirmNothingBetween[0].upper()
					if (confirmNothingBetween == "Y"):
						fabricQuestionTest = False
						fabricSpacingTest = False
					elif (confirmNothingBetween == "N"):
						fabricQuestionTest = False
						fabricSpacingTest = True
					else:
						print (confirmNothingBetween, 'is not a valid input.')
						fabricQuestionTest = True
						fabricSpacingTest = True
			elif (layersBetweenFabric < 0):
				print( layersBetweenFabric, ' must be at least 0.' )
				fabricSpacingTest = True
			else:
				fabricSpacingTest = False

#Print layer where interface layers begin
while (begLayerNumTest == True):
	try:
		begLayerNum = int(input('What layer do we start printing on (CURA starts at 0): '))
	except:
		print ("That doesn't seem to be a valid number.") 
	else:
		if (begLayerNum < 0):
			print ("At this time we need to start with at least LAYER:0.")
			begLayerNumTest = True
		else:
			begLayerNumTest = False


#If S3D check for Raft
while (raftCheckTest): 
	buildingOnRaft = input("Printing on a raft? (Y/N)")   #Choosing Y or N we need to ensure valid input for both cases and incorrect input.
	buildingOnRaft = buildingOnRaft[0].upper()
	if (buildingOnRaft == "Y"):
		try:
			numRaftLayers = int(input('How many raft layers? ')) #Use this to check number of positive layers in S3D otherwise we don't really need to know for CURA
		except:
			print ("That doesn't seem to be a valid number.")
		else:
			raftCheckTest = False
			begLayerNumTest = False
	elif (buildingOnRaft == "N"):
		raftCheckTest = False
		begLayerNumTest = False
	else:
		print (buildingOnRaft, ' is not something I recognize.')


#Height to lift print head
while (liftHeightTest == True):
    try:
        liftHeight = float(input('Minimum height to lift printer head (mm): '))
    except:
        #Extra characters or anything that makes the variable become a non-integer gets caught
        print ("That doesn't seem to be a valid number.")
    else:
        if (liftHeight >= machHeight):
            print ("The machine height is ", machHeight," so the lifting height must be less than this.")
            liftHeightTest = True
        else:
            if (liftHeight <= fabricThick) and (begLayerNum == 0):
                print ("Need to lift the head higher than the fabric layer thickness of ", fabricThick, " .")
                liftHeightTest = True
            else:
                liftHeightTest = False
while (pauseTimeTest == True):
    #wait time
    try:
        pauseTime = float(input('Hold time after lift (min): '))
    except:
        #Extra characters or anyhting that makes the variable become a non-integer gets caught
        print ("That doesn't seem to be a valid number.")
    else:
        if (pauseTime < 0):
            print ("Time must be at least zero. Ex: 0.2, 1, 1.4, etc.")
        else:
            pauseTimeTest = False
print("Parsing File")


#DebugTests
#print(inFile) 
#print(machHeight)
#print(liftHeight)
#print(pauseTime)
#print(totalNumFabrics)
#print(fabricThick)
#print(begLayerNum)
#print (os.path.isfile(inFile))
dontWriteFile = True
fileVersionNum = 0

while (dontWriteFile):                                                  
	if origGcodeFile.endswith('.gcode'):                           #checks for .gcode
		outfile = origGcodeFile[:-6] + '_ClothMod_'+ str(fileVersionNum) + '.gcode'
		print ("Output file name: ", outfile)
	elif origGcodeFile.endswith('.txt'):                           #check for .txt file. Just at test at this time
		outfile = origGcodeFile[:-6] + '_ClothMod_'+ str(fileVersionNum) + '.gcode'
		print ("Output file name: ", outfile)
	elif origGcodeFile.endswith('.g'):                             #check for .g file. Just a test at this time unless it has CURA format
		outfile = origGcodeFile[:-6] + '_ClothMod_'+ str(fileVersionNum) + '.gcode'
		print ("Output file name: ", outfile)
	else:                                                   #catch all other error. Should loop back to file input as a test
		print ("I don't recognize this file type")

	try:									#Tries to open file
		fo = open(outfile)
	except:									#If file does not exist exception is thrown and while exits to begin writing file
		dontWriteFile = False
	else:									#If file exists then we check if user wants to overwrite existing file
		overwriteTest = True
		while (overwriteTest):
			print (outfile, " exists. ")
			overWriteStatus = input ("Overwrite? (Y/N) ")
			overWriteStatus = overWriteStatus[0].upper()

			if(overWriteStatus == "Y"):			#Yes overwrite then we exit the loop
				fo.close()
				dontWriteFile = False
				overwriteTest = False
			elif (overWriteStatus == "N"):
				fo.close()
				fileVersionNum += 1
				dontWriteFile = True
				overWriteTest = False
			else:								#If no file version increments and then we check again for an existing file
				print (overWriteStatus, 'is not something I recognize')
				overwriteTest = True
			
zSearch ='Z'        #Declare search for the Z change. This only works in CURA or software that makes 1 zchange. Some software lists Z at every line.
zPosNum = 0			#Initializing the z position to zero

print ("First layer starts on: ",firstLayer)
changeBegin = False
        #CURA converts the input mm/s into mm/min for Marlin
        #Time of 5 minutes hold is then 5 min to travel 10mm
        #10mm/5min = 2mm/min
liftHeightShort = liftHeight - 10  #Buffer so the lift head can use the last 10 mm to move since many machines cannot start and stop movement.
holdTime = 10 / pauseTime    #mm/min

        #the following will get written, line by line, to the file once the firt layer has been found
skipParameterList = ["LIFT HEIGHT", 'G0 F3600 Z' + str(liftHeightShort), ";HOLD TIME", 'G0 F' + str(holdTime) + ' Z' + str(liftHeight), 'RESUME PRINTING']

counter = 0
with open (outfile, 'wt') as writeOutFile:                      #opens the copy file for writing into and closes when the loop is completed
	with open (origGcodeFile, 'rt') as readInFile:                 #with opens the file and closes it once everything has been read
		for line in readInFile:                             #Begins reading each line in the input file one at a time to 'line'
																##Need to test if this is a new layer and check for zhop but this is more complicated
																##and will need to be added into later versions. Possibly similar logic for processing the different gcode file types
		   # layerNum = ';LAYER:' + str(counter)             #sets the layer with the counter on each loop
																   #doesn't work because the 'line' itterates more than the layers do. This test needs to be set else where.
			lineLength = len(line)                          #reads the length of the current string variable for the current line

		#Find zero layer ;LAYER:0
			if (begLayerNum == 0) and (line == firstLayer):
				print ("Printing on fabric.")
				changeBegin = true           
			elif (line == firstLayer):
				print ("Fabric layer found.")
				changeBegin = true

			zLineGrab = line.find(zSearch)                
		#write non changed lines to file
			if (changeBegin == True) and (zLineGrab != (-1)):
				#break line into movement and zNumber
				zLineGrab = zLineGrab + 1
				stringLength = lineLength - zLineGrab
				zStartPos = line[zLineGrab:]
				zStartPos = int(zStartPos)
				zEndPosition = zStartPos + fabricThick

				#Add the fabric thickness to the zheight
			else:
				writeOutFile.write(line)