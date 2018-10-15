# Toolpath Analysis

A basic program to perform Data analysis on gcode files. Currently it can handle small gcode files of upto 100,000 lines well. Larger gcode files might have performance issues.
It is currently compatible with Simplify3D gcodes of version 4.X

The purpose of this program is to visualize the gcode data in the form of charts and graphs. This tool will allow us to understand the components of the 3D Printed part using vidual tools

## Installation

This program is written in Python. Hence using a Python IDE will make things easier in terms of executing the program. Some popular IDEs include Pycharm, Conda etc


## Dependencies

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

#### 3. Choose the module to run


## Results

The results will be available in a nice chart

![Screenshot](https://i.imgur.com/7FmlIRp.png)


![Screenshot](https://i.imgur.com/IPPJmSJ.png)

You are currently looking at the source code repository of OctoPrint. If you already installed it
(e.g. by using the Raspberry Pi targeted distribution [OctoPi](https://github.com/guysoft/OctoPi)) and only
want to find out how to use it, [the documentation](http://docs.octoprint.org/) and [the public wiki](https://github.com/foosel/OctoPrint/wiki)
might be of more interest for you. You might also want to subscribe to join 
[the community forum at discourse.octoprint.org](https://discourse.octoprint.org) where there are other active users who might be

