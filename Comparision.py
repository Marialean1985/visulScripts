import numpy as inp
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
import os
import math
import itertools


def prSetting(  ):
	plt.clf()
	plt.xticks(weight='bold',rotation=30)
	plt.yticks(weight='bold')
	plt.tick_params(labelsize=18)
	#plt.figure(figsize=(3.1, 3))
	plt.tight_layout()
	sns.set(color_codes=True)
	sns.set_context("paper",font_scale=1.5, rc={"lines.linewidth": 1.5})
	sns.set_style("whitegrid")
	sns.set_style({'axes.edgecolor': 'black'})
	sns.set_style({'axes.linewidth': 1.0})
	return
def plotAnewFigure ( xString, yString, xCol,yCol,hueCol,fileString, InputArray):

	prSetting()
	legend_properties = {'weight':'bold', 'size': 24}
#	palette="muted"
#	palette="gray"
#	palette="tab20"
	col_list = [ "slate","silver","dark grey","cool grey"]
#	sns.palplot(sns.xkcd_palette(col_list))
	col_list_palette = sns.xkcd_palette(col_list)
#	sns.set_palette(col_list_palette)
	sns_plot= sns.barplot(x=xCol, y=yCol, hue=hueCol,ci=None, palette=col_list_palette,data=InputArray)
	sns_plot.set_xlabel(xString,fontsize=20, weight='bold')
	sns_plot.set_ylabel(yString,fontsize=20,weight='bold')
	sns.set_style("whitegrid")
	sns_plot.spines['top'].set_visible(True)
	sns_plot.spines['right'].set_visible(True)
	sns_plot.spines['bottom'].set_linewidth(1.0)
	sns_plot.spines['left'].set_linewidth(1.0)
	sns_plot.spines['right'].set_linewidth(1.0)
	sns_plot.spines['bottom'].set_linewidth(1.0)
	sns_plot.spines['bottom'].set_color('black')
	sns_plot.spines['top'].set_color('black')
	sns_plot.spines['left'].set_color('black')
	sns_plot.spines['right'].set_color('black')
#	hatches = itertools.cycle(['/', '\\', '+', '||', 'x', '*', 'o', 'O', '.'])
#	for i, bar in enumerate(sns_plot.patches):
#		if i % 4 == 0:
#			hatch = next(hatches)
#		bar.set_hatch(hatch)
#	plt.yscale('log')
#	plt.legend(loc='upper left',fontsize=34)
#	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize=24)
	plt.legend(loc='best', prop=legend_properties)
	fig=sns_plot.get_figure()
	fig.savefig(fileString,bbox_inches='tight')
	return
prSetting()
#---------------------
visualDf=pd.DataFrame()
fileNamMap={'Alex.csv':'convolutionAlexnet.csv','Blackscholes.csv':'blackscholes.csv','FFT.csv':'fft.csv','Inversek2j.csv':'inversek2j.csv','Sobel.csv':'convolutionSobel.csv','VGG.csv':'convolutionVgg.csv', 'Jmeint.csv':'jmeint.csv'}

AppNamMap={'Alex.csv':'AlexNet','Blackscholes.csv':'Blackscholes','FFT.csv':'FFT','Inversek2j.csv':'Inversek2j','Sobel.csv':'Sobel','VGG.csv':'VGG', 'Jmeint.csv':'Jmeint'}
figureName="ComparisionAnalysis/ComparisionAnalysis.pdf"
directory= "ErrorAnalysis/Quantization"
for filename in os.listdir(directory):
	if filename.endswith(".csv")  and filename !="Kmeans.csv" : 
		CSVQuantName=os.path.join(directory, filename)
		CSVOLSBName=os.path.join('ErrorAnalysis/OLSB', filename)
		CSVPerformanceOLSBName=os.path.join('ComparisionAnalysis', fileNamMap[filename])
		CSVPerformanceQuantName=os.path.join('PerformanceAndEnergyAnalysis', fileNamMap[filename])
		print(filename)
		print(CSVPerformanceOLSBName)		
		print(CSVPerformanceQuantName)		
#		print(CSVOLSBName)
		x1 = pd.read_csv(CSVQuantName,skiprows=6, delim_whitespace=True)
		x1.drop(x1.index[0], inplace=True)
		x1.drop(x1.index[0], inplace=True)
		x2 = pd.read_csv(CSVOLSBName,skiprows=6, delim_whitespace=True)
		x2.drop(x2.index[0], inplace=True)
		x2.drop(x2.index[0], inplace=True)
		x=x1.append(x2, ignore_index=True)
#		x=x.iloc[1::2]
		olsbDF = pd.read_csv(CSVPerformanceOLSBName,skiprows=0, delim_whitespace=True)
#		olsbDF = pd.read_csv(CSVPerformanceQuantName,skiprows=0, delim_whitespace=True)
		QuantDF = pd.read_csv(CSVPerformanceQuantName,skiprows=0, delim_whitespace=True)
