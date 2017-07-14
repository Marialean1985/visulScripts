import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns

def prSetting(  ):
	plt.clf()
	plt.xticks(weight='bold')
	plt.yticks(weight='bold')
	plt.tick_params(labelsize=9)
	#plt.figure(figsize=(3.1, 3))
	plt.tight_layout()
#plt.xlabel("Spot Price",fontsize=14, weight='bold')
#plhg
	return
def plotAnewFigure ( xString, yString, fileString, InputArray, binRanges):
	prSetting()
	sns_plot=sns.distplot(InputArray, kde=False, hist=True,color='black',bins=binRanges )
	sns_plot.set_xlabel(xString,fontsize=34, weight='bold')
	sns_plot.set_ylabel(yString,fontsize=34,weight='bold')
	fig=sns_plot.get_figure()
	fig.savefig(fileString,bbox_inches='tight')
	return
AxisLableFont=14
sns.set(color_codes=True)
sns.set_context("paper",font_scale=1.5, rc={"lines.linewidth": 1.5})
sns.set_style("whitegrid")
sns.set_style({'axes.edgecolor': '0'})
sns.set_style({'axes.linewidth': 1.0})
#print(sns.axes_style())
prSetting()
x = pd.read_csv('HistogramInputs/NYSECleaned.csv',skiprows=2)
#x.replace('   ', 0)
#print(x.head())
#print(x.describe())
plotAnewFigure ( xString="Spot Price", yString="Frequency", fileString="FinalHistograms/spotPrice.pdf",InputArray=x.Open, binRanges=np.linspace(0,640,50))
#----------------------
plotAnewFigure ( xString="Net Chg", yString="Frequency", fileString="FinalHistograms/NetChg.pdf", InputArray=x['Net Chg'], binRanges=np.linspace(-10,10,50))
#----------------------

y = pd.read_csv('HistogramInputs/FFT_Output.txt',skiprows=0,header=None,delim_whitespace=True)
InputArray=list(y[0])+list(y[1])
print(len(InputArray))
#print(y.describe())
plotAnewFigure ( xString="FFT output", yString="Frequency", fileString="FinalHistograms/FFT_output.pdf", InputArray=InputArray, binRanges=np.linspace(-500,500,50))
#----------------------
z = pd.read_csv('HistogramInputs/EEG Eye State.arff.txt',skiprows=20,header=None)
#print(z[1])
Z_all=list(z[0])
#print(z.describe())
for i in range(1,13):
	Z_all=Z_all+list(z[i])
print(len(Z_all))

plotAnewFigure ( xString="EEG", yString="Frequency", fileString="FinalHistograms/EEG.pdf", InputArray=Z_all, binRanges=np.linspace(3500,5000,50))
#--------------------------
z = pd.read_csv('HistogramInputs/Train_Arabic_Digit.txt',skiprows=0,header=None,delim_whitespace=True)
#print(z[1])
Z_all=list(z[0])
print(z.describe())
for i in range(1,12):
        Z_all=Z_all+list(z[i])
print(len(Z_all))

plotAnewFigure ( xString="Voice", yString="Frequency", fileString="FinalHistograms/Voice.pdf", InputArray=Z_all, binRanges=np.linspace(-10,10,50))
#------------------

z = pd.read_csv('HistogramInputs/savedTensors/InputTesnsor.csv',skiprows=17,header=None,delim_whitespace=True)
z=z.T
Z_all=z[0]
#print(z.describe())
#for i in range(1,12):
#        Z_all=Z_all+list(z[i])
print(len(Z_all))

plotAnewFigure ( xString="activation values", yString="Frequency", fileString="FinalHistograms/AlexnetInput.pdf", InputArray=Z_all, binRanges=np.linspace(-10,10,50))
#-------------------

z = pd.read_csv('HistogramInputs/savedTensors/OutLastLayerVGG.csv',skiprows=17,header=None,delim_whitespace=True)
z=z.T
Z_all=z[0]
#print(z.describe())
#for i in range(1,12):
#        Z_all=Z_all+list(z[i])
print(len(Z_all))

plotAnewFigure ( xString="activation values", yString="Frequency", fileString="FinalHistograms/AlexnetOutput.pdf", InputArray=Z_all, binRanges=np.linspace(-2,2,50))

#-----------------------------
z = pd.read_csv('HistogramInputs/savedTensors/InputLastLayerVGG.csv',skiprows=17,header=None,delim_whitespace=True)
z=z.T
Z_all=z[0]
#print(z.describe())
#for i in range(1,12):
#        Z_all=Z_all+list(z[i])
print(len(Z_all))

plotAnewFigure ( xString="activation values", yString="Frequency", fileString="FinalHistograms/VGGInput.pdf", InputArray=Z_all, binRanges=np.linspace(-2,2,50))
#----------------------------
z = pd.read_csv('HistogramInputs/savedTensors/OutLastLayerVGG.csv',skiprows=17,header=None,delim_whitespace=True)
z=z.T
Z_all=z[0]
#print(z.describe())
#for i in range(1,12):
#        Z_all=Z_all+list(z[i])
print(len(Z_all))

plotAnewFigure ( xString="activation values", yString="Frequency", fileString="FinalHistograms/VGGOutput.pdf", InputArray=Z_all, binRanges=np.linspace(-2,2,50))
