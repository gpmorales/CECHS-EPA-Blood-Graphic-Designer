# ALL CODE WRITTEN BY GEORGE MORALES @ EMORY UNIVERSITY
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BloodFrame = pd.DataFrame(pd.read_excel("EPA blood metals 9-16-2022_ES2.xlsx"));

''' Before Event '''
Patient = BloodFrame.iloc[1:45,0]; # patients

D = BloodFrame.iloc[1:7,3]; # Col D (Manganese, micro)
DEvent = BloodFrame.iloc[7:49,3]; # Event

FEvent = BloodFrame.iloc[7:49,5]; # Col F (Cobalt)

J = BloodFrame.iloc[1:7,9]; # Col J (Arsenic)
JEvent = BloodFrame.iloc[7:49,9]; # Col J (Arsenic)

N = BloodFrame.iloc[1:7,13]; # Col N # Cadmium, ng/mL
NEvent = BloodFrame.iloc[7:49,13];

Axis = pd.DataFrame(np.array([0]));

# Prints a single graph for that patient
def Plot(FrEl, patientNum, RefA, RefB, Bool, isCobalt): #FUNCTION 1
    el = patientNum;
    Reading = FrEl.iloc[el];

    FrEl = FrEl.tolist();
    FrEl = np.array(FrEl, dtype = np.float64);
    Min = np.nanmin(FrEl);
    Max = np.nanmax(FrEl);


    if(len(FrEl) < 7): # NON EVENT SAMPLE
        plt.axhline(y = RefB, color = "green", linewidth = 3, linestyle ='--'); # Reference lines

        if( not(RefA == 0 and RefB == 0) and Max > 5):
            plt.annotate("Blood {} Level of Typical Person in the U.S. : {} {}g/{}L".format(element,RefB,unitB,unit), ha = 'center', va = 'bottom', xytext = (0, RefB - 0.50), xy = (0, RefB));
            #plt.annotate("Blood {} Level of Typical Child in the U.S. : {} {}g/{}L".format(element,RefB,unitB,unit), ha = 'center', va = 'bottom', xytext = (0, RefB - 0.20), xy = (0, RefB));

            plt.annotate("[Your Level = {} {}g/{}L]".format(round(Reading,1),unitB, unit), ha = 'center', va = 'bottom',
                  xytext = (0, Reading + 1.5), xy = (0, Reading + 0.15), arrowprops = {'facecolor' : 'white'});

        elif( Max < 5 ):
            plt.annotate("[Your Level = {} {}g/{}L]".format(round(Reading,1),unitB, unit), ha = 'center', va = 'bottom',
                  xytext = (0, Reading + 0.2), xy = (0, Reading + 0.05), arrowprops = {'facecolor' : 'white'});

            plt.annotate("Blood {} Level of Typical Person in the U.S. : {} {}g/{}L".format(element,RefB,unitB,unit), ha = 'center', va = 'bottom', xytext = (0, RefB - 0.07), xy = (0, RefB));
            #plt.annotate("Blood {} Level of Typical Child in the U.S. : {} {}g/{}L".format(element,RefB,unitB,unit), ha = 'center', va = 'bottom', xytext = (0, RefB - 0.20), xy = (0, RefB));

        else:
            plt.annotate("[Your Level = {} {}g/{}L]".format(round(Reading,1),unitB, unit), ha = 'center', va = 'bottom',
                  xytext = (0, Reading + 0.6), xy = (0, Reading + 0.1), arrowprops = {'facecolor' : 'white'});


    if(len(FrEl) > 7): # EVENT SAMPLE
        if( not Bool ):
            if (np.nanmax(FrEl) > 2.5 and np.nanmax(FrEl) < 6):
                Offset = 0.4;
            elif (np.nanmax(FrEl) > 6 and np.nanmax(FrEl) < 10):
                Offset = 0.9;
            elif (np.nanmax(FrEl) > 15 and np.nanmax(FrEl) < 28 ):
                Offset = 3;
            elif (np.nanmax(FrEl) > 28 and np.nanmax(FrEl) < 45):
                Offset = 4;
            else:
                Offset = 1.5;

            if (np.nanmax(FrEl) > 2.5 and np.nanmax(FrEl) < 6):
                OffsetB = 0.1;
            elif (np.nanmax(FrEl) > 6 and np.nanmax(FrEl) < 10):
                OffsetB = 0.2;
            elif (np.nanmax(FrEl) > 15 and np.nanmax(FrEl) < 28):
                OffsetB = 0.6;
            elif (np.nanmax(FrEl) > 28 and np.nanmax(FrEl) < 45):
                OffsetB = 0.8;
            elif (np.nanmax(FrEl) > 45 and np.nanmax(FrEl) < 90):
                OffsetB = 0.9;
            else:
                OffsetB = 1.0;

            plt.annotate("[Your Level = {} {}g/{}L]".format(round(Reading,1),unitB,unit), ha = 'center', va = 'bottom',
                      xytext = (0, Reading + 1*Offset), xy = (0, Reading + OffsetB), arrowprops = {'facecolor' : 'white'}); #""""""""""""""""""""""""""""""""""""""""""""""

        elif( Bool ):
            plt.annotate("[Your Level = {} {}g/{}L]".format(round(Reading,1),unitB,unit), ha = 'center', va = 'bottom',
                      xytext = (0, Reading - 5), xy = (0, Reading - 1.0), arrowprops = {'facecolor' : 'white'});

    if(len(FrEl) > 7): el = el + 6;

    print("CURRENT PATIENT ----------------------------------------------------------------------------------------------------------------------------> " + Patient.iloc[el]);
    plt.title("Capillary Blood {} Level Results".format(element));

    # FOR EVENT SAMPLES
    if(len(FrEl) > 7):
        if( not (RefA == 0 and RefB == 0)):
            Offset = 0.5 if np.nanmax(FrEl) > 2.5 else 0.5;
            Offset = 0.08 if np.nanmax(FrEl) < 2.8 else 0.5;

            if(not isCobalt):
                plt.annotate("Blood {} Level of Typical Person in the U.S. : {} {}g/{}L".format(element,RefB,unitB,unit), ha = 'center', va = 'bottom', xytext = (-5.5, RefB + 0.4 * Offset), xy = (0, RefB));

            elif(isCobalt):
                plt.annotate("Blood {} Level of Typical Adult in the U.S. : {} {}g/{}L".format(element,RefB,unitB,unit), ha = 'center', va = 'bottom', xytext = (-5.5, RefB + Offset), xy = (0, RefB));

            plt.axhline(y = RefB, color = "green", linewidth = 3, linestyle ='--'); # Reference lines


        Offset = 0.45 if np.nanmax(FrEl) > 15 else 0.06;
        plt.axhline(y = Max , color = "Blue", linewidth = 3, linestyle = '-.'); # Reference lines
        plt.annotate('Westside Health Day Event Max : {} {}g/{}L'.format(round(Max,1),unitB, unit), ha = 'center', va = 'bottom', xytext = (4.5, Max + 2.74*Offset), xy = (0, Max));

    # Graphing
    plt.ylabel("Capillary Blood {} Level ({}g/{}L)".format(element, unitB, unit));

    # Reference values for each Column
    plt.axhline(y = 0, color = "white", linewidth = 0);

    if(Max < 5):
        plt.axhline(y = 3, color = "white");
    elif(Max < 10):
        plt.axhline(y = 10, color = "white");
    else:
        plt.axhline(y = 32, color = "white");
        plt.axhline(y = 5, color = "white", linewidth = 0);

    plt.axvline(x = -10, color = "white", linewidth = 0, linestyle = '--');
    plt.axvline(x = 10, color = "white", linewidth = 0, linestyle = '--');
    plt.axvline(x = 0, color = "grey", linewidth = 1, linestyle = '--');

    plt.scatter(Axis, Reading, s = 160, color = 'black', marker = 'X', alpha = 1);
    print("-------------------------------------------------------------------------------------------------------------------------------------> Reading: " + str(Reading));
    plt.show();