#		print(x1.columns.values)
#		print(x2.columns.values)
		print(x1.shape)
		print(x2.shape)
#		print(x.shape)
		MaxList=x.max()
#		print(MaxList)
#		print(len(x['Method']))
		print(figureName)
#		plotAnewFigure ( xString="Bit-Width", yString="Max Absolute Error",xCol="fileNamingArg",yCol="MAxAbsErrInput",hueCol="Method", fileString=figureName,InputArray=x)
#---------------------------
		cols_to_norm = ['MaxAbsErrorOutput']
		if filename =="Jmeint.csv":
			cols_to_norm = ['AverageRelativeError']
		x1['NormalizedAbsErr'] = x1[cols_to_norm].apply(lambda p: p/ p.max())
		x2['NormalizedAbsErr'] = x2[cols_to_norm].apply(lambda p: p/ p.max())
#		print( x1[x1['NormalizedAbsErr']<0.1].index[0], x1[x1['NormalizedAbsErr']<0.05].index[0], x1[x1['NormalizedAbsErr']<0.01].index[0], 1[x1['NormalizedAbsErr']<0.001].index[0] )
#		print(x2[x2['NormalizedAbsErr']<0.1].index[0] , x2[x2['NormalizedAbsErr']<0.05].index[0] ,x2[x2['NormalizedAbsErr']<0.01].index[0] , x2[x2['NormalizedAbsErr']<0.001].index[0] )
		olsb=[]
		quant =[]
		olsb.append(x2[x2['NormalizedAbsErr']<0.1].index[0])
		olsb.append(x2[x2['NormalizedAbsErr']<0.05].index[0])
		olsb.append(x2[x2['NormalizedAbsErr']<0.01].index[0])
		olsb.append(x2[x2['NormalizedAbsErr']<0.001].index[0])
		quant.append(x1[x1['NormalizedAbsErr']<0.1].index[0])
		quant.append(x1[x1['NormalizedAbsErr']<0.05].index[0])
		quant.append(x1[x1['NormalizedAbsErr']<0.01].index[0])
		quant.append(x1[x1['NormalizedAbsErr']<0.001].index[0])
		print(x2['fileNamingArg'][olsb[0]],x2['fileNamingArg'][olsb[1]],x2['fileNamingArg'][olsb[2]],x2['fileNamingArg'][olsb[3]])
		print(x1['fileNamingArg'][quant[0]],x1['fileNamingArg'][quant[1]],x1['fileNamingArg'][quant[2]],x1['fileNamingArg'][quant[3]])
#		print(olsbDF['runtime'])
#		print(QuantDF['runtime'])
		print(olsb)
		print(quant)
		cols_to_norm = ['runtime']
		olsbDF[cols_to_norm] = olsbDF[cols_to_norm].apply(lambda p: p/ p[15])
		QuantDF[cols_to_norm] = QuantDF[cols_to_norm].apply(lambda p: p/ p[15])
		print(olsbDF['runtime'])
		print(QuantDF['runtime'])
#		print(olsbDF['runtime'][olsb[0]-1],olsbDF['runtime'][olsb[1]-1],olsbDF['runtime'][olsb[2]-1],olsbDF['runtime'][olsb[3]-1])
		olsbRuntine=[olsbDF['runtime'][olsb[0]-1],olsbDF['runtime'][olsb[1]-1],olsbDF['runtime'][olsb[2]-1],olsbDF['runtime'][olsb[3]-1]]
#		print(QuantDF['runtime'][quant[0]-1],QuantDF['runtime'][quant[1]-1],QuantDF['runtime'][quant[2]-1],QuantDF['runtime'][quant[3]-1])
		quantRuntime=[QuantDF['runtime'][quant[0]-1],QuantDF['runtime'][quant[1]-1],QuantDF['runtime'][quant[2]-1],QuantDF['runtime'][quant[3]-1]]
		speedup=[((t1-t2)/t1)*100 for t1, t2 in zip(olsbRuntine,quantRuntime )]
		print(speedup)
		visualDf = visualDf.append({'Application':AppNamMap[filename], 'Error':'0.1', 'Speedup':speedup[0]}, ignore_index=True)
#		visualDf = visualDf.append({'Application':AppNamMap[filename], 'Error':'0.05', 'Speedup':speedup[1]}, ignore_index=True)
		visualDf = visualDf.append({'Application':AppNamMap[filename], 'Error':'0.01', 'Speedup':speedup[2]}, ignore_index=True)
		visualDf = visualDf.append({'Application':AppNamMap[filename], 'Error':'0.001', 'Speedup':speedup[3]}, ignore_index=True)
		print(AppNamMap[filename])		
	else:

		continue

plotAnewFigure ( xString="Applications", yString="Perfromance Improvement",xCol="Application",yCol="Speedup",hueCol="Error", fileString=figureName,InputArray=visualDf)
