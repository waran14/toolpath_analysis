# Toolpath Analysis

A very basic tool to study the material usage in 3D printed parts. Material consumption can be broken down based on the type of 3D printing feature (rafts, outlines, infill etc). This will allow the user to make smart decisions while configuring the print settings. The data is visualized using charts and text summary. Currently the program can handle small gcode files of upto 100,000 lines well. Larger gcode files might have performance issues.

Compatibility: The program is currently compatible with Simplify3D gcodes of version 4.X and higher


## Installation and Dependencies

This program is written in Python. Hence using a Python IDE will make things easier in terms of executing the program. Some popular IDEs include Pycharm, Conda etc

The program is written in Python. It is compatible with the 3.5 and higher. Although 2.7 should also work just fine. The following Python libraries will be required to get this program running 

    Pandas
    Numpy
    re
    math
    Matplotlib
    Seaborn
    Pathlib

All these libraries can be installed using `pip` from the Terminal window (on Mac) or the cmd prompt (Windows)

## Configuration

Open `da_gcode.py` file in your favorite python IDE and follow the steps below

#### 1. Select the input file
User needs to provide an input gcode file (generated from Simplify3D). Only Plaintext gcode files are compatible as of now. But this includes a major chunk of desktop printers in the market. Copy the gcode filepath from your desktop and enter it in the following section. 

        self.inputfilepath = Path("C:/Users/Username/PycharmProjects/learning/midsizefile.gcode")
        
#### 2. Select the Layer Range
A start and end layer is required to compute the print properties within that range. `self.startlayer` can take any values greater than 0 and and `self.endlayer` can take any value equal to or greater than the Start layer value. If you would like to compute the stats for the entire print, set starting layer to 1 and ending layer to a very large number- 999999999 (this might take a few minutes to complete)

        self.startlayer = 1        # must be greater than 0
        self.endlayer = 500         # enter a large number like 999999 if you want to go until the end

#### 3. Choose the module to run

Module 1: Calculate the distance traveled by the toolhead
This module will compute the distance traveled by the nozzle during printing moves and travel moves. A simple bar chart is used to represent this data visually. Uncomment `self.distancetraveled()` and `self.distanceGraphs()` to run this section of the program

        # Module 1: uncomment to calculate the distance traveled
        # self.distancetraveled()
        # self.distanceGraphs()
        
Module 2: Calculate the filament usage, categorized by feature
This module calcualtes the filament consumed by each feature eg. amount of filament consumed by the Outlines and plots a nice pie chart to compare the individual contributions 

        # Module 2: uncomment to calculate the extrusion amounts for each feature
        self.extByFeature()
        self.extrusionGraphs()

## Results

Sample summary and charts for Distance Traveled by the nozzle 

    Total extrusion distance:  33419.2097 mm
    Total travel distance:  1543.1156 mm
    Total distance traveled by the Toolhead:  34962.3254 mm

![Screenshot](https://i.imgur.com/IPPJmSJ.png)

Sample summary and charts for the amount of filament consumed (length in raw filament)

    Outlines:  392.646 mm
    Infill:  411.4081 mm
    Supports:  0.0 mm
    Solid Layers (Top and Bottom):  184.3608 mm
    Other Features:  0.0 mm
    Total length of filament used:  994.7766 mm
    
![Screenshot](https://i.imgur.com/7FmlIRp.png)


## References

To learn more about gcode files and commands
- [Marlin Gcode commands](http://marlinfw.org/meta/gcode/) 
- [RepRap Wiki](https://reprap.org/wiki/G-code)
- [Simplify3D Gcode 101](https://www.simplify3d.com/support/articles/3d-printing-gcode-tutorial/)

