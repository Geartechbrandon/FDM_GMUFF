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

import os.path


#Will
print('                 :::       ::: ::::::::::: :::        :::        ', '\n','               :+:       :+:     :+:     :+:        :+:         ', '\n','              +:+       +:+     +:+     +:+        +:+          ', '\n','             +#+  +:+  +#+     +#+     +#+        +#+           ', '\n','            +#+ +#+#+ +#+     +#+     +#+        +#+            ', '\n','            #+#+# #+#+#      #+#     #+#        #+#             ', '\n','            ###   ###   ########### ########## ##########       ', '\n')
#It
print('                         ::::::::::: :::::::::::                 ', '\n','                           :+:         :+:                      ', '\n','                          +:+         +:+                       ', '\n','                         +#+         +#+                        ', '\n','                        +#+         +#+                         ', '\n','                       #+#         #+#                          ', '\n','                  ###########     ###                           ', '\n')                  
#Print
print('       :::::::::  :::::::::  ::::::::::: ::::    ::: ::::::::::: ', '\n','     :+:    :+: :+:    :+:     :+:     :+:+:   :+:     :+:      ', '\n','    +:+    +:+ +:+    +:+     +:+     :+:+:+  +:+     +:+       ', '\n','   +#++:++#+  +#++:++#:      +#+     +#+ +:+ +#+     +#+        ', '\n','  +#+        +#+    +#+     +#+     +#+  +#+#+#     +#+         ', '\n',' #+#        #+#    #+#     #+#     #+#   #+#+#     #+#          ', '\n','###        ###    ### ########### ###    ####     ###           ','\n')  

#Begining header
print('\n','\n')
print('Welcome to the FDM/FFF gcode modification unit for fabric (GMUFF)','\n')
print('Please make sure this .py file is in the same directory/folder as the GCode file(s).')

#File location

inFile = input('Filename: ')

#DebugTest
print(inFile)
print (os.path.isfile(inFile))

readInFile = open(inFile,'r')