# Reference values for each Column **************************************************************
DF = JEvent; #J

isCobalt = False;
if(DF.equals(D)):
    RefA = 1.8;
    RefB = 17.9; ''' Manganese - Child'''
    unit = ""; # Unit for Concentration measurements ***************************
    unitB = "µ"; # second unit for Concentration measurements ***************************
    element = "Manganese"; # ******************** Element present in blood

if(DF.equals(DEvent)):
    RefA = 1.8;
    RefB = 16.5; ''' Manganese - Person'''
    unit = ""; # Unit for Concentration measurements ***************************
    unitB = "µ"; # second unit for Concentration measurements ***************************
    element = "Manganese"; # ******************** Element present in blood

if(DF.equals(FEvent)):
    RefA = 0.1;
    RefB = 0.67; ''' Cobalt - Person'''
    unit = ""; # Unit for Concentration measurements ***************************
    unitB = "µ"; # second unit for Concentration measurements ***************************
    element = "Cobalt"; # ******************** Element present in blood
    isCobalt = True;

if(DF.equals(J)):
    RefA = 0.0;
    RefB = 1.00; ''' Arsenic - Child'''
    unit = ""; # Unit for Concentration measurements ***************************
    unitB = "µ"; # second unit for Concentration measurements ***************************
    element = "Arsenic"; # ******************** Element present in blood

