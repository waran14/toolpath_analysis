import pandas as pd
from pandas import DataFrame
import re
import math
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1500)


class Application():


    def __init__(self):

        self.inputfilepath ='C:\\Users\\Dinesh\\Desktop\\Test gcodes\\benchy_simple.gcode'
        self.startlayer = 1
        self.endlayer = 240
        self.emode = 'A'

        self.gepattern = re.compile(r"G1\sX\d+\.\d+\sY\d+\.\d+\sE\d+\.\d+")
        self.gonepattern = re.compile(r"G1\sX\d+\.\d+\sY\d+\.\d+\sE\d+\.\d+\sF\d+")
        self.gtrpattern = re.compile(r"G1\sX\d+\.\d+\sY\d+\.\d+\sF\d+")

        self.ftpattern = re.compile(r";\sfeature\s\w+")
        self.layerpattern = re.compile(r";\slayer\s")
        self.toolcompattern = re.compile(r";\stool\s")

        self.resetextpattern = re.compile(r"G92\sE0")
        self.zpattern = re.compile(r"G1\sZ\d+\.\d+")

        self.layerlist = []
        self.newdataframe = DataFrame(columns=['Xc', 'Yc', 'Zc', 'E', 'F', 'FT', 'EW', 'LH', 'Layer'])
        self.layerheight = 0.2
        self.extwidth = 0.4*0.5
        self.fildia = 1.75
        self.extmult = 0.92

        self.gc_summary_dt = {}
        self.ft_var = str
        self.tc_ew = 0.0
        self.tc_lh = 0.0
        self.gc_z = 0.0
        self.cmt_layer = int

        self.gcodetodf()

        # self.coordinateTable()
        # self.gcodeSummary()
        # self.extrusionAmount()
        # self.retractionCount()

        # uncomment to calculate the distance traveled
        # self.distancetraveled()
        # self.distanceGraphs()

        # uncomment to calculate the extrusion amounts for each feature
        self.extByFeature()
        self.extrusionGraphs()

    def gc_g1xyef(self):
        self.newdataframe = self.newdataframe.append(
            {'Xc': float(self.tlist[1][1:]), 'Yc': float(self.tlist[2][1:]), 'Zc': self.gc_z,
             'E': float(self.tlist[3][1:]),
             'F': float(self.tlist[4][1:]), 'FT': self.ft_var, 'EW': self.tc_ew, 'LH': self.tc_lh,
             'Layer': self.cmt_layer},
            ignore_index=True)

    def gc_g1xye(self):
        self.newdataframe = self.newdataframe.append(
            {'Xc': float(self.tlist[1][1:]), 'Yc': float(self.tlist[2][1:]), 'Zc': self.gc_z,
             'E': float(self.tlist[3][1:]),
             'F': None, 'FT': self.ft_var, 'EW': self.tc_ew, 'LH': self.tc_lh, 'Layer': self.cmt_layer},
            ignore_index=True)

    def gc_g1xyf(self):
        self.newdataframe = self.newdataframe.append(
            {'Xc': float(self.tlist[1][1:]), 'Yc': float(self.tlist[2][1:]), 'Zc': self.gc_z, 'E': None,
             'F': float(self.tlist[3][1:]), 'FT': self.ft_var, 'EW': self.tc_ew, 'LH': self.tc_lh,
             'Layer': self.cmt_layer},
            ignore_index=True)

    def gc_g92e0(self):
        if self.newdataframe.empty is False:
            self.newdataframe = self.newdataframe.append(
                {'Xc': self.newdataframe['Xc'].iloc[-1], 'Yc': self.newdataframe['Yc'].iloc[-1],
                 'Zc': self.gc_z,
                 'E': 0.0, 'F': None, 'FT': self.ft_var, 'EW': self.tc_ew, 'LH': self.tc_lh,
                 'Layer': self.cmt_layer}, ignore_index=True)
        elif self.newdataframe.empty is True:
            return

    def gc_ftype(self):
        self.ft_var = self.clist[3]

    def gc_laycmt(self):
        self.cmt_layer = float(self.tlist[2][:-1])

    def gc_toolcmt(self):
        self.tc_ew = float(self.tlist[3][1:])
        self.tc_lh = float(self.tlist[2][1:-1])

    def gc_g1z(self):
        self.gc_z = float(self.tlist[1][1:])

    def contd(self):
        return

    def gcodetodf(self):

        # self.df_cols = {'featureType': str, 'toolew': 0.0, 'toollh': 0.0, 'gcodeZ': 0.0, 'layerCmt': int}

        with open(self.inputfilepath, 'r') as ifile:

            lflag = False
            for i, item in enumerate(ifile):

                layermatch = self.layerpattern.match(item)
                self.tlist = item.split(' ')
                self.clist = re.split(r"(\w+)", item)

                if layermatch and (str(self.tlist[2][:-1]) == 'end' or int(self.tlist[2][:-1]) == (self.endlayer + 1)):
                    break

                if (layermatch and int(self.tlist[2][:-1]) == self.startlayer) or lflag is True:
                    lflag = True
                    # clist = re.split(r"(\w+)", item)

                    map_gcpat = {bool(self.gonepattern.match(item)): self.gc_g1xyef,
                                 bool(self.gepattern.match(item)): self.gc_g1xye,
                                 bool(self.gtrpattern.match(item)): self.gc_g1xyf,
                                 bool(self.resetextpattern.match(item)): self.gc_g92e0,
                                 bool(self.ftpattern.match(item)): self.gc_ftype,
                                 bool(self.toolcompattern.match(item)): self.gc_toolcmt,
                                 bool(self.layerpattern.match(item)): self.gc_laycmt,
                                 bool(self.zpattern.match(item)): self.gc_g1z}

                    map_gcpat.get(True, self.contd)()

        # print(self.newdataframe)

    def gcodeSummary(self):

        with open(self.inputfilepath, 'r') as ifile:
            head = [next(ifile) for x in range(0, 200)]
            # tail = [line for line in ifile.readlines()[-10:]]

        gcsumpattern = re.compile(r";\s\s\s\w+")
        patt_retractiondistance = re.compile(r";\s\s\sextruderRetractionDistance,")
        patt_extrusionmultiplier = re.compile(r";\s\s\sextrusionMultiplier,")

        for item in head:
            mat_retractiondistance = patt_retractiondistance.match(item)
            mat_extrusionmultiplier = patt_extrusionmultiplier.match(item)

            if mat_retractiondistance:
                self.gc_summary_dt['retractionDistance'] = float(item.split(',')[1])
                break

            if mat_extrusionmultiplier:
                self.gc_summary_dt['extrusionMultiplier'] = float(item.split(',')[1])
                break

    def extrusionAmount(self):

        tempevalue = (self.extmult * self.layerheight * self.extwidth) / (math.pi * math.pow((self.fildia / 2), 2))
        evalue = 0.0 if pd.isnull(self.newdataframe.iloc[0]['E']) is True else self.newdataframe.iloc[0]['E']
        totaldistance = 0.0
        totalextrusion = 0.0


        for i, row in self.newdataframe.iterrows():

            if i < 1:
                continue

            if pd.isnull(self.newdataframe.iloc[i]['E']) is True:
                evalue = 0.0
                continue

            x2 = row['Xc']
            y2 = row['Yc']
            x1 = self.newdataframe.iloc[i-1]['Xc']
            y1 = self.newdataframe.iloc[i-1]['Yc']

            edist = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))
            totaldistance += edist

            evalue = (evalue + (tempevalue * edist)) if self.emode == 'A' else (tempevalue * edist)


            # for visual inspection
            eformat = float(format(evalue, '.4f'))
            # print(i, x2, y2, self.newdataframe.iloc[i]['E'], eformat, [True if self.newdataframe.iloc[i]['E'] == eformat else False])

        print(self.newdataframe)
        print(float(format(totaldistance, '.4f')))

    def retractionCount(self):

        # cannot handle weird cases where there is a combo of stationary and non stationary in a single retract move

        retcount = 0
        nonstretpattern = re.compile(r"G1\sX\d+\.\d+\sY\d+\.\d+\sE-{}\d+".format(self.gc_retractiondistance))
        stretpattern = re.compile(r"G1\sE-{}\d+\sF\d+".format(self.gc_retractiondistance))
        comboretpattern = re.compile(r"G1\sE-\d+\.\d+")

        for item in self.layerlist:
            nonstretmatch = nonstretpattern.match(item)
            stretmatch = stretpattern.match(item)

            if stretmatch or nonstretmatch:
                retcount += 1
                print(item)
                continue

        rdisttotal = float(format((retcount*self.gc_retractiondistance), '.4f'))

        print(f'total no. of retractions: {retcount}')
        print(f'Total distance retracted: {rdisttotal} mm')

    def distancetraveled(self):

        self.dist_total = 0.0
        self.dist = {'extrusion': 0.0, 'travel': 0.0}

        for i, row in self.newdataframe.iterrows():

            if i < 1:
                # skip the first line as there is no previous coordinate to calculate from
                # print(self.newdataframe.iloc[i]['E'])
                continue

            self.distance_tup = (pd.isnull(self.newdataframe.iloc[i]['E']), pd.isnull(self.newdataframe.iloc[i-1]['E']))

            # distance between 2 points formula
            edist = math.sqrt(math.pow((row['Xc']-self.newdataframe.iloc[i-1]['Xc']), 2)
                              + math.pow((row['Yc']-self.newdataframe.iloc[i-1]['Yc']), 2))
            self.dist_total += edist

            if self.distance_tup in ((False, False), (False, True)):
                self.dist['extrusion'] += edist
            elif self.distance_tup in ((True, True), (True, False)):
                self.dist['travel'] += edist

        print(f'total extrusion distance: ', float(format(self.dist['extrusion'], '.4f')))
        print(f'total extrusion distance: ', float(format(self.dist['travel'], '.4f')))
        print(f'total distance: ', float(format(self.dist_total, '.4f')))

    def distanceGraphs(self):

        pieslices = [self.dist['travel'], self.dist['extrusion']]
        pielabels = ['Travel', 'Extrusion']
        plt.pie(pieslices, labels=pielabels, startangle=90, autopct='%1.1f%%')
        plt.subplots_adjust(top=1.0, bottom=0)
        # plt.bar(self.ext_total, self.totalext, label='Extrusion %')
        # plt.xlabel('X')
        # plt.ylabel('Y')
        plt.show(block=True)

    def extByFeature(self):

        self.map_ext = {'outer': 0.0,
                 'inner': 0.0,
                 'solid': 0.0,
                 'infill': 0.0,
                 'support': 0.0,
                 'other': 0.0}

        self.ext_total = 0.0
        self.ftypes = [x for x in self.map_ext.keys() if x != 'other']

        for i, row in self.newdataframe.iterrows():

            if i < 1 is True or pd.isnull(self.newdataframe.iloc[i]['E']) is True or self.newdataframe.iloc[i]['E'] == 0:
                continue

            edist = self.newdataframe.iloc[i]['E'] - self.newdataframe.iloc[i - 1]['E']
            self.ext_total += edist
            self.map_ext[self.newdataframe.iloc[i]['FT'] if self.newdataframe.iloc[i]['FT'] in self.ftypes else 'other'] += edist

        # print(self.newdataframe)

        print(f'outline extrusion distance: ', float(format((self.map_ext['outer'] + self.map_ext['inner']), '.4f')))
        print(f'infill extrusion distance: ', float(format(self.map_ext['infill'], '.4f')))
        print(f'support extrusion distance: ', float(format(self.map_ext['support'], '.4f')))
        print(f'solid layer extrusion distance: ', float(format(self.map_ext['solid'], '.4f')))
        print(f'other extrusion distance: ', float(format(self.map_ext['other'], '.4f')))
        print(f'total extrusion distance: ', float(format(self.ext_total, '.4f')))

    def extrusionGraphs(self):

        pieslices = [float(x) for x in self.map_ext.values() if x > 0.0]
        pielabels = [x for x in self.map_ext.keys() if self.map_ext[x] > 0.0]
        plt.style.use('ggplot')
        plt.pie(pieslices, labels=pielabels, startangle=90, autopct='%1.1f%%')
        plt.subplots_adjust(top=1.0, bottom=0)
        plt.show(block=True)

        sns.barplot(x=[x for x in self.map_ext.keys()], y=[float(x) for x in self.map_ext.values()])
        plt.show(block=True)


app = Application()
