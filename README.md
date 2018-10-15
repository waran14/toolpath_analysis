# Toolpath Analysis

A basic program to perform Data analysis on gcode files. Currently it can handle small gcode files of upto 100,000 lines well. Larger gcode files might have performance issues.
It is currently compatible with Simplify3D gcodes of version 4.X

The purpose of this program is to visualize the gcode data in the form of charts and graphs. This tool will allow us to understand the components of the 3D Printed part using vidual tools

## Installation and Dependencies

This program is written in Python. Hence using a Python IDE will make things easier in terms of executing the program. Some popular IDEs include Pycharm, Conda etc

The program is written in Python. It is compatible with the 3.5 and higher
The Python libraries required to get this program going are 

    Pandas
    Numpy
    re
    math
    Matplotlib
    Seaborn
    Pathlib

All these libraries can be installed using `pip` from the Terminal window (on Mac) or the cmd prompt (Windows)

        pip install 

## Configuration

#### 1. Select the input file
User needs to provide an input gcode file (generated from Simplify3D). Only Plaintext gcode files are compatible as of now. Copy the filepath from your desktop and enter the path in variable `self.inputfilepath`. Sample filepath available here

        self.inputfilepath = Path("C:/Users/Username/PycharmProjects/learning/midsizefile.gcode")
        
#### 2. Select the Layer Range
Starting layer is set using the variable `self.startlayer` and ending layer using `self.endlayer`. Key in the numbers accordingly to a specific section of the model. Alternatively, set starting layer to 1 and ending layer to a very large number- 999999999 to analyze a entire gcode file (this might take a few minutes to complete)

        self.startlayer = 1        # must be greater than 1
        self.endlayer = 50         # enter a large number like 999999 if you want to go until the end

#### 3. Choose the module to run

Module 1: Calculate the distance traveled by the toolhead

        # Module 1: uncomment to calculate the distance traveled
        self.distancetraveled()
        self.distanceGraphs()
        
Module 2: Calculate the filament usage, categorized by feature

        # Module 2: uncomment to calculate the extrusion amounts for each feature
        self.extByFeature()
        self.extrusionGraphs()

## Results

Distance Traveled

    Total extrusion distance:  33419.2097 mm
    Total travel distance:  1543.1156 mm
    Total distance traveled by the Toolhead:  34962.3254 mm

![Screenshot](https://i.imgur.com/IPPJmSJ.png)

Extrusion amount Summary (length in raw filament)

    Outlines:  392.646 mm
    Infill:  411.4081 mm
    Supports:  0.0 mm
    Solid Layers (Top and Bottom):  184.3608 mm
    Other Features:  0.0 mm
    Total length of filament used:  994.7766 mm
    
![Screenshot](https://i.imgur.com/7FmlIRp.png)






To learn more about gcode files and commands
[Marlin Gcode commands](http://marlinfw.org/meta/gcode/) 
[RepRap Wiki](https://reprap.org/wiki/G-code)
[Simplify3D Gcode 101](https://www.simplify3d.com/support/articles/3d-printing-gcode-tutorial/)

