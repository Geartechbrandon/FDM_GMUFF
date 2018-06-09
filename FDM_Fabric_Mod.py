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


#Released 06/ /2018
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

#File name

inFile = input('Filename: ')
			##printer specifications
			##eventually change to .cfg, .json, or other input file format
#printer max height
machHeight = input('Printer max height (mm): ')

#lift height
liftHeight = input('Minimum height to left print head (mm): ')

#wait time
pauseTime = input('Hold time after lift (s): ')

#interface layers
totalNumFabrics = input('How many pieces to insert: ')

#layer height to skip
fabricThick = input('How thick is the material (mm): ')
	#test valid number (<0.5)

#interface layers begin
begLayerNum = input('How many layers to skip before adding material: ')
	#test number is int
		#if not report error and request new number
		#if zero notify that gcode will be offset to print on fabric
#Test file for correct number of base layers
	#if number of interface layers is greater than number of base layer print warning




print(inFile) #DebugTest
print (os.path.isfile(inFile))

readInFile = open(inFile,'r')

#Create copy file 
#Test line and copy
	#If test layer is a begLayerNum input lift and pause