if(DF.equals(JEvent)):
    RefA = 0.0;
    RefB = 1.00; ''' Arsenic - Person'''
    unit = ""; # Unit for Concentration measurements ***************************
    unitB = "µ"; # second unit for Concentration measurements ***************************
    element = "Arsenic"; # ******************** Element present in blood

if(DF.equals(N)):
    RefA = 0.0;
    RefB = 0.190; ''' Cadmium - Child'''
    unit = ""; # Unit for Concentration measurements ***************************
    unitB = "µ"; # second unit for Concentration measurements ***************************
    element = "Cadmium"; # ******************** Element present in blood

if(DF.equals(NEvent)):
    RefA = 0.0;
    RefB = 1.28; ''' Cadmium - Person'''
    unit = ""; # Unit for Concentration measurements ***************************
    unitB = "µ"; # second unit for Concentration measurements ***************************
    element = "Cadmium"; # ******************** Element present in blood


#SELECT PATIENT (0-5) FOR NONEVENT OR (0-37) FOR EVENT PARTICIPANTS *******

SAMPLE_ID = 37;

Plot(DF, SAMPLE_ID, RefA, RefB, False, isCobalt); # Run Magnesium visuals 


#*************************************************************************************************************************************************************************************
''' Lead Visualizations '''
FrPb = BloodFrame.iloc[1:7,15]; # Col Pb
FrPbEvent = BloodFrame.iloc[7:45,15]; # Col Pb

Axis = pd.DataFrame(np.array([0]));

