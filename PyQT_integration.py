from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QFileDialog,
                             QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton)

import pandas as pd
from pandas import DataFrame
import re
import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pathlib import Path
import simple_ui_1

class MainWindow(QMainWindow):

    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)
        self.ui = simple_ui_1.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_browse.clicked.connect(self.browseFileDialog)

        # self.inputfilepath = 'C:\\Users\\Dinesh\\Desktop\\Test gcodes\\benchy_simple.gcode'
        self.startlayer = 1
        self.endlayer = 5000
        self.emode = 'A'

        self.gepattern = re.compile(r"G1\sX\d+\.\d+\sY\d+\.\d+\sE\d+\.\d+")
        self.gonepattern = re.compile(r"G1\sX\d+\.\d+\sY\d+\.\d+\sE\d+\.\d+\sF\d+")
        self.gtrpattern = re.compile(r"G1\sX\d+\.\d+\sY\d+\.\d+\sF\d+")

        self.ftpattern = re.compile(r";\sfeature\s\w+")
        self.layerpattern = re.compile(r";\slayer\s")
        self.toolcompattern = re.compile(r";\stool\s")

        self.resetextpattern = re.compile(r"G92\sE0")
        self.zpattern = re.compile(r"G1\sZ\d+\.\d+")

        self.tablelist = []
        self.newdataframe = DataFrame(columns=['Xc', 'Yc', 'Zc', 'E', 'F', 'FT', 'EW', 'LH', 'Layer'])
        self.layerheight = 0.2
        self.extwidth = 0.4 * 0.5
        self.fildia = 1.75
        self.extmult = 0.92

        self.gc_summary_dt = {}
        self.ft_var = str
        self.tc_ew = 0.0
        self.tc_lh = 0.0
        self.gc_z = 0.0
        self.cmt_layer = int

        # parse the gcode into a dataframe
        # self.gcodetodf()

        # uncomment to calculate the extrusion amounts for each feature
        # self.extByFeature()
        # self.extrusionGraphs()

    def browseFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.inputfilepath, _ = QFileDialog.getOpenFileName(self, "Select a Gcode file", "",
                                                  "All Files (*);;Gcode Files (*.gcode)", options=options)
        if self.inputfilepath:
            self.ui.lineEdit_filename.setText(self.inputfilepath)
            self.ui.label_status.setText('file selected')
        else:
            self.ui.label_status.setText('File does not exist. Select the correct path')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
