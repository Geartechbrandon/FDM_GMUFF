# FDM_GMUFF
Developing a script to make it easier to modify gcode files in order to print across a layer of fabric.

This code allows the user to:
-Choose how much of a gap to be left for the inserted fabric
  --Ex. Fabric is 0.1mm gap chosen is 0.09. Program inserts a permanet offset to all subsequent layers to compensate.
-Can have n number of gaps
  --Ex. User wants to insert three different pieces spaced precisely 4 layers apart and starting at layer 150.
-Can adjust how long the print head stays raised (paused) and can use printer controls to extend the pause indefinitely

To build source into compiled executable binary, requires cx_Freeze to be installed, run:
>python setup.py build