def PlotLead(LeadFr, patientNum, RefA, RefPb): #FUNCTION 2
    el = patientNum;
    Reading = LeadFr.iloc[el];

    plt.scatter(Axis, Reading, s = 170, color = 'black', marker = 'X', alpha = 1);

    # Must have in all Lead graphs
    plt.annotate('[ Reference Value : {} µg/dL ]'.format(3.50), ha = 'center', va = 'bottom', xytext = (-5.5, 3.50 + 0.07), xy = (0, 3.50));
    plt.axhline(y = RefPb, color = "Green", linewidth = 3, linestyle = '--'); # Reference lines

    if(len(LeadFr) < 7): #NON EVENT SAMPLE
        plt.annotate("Blood Lead Level of Typical Child in the U.S. : {} µg/dL".format(RefPb), ha = 'center', va = 'bottom', xytext = (-5.5, RefPb + 0.07), xy = (4, RefPb));
        if(Reading < 2.2 or Reading > RefPb + 0.2):
            plt.annotate("[Your Level = {} µg/dL]".format(round(Reading,2)), ha = 'center', va = 'bottom',
                      xytext = (4, Reading - 0.05), xy = (0.3, Reading), arrowprops = {'facecolor' : 'white'});
        elif( Reading < RefA):
            plt.annotate("[Your Level = {} µg/dL]".format(round(Reading,2)), ha = 'center', va = 'bottom',
                      xytext = (-0.1, Reading - 0.5), xy = (0, Reading - 0.1), arrowprops = {'facecolor' : 'white'});

    if(len(LeadFr) > 7): # Event sample
        plt.annotate("Blood Lead Level of Typical Person in the U.S. : {} µg/dL".format(RefPb), ha = 'center', va = 'bottom', xytext = (-5.5, RefPb + 0.07), xy = (4, RefPb));
        if( Reading < RefA or Reading > 4.0):
            plt.annotate("[Your Level = {} µg/dL]".format(round(Reading,2)), ha = 'center', va = 'bottom',
                      xytext = (-0.0, Reading + 1 * 0.35), xy = (0, Reading + 0.1), arrowprops = {'facecolor' : 'white'});

        elif(Reading > RefA):
            plt.annotate("[Your Level = {} µg/dL]".format(round(Reading,2)), ha = 'center', va = 'bottom',
                      xytext = (4, Reading - 0.05), xy = (0.3, Reading), arrowprops = {'facecolor' : 'white'});


    if(len(LeadFr) > 7): el = el + 6;

    print("CURRENT PATIENT ---------------------------------------------------------------------------------------------------> " + Patient.iloc[el]);
    print("-------------------------------------------------------------------------------------------------------------------> Reading: " + str(Reading));
    plt.title("Capillary Blood Lead Level Results");

    # For EVENT SAMPLES
    if(len(LeadFr) > 7):
        LeadFr = LeadFr.tolist();
        LeadFr = np.array(LeadFr, dtype = np.float64);
        Min = np.nanmin(LeadFr);
        Max = np.nanmax(LeadFr);
        Max = round(Max,1);

        plt.axhline(y = Min, color = "Blue", linewidth = 3, linestyle = '-.'); # Reference lines
        if( Reading >= Min and Reading < Min + 0.3 or Reading > 4.0 ):
            plt.annotate('Westside Health Day Event Min : {} µg/dL'.format(round(Min,2)), ha = 'center', va = 'bottom', xytext = (-6, Min + 0.1), xy = (4, Min));
            plt.annotate('Westside Health Day Event Max : {} µg/dL'.format(round(Max,2)), ha = 'center', va = 'bottom', xytext = (-6, Max + 0.1), xy = (4, Max));
        else:
            plt.annotate('Westside Health Day Event Min : {} µg/dL'.format(round(Min,2)), ha = 'center', va = 'bottom', xytext = (0, Min + 0.1), xy = (4, Min));
            plt.annotate('Westside Health Day Event Max : {} µg/dL'.format(round(Max,2)), ha = 'center', va = 'bottom', xytext = (0, Max + 0.1), xy = (4, Max));

        plt.axhline(y = Max , color = "Blue", linewidth = 3, linestyle = '-.'); # Reference lines

    # Reference values for each Column
    plt.axhline(y = 0, color = "white", linewidth = 3);
    plt.axhline(y = RefA, color = "orange", linewidth = 3); # Reference lines
    plt.axvline(x = -10, color = "white", linewidth = 0, linestyle = '--');
    plt.axvline(x = 10, color = "white", linewidth = 0, linestyle = '--');
    plt.axvline(x = 0, color = "grey", linewidth = 1, linestyle = '--');
    plt.axhline(y = 5, color = "white");

    plt.ylabel("{} (µg/dL)".format("Capillary Blood Lead Level"));

    plt.show();


# Select some parameters
# Reference values for each Column ***********************************************************************************
DF = FrPbEvent;

if(DF.equals(FrPb)):
    RefPb = 2.02;
else:
    RefPb = 2.41;

#SELECT PATIENT (0-5) FOR NONEVENT OR (0-37) FOR EVENT PARTICIPANTS *******
SAMPLE_ID = 37;

#PlotLead(DF, SAMPLE_ID, 3.50, RefPb); ''' RUN VISUALS '''
